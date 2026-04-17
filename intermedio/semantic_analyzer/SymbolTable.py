# semantic_analyzer/SymbolTable.py

class Symbol:
    """
    Representa un símbolo en la tabla. Puede ser una variable o una función.
    """
    def __init__(self, name, type, category=None, params=None):
        self.name = name
        # Para variables, 'type' es su tipo de dato.
        # Para funciones, 'type' es su tipo de RETORNO.
        self.type = type
        self.category = category  # 'variable' o 'function'
        self.params = params if params is not None else [] # Lista de Símbolos de parámetros

    def __str__(self):
        return f"<Symbol(name='{self.name}', type='{self.type}', category='{self.category}')>"

class Scope:
    """
    Representa un ámbito (scope), que contiene una tabla de símbolos.
    """
    def __init__(self, name, enclosing_scope=None):
        self.name = name
        self.symbols = {}
        self.enclosing_scope = enclosing_scope

    def insert(self, symbol):
        """Define un nuevo símbolo en el ámbito actual."""
        if symbol.name in self.symbols:
            # Devuelve False si el símbolo ya existe en este ámbito
            return False
        self.symbols[symbol.name] = symbol
        return True

    def lookup(self, name):
        """Busca un símbolo en este ámbito o en los ámbitos padres."""
        symbol = self.symbols.get(name)
        if symbol:
            return symbol
        if self.enclosing_scope:
            return self.enclosing_scope.lookup(name)
        return None

class SymbolTable:
    """
    Gestiona la pila de ámbitos.
    """
    def __init__(self):
        self.current_scope = Scope("global")

    def enter_scope(self):
        """Entra a un nuevo ámbito anidado."""
        new_scope = Scope("local", enclosing_scope=self.current_scope)
        self.current_scope = new_scope

    def exit_scope(self):
        """Sale del ámbito actual y regresa al padre."""
        if self.current_scope.enclosing_scope:
            self.current_scope = self.current_scope.enclosing_scope

    def insert(self, name, symbol):
        """Inserta un símbolo en el ámbito actual."""
        print(f"Definiendo '{name}' en el ámbito '{self.current_scope.name}'")
        if not self.current_scope.insert(symbol):
             print(f"Error Semántico: El símbolo '{name}' ya ha sido declarado en este ámbito.")
             # En un compilador real, aquí se detendría o se registraría un error.

    def lookup(self, name):
        """Busca un símbolo en todos los ámbitos visibles."""
        return self.current_scope.lookup(name)