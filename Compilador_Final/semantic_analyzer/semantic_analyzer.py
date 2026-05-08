# ============================================================
#  semantic_analyzer.py
#  Análisis Semántico — Tabla de Símbolos y Validaciones
#  Mini-compilador DroneScript
# ============================================================

class SemanticError(Exception):
    """Error semántico con número de línea y mensaje descriptivo."""
    def __init__(self, message, line=None):
        self.line = line
        prefix = f"[Error Semántico - Línea {line}]" if line else "[Error Semántico]"
        super().__init__(f"{prefix} {message}")


class SemanticWarning:
    """Advertencia semántica (no detiene compilación)."""
    def __init__(self, message, line=None):
        self.line = line
        prefix = f"[Advertencia - Línea {line}]" if line else "[Advertencia]"
        self.message = f"{prefix} {message}"

    def __str__(self):
        return self.message


# ─── TABLA DE SÍMBOLOS ───────────────────────────────────────

class SymbolTable:
    """
    Tabla de símbolos que almacena drones y zonas declarados.
    También lleva el estado en vuelo de cada drone para validaciones.
    """

    def __init__(self):
        self.drones: dict[str, dict] = {}   # nombre -> {en_vuelo, linea_decl}
        self.zonas: dict[str, tuple] = {}    # nombre -> (x, y)

    def declare_drone(self, name: str, line: int = None):
        if name in self.drones:
            raise SemanticError(f"El drone '{name}' ya fue declarado.", line)
        if name in self.zonas:
            raise SemanticError(f"'{name}' ya existe como zona.", line)
        self.drones[name] = {"en_vuelo": False, "linea_decl": line}
        print(f"  [Tabla] Drone registrado: '{name}'")

    def declare_zona(self, name: str, x: float, y: float, line: int = None):
        if name in self.zonas:
            raise SemanticError(f"La zona '{name}' ya fue declarada.", line)
        if name in self.drones:
            raise SemanticError(f"'{name}' ya existe como drone.", line)
        self.zonas[name] = (x, y)
        print(f"  [Tabla] Zona registrada: '{name}' en ({x}, {y})")

    def get_drone(self, name: str, line: int = None) -> dict:
        if name not in self.drones:
            raise SemanticError(
                f"El drone '{name}' no fue declarado. Decláralo con: drone {name};", line
            )
        return self.drones[name]

    def get_zona(self, name: str, line: int = None) -> tuple:
        if name not in self.zonas:
            raise SemanticError(
                f"La zona '{name}' no existe. Declárala con: zona {name}(x, y);", line
            )
        return self.zonas[name]

    def set_en_vuelo(self, name: str, estado: bool):
        self.drones[name]["en_vuelo"] = estado

    def esta_en_vuelo(self, name: str) -> bool:
        return self.drones[name]["en_vuelo"]

    def __str__(self):
        lines = ["\n╔══════════════ TABLA DE SÍMBOLOS ══════════════╗"]
        if self.drones:
            lines.append("  DRONES:")
            for name, info in self.drones.items():
                lines.append(f"    • {name:<15} (declarado en línea {info['linea_decl']})")
        if self.zonas:
            lines.append("  ZONAS:")
            for name, coords in self.zonas.items():
                lines.append(f"    • {name:<15} coordenadas {coords}")
        lines.append("╚════════════════════════════════════════════════╝")
        return "\n".join(lines)


# ─── ANALIZADOR SEMÁNTICO ────────────────────────────────────

class SemanticAnalyzer:
    """
    Recorre el AST generado por ANTLR4 y aplica todas las
    reglas semánticas del lenguaje DroneScript.
    """

    def __init__(self):
        self.symbol_table = SymbolTable()
        self.errors: list[SemanticError] = []
        self.warnings: list[SemanticWarning] = []
        self.dentro_de_mision = False

    # ── Entrada principal ─────────────────────────────────────

    def analyze(self, tree, parser=None):
        """Analiza el árbol AST completo."""
        print("\n┌─────────────────────────────────────────────┐")
        print("│       FASE 3: ANÁLISIS SEMÁNTICO             │")
        print("└─────────────────────────────────────────────┘")
        try:
            self._visit_program(tree)
        except SemanticError as e:
            self.errors.append(e)

        print(self.symbol_table)
        self._report()
        return len(self.errors) == 0

    # ── Visita nodos del AST ──────────────────────────────────

    def _visit_program(self, tree):
        from generated.gramaticaParser import gramaticaParser
        for child in tree.getChildren():
            ctx_type = type(child).__name__
            if isinstance(child, gramaticaParser.DronDeclContext):
                self._visit_drone_decl(child)
            elif isinstance(child, gramaticaParser.ZonaDeclContext):
                self._visit_zona_decl(child)
            elif isinstance(child, gramaticaParser.MissionContext):
                self._visit_mission(child)
            elif isinstance(child, gramaticaParser.CommandContext):
                self._visit_command(child)

    def _visit_drone_decl(self, ctx):
        name = ctx.ID().getText()
        line = ctx.start.line
        try:
            self.symbol_table.declare_drone(name, line)
        except SemanticError as e:
            self.errors.append(e)

    def _visit_zona_decl(self, ctx):
        name = ctx.ID().getText()
        line = ctx.start.line
        nums = ctx.NUMBER()
        x, y = float(nums[0].getText()), float(nums[1].getText())
        try:
            self.symbol_table.declare_zona(name, x, y, line)
        except SemanticError as e:
            self.errors.append(e)

    def _visit_mission(self, ctx):
        from generated.gramaticaParser import gramaticaParser
        name = ctx.ID().getText()
        line = ctx.start.line
        print(f"  [Semántico] Analizando misión: '{name}'")
        self.dentro_de_mision = True

        # Advertencia: verificar batería de todos los drones declarados
        for drone_name in self.symbol_table.drones:
            self.warnings.append(SemanticWarning(
                f"Antes de iniciar misión '{name}', verifique batería del drone '{drone_name}'.",
                line
            ))

        for cmd in ctx.command():
            self._visit_command(cmd)

        self.dentro_de_mision = False

    def _visit_command(self, ctx):
        from generated.gramaticaParser import gramaticaParser
        if ctx.action():
            self._visit_action(ctx.action())
        elif ctx.control():
            self._visit_control(ctx.control())
        elif ctx.waitCmd():
            pass  # esperar no requiere validación semántica adicional

    def _visit_action(self, ctx):
        from generated.gramaticaParser import gramaticaParser
        line = ctx.start.line

        if isinstance(ctx, gramaticaParser.SimpleActionContext):
            keyword = ctx.getChild(0).getText()
            drone_name = ctx.ID().getText()
            try:
                drone = self.symbol_table.get_drone(drone_name, line)
                if keyword == 'despegar':
                    if drone["en_vuelo"]:
                        raise SemanticError(
                            f"El drone '{drone_name}' ya está en vuelo. No puede despegar de nuevo.", line
                        )
                    self.symbol_table.set_en_vuelo(drone_name, True)
                    print(f"  [Semántico] '{drone_name}' despega ✓")

                elif keyword == 'aterrizar':
                    if not drone["en_vuelo"]:
                        raise SemanticError(
                            f"El drone '{drone_name}' no está en vuelo. No puede aterrizar.", line
                        )
                    self.symbol_table.set_en_vuelo(drone_name, False)
                    print(f"  [Semántico] '{drone_name}' aterriza ✓")

                elif keyword == 'hover':
                    if not drone["en_vuelo"]:
                        raise SemanticError(
                            f"El drone '{drone_name}' debe estar en vuelo para hacer hover.", line
                        )
            except SemanticError as e:
                self.errors.append(e)

        elif isinstance(ctx, gramaticaParser.MoverActionContext):
            drone_name = ctx.ID().getText()
            value = float(ctx.NUMBER().getText())
            try:
                drone = self.symbol_table.get_drone(drone_name, line)
                if not drone["en_vuelo"]:
                    raise SemanticError(
                        f"El drone '{drone_name}' debe despegar antes de moverse.", line
                    )
                if value <= 0:
                    raise SemanticError(
                        f"El valor de movimiento debe ser positivo, se recibió {value}.", line
                    )
                print(f"  [Semántico] mover '{drone_name}' → valor={value} ✓")
            except SemanticError as e:
                self.errors.append(e)

        elif isinstance(ctx, gramaticaParser.IrAActionContext):
            ids = ctx.ID()
            drone_name = ids[0].getText()
            zona_name = ids[1].getText()
            try:
                drone = self.symbol_table.get_drone(drone_name, line)
                if not drone["en_vuelo"]:
                    raise SemanticError(
                        f"El drone '{drone_name}' debe despegar antes de ir a una zona.", line
                    )
                self.symbol_table.get_zona(zona_name, line)   # valida existencia
                print(f"  [Semántico] ir_a '{drone_name}' → zona '{zona_name}' ✓")
            except SemanticError as e:
                self.errors.append(e)

        elif isinstance(ctx, gramaticaParser.GirarActionContext):
            drone_name = ctx.ID().getText()
            value = float(ctx.NUMBER().getText())
            try:
                drone = self.symbol_table.get_drone(drone_name, line)
                if not drone["en_vuelo"]:
                    raise SemanticError(
                        f"El drone '{drone_name}' debe estar en vuelo para girar.", line
                    )
                if value <= 0:
                    raise SemanticError(
                        f"El ángulo de giro debe ser positivo, se recibió {value}.", line
                    )
                print(f"  [Semántico] girar '{drone_name}' → {value}° ✓")
            except SemanticError as e:
                self.errors.append(e)

    def _visit_control(self, ctx):
        from generated.gramaticaParser import gramaticaParser
        line = ctx.start.line

        if isinstance(ctx, gramaticaParser.SiControlContext):
            # Validar condición: el drone del sensor debe existir
            cond = ctx.condition()
            drone_name = cond.ID().getText()
            try:
                self.symbol_table.get_drone(drone_name, line)
            except SemanticError as e:
                self.errors.append(e)
            for cmd in ctx.command():
                self._visit_command(cmd)

        elif isinstance(ctx, gramaticaParser.RepetirControlContext):
            count = int(ctx.NUMBER().getText())
            if count <= 0:
                self.errors.append(SemanticError(
                    f"El número de repeticiones debe ser positivo, se recibió {count}.", line
                ))
            for cmd in ctx.command():
                self._visit_command(cmd)

    # ── Reporte final ─────────────────────────────────────────

    def _report(self):
        if self.warnings:
            print("\n⚠️  ADVERTENCIAS SEMÁNTICAS:")
            for w in self.warnings:
                print(f"  {w}")

        if self.errors:
            print(f"\n❌ Se encontraron {len(self.errors)} error(es) semántico(s):")
            for e in self.errors:
                print(f"  {e}")
        else:
            print("\n✅ Análisis semántico completado sin errores.")
