# semantic_analyzer/SymbolTable.py

class Symbol:
    def __init__(self, name, type):
        self.name = name
        self.type = type

class SymbolTable:
    def __init__(self):
        # Una lista de diccionarios. El último es el ámbito actual.
        self.scope_stack = [{}]

    def enter_scope(self):
        # Inicia un nuevo ámbito
        self.scope_stack.append({})

    def exit_scope(self):
        # Sale del ámbito actual
        if len(self.scope_stack) > 1:
            self.scope_stack.pop()

    def insert(self, name, symbol):
        # Inserta en el ámbito actual (el último de la lista)
        current_scope = self.scope_stack[-1]
        if name in current_scope:
            print(f"Error Semántico: La variable '{name}' ya ha sido declarada en este ámbito.")
            return False
        current_scope[name] = symbol
        return True

    def lookup(self, name):
        # Busca desde el ámbito actual hacia los exteriores (global)
        for scope in reversed(self.scope_stack):
            if name in scope:
                return scope[name]
        return None # No se encontró en ningún ámbito