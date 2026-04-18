class SymbolTable:
    """
    Tabla de Simbolos con soporte para ambitos (scopes) anidados.
    Cada ambito tiene su propio diccionario de variables.
    """

    def __init__(self):
        # Pila de ambitos: cada elemento es un dict {nombre: tipo}
        self.scopes = [{}]

    def enter_scope(self):
        """Entra a un nuevo ambito (push)."""
        self.scopes.append({})

    def exit_scope(self):
        """Sale del ambito actual (pop)."""
        if len(self.scopes) > 1:
            self.scopes.pop()

    def declare(self, name, var_type):
        """
        Declara una variable en el ambito actual.
        Retorna False si ya existe en el mismo ambito (redeclaracion).
        """
        current_scope = self.scopes[-1]
        if name in current_scope:
            return False  # Redeclaracion en el mismo ambito
        current_scope[name] = var_type
        return True

    def lookup(self, name):
        """
        Busca una variable recorriendo los ambitos desde el mas interno.
        Retorna el tipo si la encuentra, None si no existe.
        """
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        return None

    def is_declared_in_current_scope(self, name):
        """Verifica si una variable fue declarada en el ambito actual."""
        return name in self.scopes[-1]
