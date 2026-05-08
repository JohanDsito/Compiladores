# ============================================================
#  code_generator.py
#  Generación de Código Intermedio (TAC/IR) y traducción a Python
#  Mini-compilador DroneScript
# ============================================================


# ─── REPRESENTACIÓN INTERMEDIA (TAC) ────────────────────────

class TACInstruction:
    """
    Instrucción de Código de Tres Direcciones (Three-Address Code).
    Formato:  op  arg1  arg2  result
    """
    def __init__(self, op, arg1=None, arg2=None, result=None):
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.result = result

    def __str__(self):
        if self.op == 'LABEL':
            return f"{self.result}:"
        if self.op == 'GOTO':
            return f"    GOTO {self.result}"
        if self.op == 'IF_FALSE':
            return f"    IF_FALSE ({self.arg1} {self.arg2[0]} {self.arg2[1]}) GOTO {self.result}"
        if self.op in ('DESPEGAR', 'ATERRIZAR', 'HOVER'):
            return f"    {self.op} {self.arg1}"
        if self.op == 'MOVER':
            return f"    MOVER {self.arg1} {self.arg2} {self.result}"
        if self.op == 'GIRAR':
            return f"    GIRAR {self.arg1} {self.arg2} {self.result}"
        if self.op == 'IR_A':
            return f"    IR_A {self.arg1} -> {self.result}"
        if self.op == 'ESPERAR':
            return f"    ESPERAR {self.arg1}s"
        if self.op == 'BEGIN_MISION':
            return f"BEGIN_MISION {self.result}"
        if self.op == 'END_MISION':
            return f"END_MISION {self.result}"
        if self.op == 'FOR_START':
            return f"    FOR_START n={self.arg1}"
        if self.op == 'FOR_END':
            return f"    FOR_END"
        return f"    {self.op} {self.arg1} {self.arg2} {self.result}"


# ─── GENERADOR PRINCIPAL ─────────────────────────────────────

class CodeGenerator:
    """
    Recorre el AST y produce:
      1. Lista de instrucciones TAC (código intermedio)
      2. Código Python ejecutable equivalente
    """

    def __init__(self, symbol_table):
        self.symbol_table = symbol_table
        self.tac: list[TACInstruction] = []
        self.py_lines: list[str] = []
        self._label_count = 0
        self._indent = 0          # nivel de indentación Python
        self._current_mission = None

    # ── Helpers ───────────────────────────────────────────────

    def _new_label(self, prefix="L"):
        self._label_count += 1
        return f"{prefix}{self._label_count}"

    def _ind(self, extra=0):
        return "    " * (self._indent + extra)

    def _emit(self, *args, **kwargs):
        self.tac.append(TACInstruction(*args, **kwargs))

    def _py(self, line: str):
        self.py_lines.append(self._ind() + line)

    # ── Entrada principal ─────────────────────────────────────

    def generate(self, tree):
        print("\n┌─────────────────────────────────────────────┐")
        print("│  FASE 4: GENERACIÓN DE CÓDIGO INTERMEDIO     │")
        print("└─────────────────────────────────────────────┘")

        self._gen_header()
        self._visit_program(tree)
        self._gen_footer()

        self._print_tac()
        return "\n".join(self.py_lines)

    # ── Cabecera Python ───────────────────────────────────────

    def _gen_header(self):
        self._py("import time")
        self._py("")
        self._py("# ── Estado de los drones ──────────────────────────────")
        for name in self.symbol_table.drones:
            self._py(f"{name} = {{'en_vuelo': False, 'x': 0.0, 'y': 0.0, "
                     f"'altitud': 0.0, 'bateria': 100, 'orientacion': 0}}")
        self._py("")
        self._py("# ── Zonas declaradas ──────────────────────────────────")
        zona_items = ", ".join(
            f"'{n}': {coords}" for n, coords in self.symbol_table.zonas.items()
        )
        self._py(f"zonas = {{{zona_items}}}")
        self._py("")

    def _gen_footer(self):
        self._py("")
        self._py("# ── Punto de entrada ──────────────────────────────────")
        self._py("if __name__ == '__main__':")
        self._indent += 1
        # Llamar misiones en orden de aparición
        for name in self._mission_names:
            self._py(f"{name}()")
        if not self._mission_names:
            self._py("pass")
        self._indent -= 1

    # ── Visita el programa ────────────────────────────────────

    def _mission_names_collect(self, tree):
        """Pre-pasa para recolectar nombres de misiones en orden."""
        from generated.gramaticaParser import gramaticaParser
        names = []
        for child in tree.getChildren():
            if isinstance(child, gramaticaParser.MissionContext):
                names.append(child.ID().getText())
        return names

    def _visit_program(self, tree):
        from generated.gramaticaParser import gramaticaParser
        self._mission_names = self._mission_names_collect(tree)
        for child in tree.getChildren():
            if isinstance(child, gramaticaParser.MissionContext):
                self._visit_mission(child)
            elif isinstance(child, gramaticaParser.CommandContext):
                # comandos sueltos fuera de misión
                self._visit_command(child)

    # ── Misión → función Python ───────────────────────────────

    def _visit_mission(self, ctx):
        name = ctx.ID().getText()
        self._current_mission = name
        self._emit('BEGIN_MISION', result=name)

        self._py(f"# ── Misión: {name} ────────────────────────────────────")
        self._py(f"def {name}():")
        self._indent += 1

        for cmd in ctx.command():
            self._visit_command(cmd)

        self._indent -= 1
        self._py("")
        self._emit('END_MISION', result=name)
        self._current_mission = None

    # ── Comandos ──────────────────────────────────────────────

    def _visit_command(self, ctx):
        from generated.gramaticaParser import gramaticaParser
        if ctx.action():
            self._visit_action(ctx.action())
        elif ctx.control():
            self._visit_control(ctx.control())
        elif ctx.waitCmd():
            self._visit_wait(ctx.waitCmd())

    # ── Acciones ──────────────────────────────────────────────

    def _visit_action(self, ctx):
        from generated.gramaticaParser import gramaticaParser

        if isinstance(ctx, gramaticaParser.SimpleActionContext):
            keyword = ctx.getChild(0).getText()
            drone = ctx.ID().getText()

            if keyword == 'despegar':
                self._emit('DESPEGAR', arg1=drone)
                self._py(f"# despegar {drone}")
                self._py(f"{drone}['en_vuelo'] = True")
                self._py(f"{drone}['altitud'] = 1.0")

            elif keyword == 'aterrizar':
                self._emit('ATERRIZAR', arg1=drone)
                self._py(f"# aterrizar {drone}")
                self._py(f"{drone}['en_vuelo'] = False")
                self._py(f"{drone}['altitud'] = 0.0")

            elif keyword == 'hover':
                self._emit('HOVER', arg1=drone)
                self._py(f"# hover {drone}")
                self._py(f"# {drone} mantiene posición (hover)")

        elif isinstance(ctx, gramaticaParser.MoverActionContext):
            drone = ctx.ID().getText()
            direction = ctx.direction().getText()
            value = ctx.NUMBER().getText()
            self._emit('MOVER', arg1=drone, arg2=direction, result=value)
            self._py(f"# mover {drone} {direction} {value}")
            self._py(self._mover_py(drone, direction, value))

        elif isinstance(ctx, gramaticaParser.IrAActionContext):
            ids = ctx.ID()
            drone = ids[0].getText()
            zona = ids[1].getText()
            self._emit('IR_A', arg1=drone, result=zona)
            self._py(f"# ir_a {drone} -> {zona}")
            self._py(f"{drone}['x'], {drone}['y'] = zonas['{zona}']")

        elif isinstance(ctx, gramaticaParser.GirarActionContext):
            drone = ctx.ID().getText()
            direccion = ctx.getChild(2).getText()   # 'izquierda' o 'derecha'
            angle = ctx.NUMBER().getText()
            self._emit('GIRAR', arg1=drone, arg2=direccion, result=angle)
            self._py(f"# girar {drone} {direccion} {angle}°")
            sign = "+" if direccion == "derecha" else "-"
            self._py(
                f"{drone}['orientacion'] = ({drone}.get('orientacion', 0) "
                f"{sign} {angle}) % 360"
            )

    def _mover_py(self, drone, direction, value):
        mapping = {
            'arriba':    f"{drone}['altitud'] += {value}",
            'abajo':     f"{drone}['altitud'] -= {value}",
            'adelante':  f"{drone}['x'] += {value}",
            'atras':     f"{drone}['x'] -= {value}",
            'izquierda': f"{drone}['y'] -= {value}",
            'derecha':   f"{drone}['y'] += {value}",
        }
        return mapping.get(direction, f"# dirección desconocida: {direction}")

    # ── Control ───────────────────────────────────────────────

    def _visit_control(self, ctx):
        from generated.gramaticaParser import gramaticaParser

        if isinstance(ctx, gramaticaParser.SiControlContext):
            cond = ctx.condition()
            drone = cond.ID().getText()
            sensor = cond.sensor().getText()
            op = cond.comparator().getText()
            val = cond.NUMBER().getText()

            label_else = self._new_label("ELSE")
            label_end  = self._new_label("END_SI")

            self._emit('IF_FALSE', arg1=drone,
                       arg2=(f"{sensor} {op}", val), result=label_else)

            self._py(f"# si {drone}.{sensor} {op} {val}")
            self._py(f"if {drone}['{sensor}'] {op} {val}:")
            self._indent += 1
            cmds = ctx.command()
            self._visit_command(cmds[0])
            self._indent -= 1

            if len(cmds) > 1:
                self._emit('GOTO', result=label_end)
                self._emit('LABEL', result=label_else)
                self._py("else:")
                self._indent += 1
                self._visit_command(cmds[1])
                self._indent -= 1
                self._emit('LABEL', result=label_end)

        elif isinstance(ctx, gramaticaParser.RepetirControlContext):
            count = ctx.NUMBER().getText()
            label_loop = self._new_label("LOOP")
            label_end  = self._new_label("END_LOOP")

            self._emit('FOR_START', arg1=count)
            self._emit('LABEL', result=label_loop)

            self._py(f"# repetir {count} veces")
            self._py(f"for _ in range({count}):")
            self._indent += 1
            for cmd in ctx.command():
                self._visit_command(cmd)
            self._indent -= 1

            self._emit('GOTO', result=label_loop)
            self._emit('FOR_END')

    # ── Esperar ───────────────────────────────────────────────

    def _visit_wait(self, ctx):
        seconds = ctx.NUMBER().getText()
        self._emit('ESPERAR', arg1=seconds)
        self._py(f"# esperar {seconds}s")
        self._py(f"time.sleep({seconds})")

    # ── Imprimir TAC ──────────────────────────────────────────

    def _print_tac(self):
        print("\n  ── Código Intermedio (TAC) ──────────────────────")
        for instr in self.tac:
            print(f"  {instr}")
        print()
