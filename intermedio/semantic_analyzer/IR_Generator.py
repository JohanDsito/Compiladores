# semantic_analyzer/IR_Generator.py

class IR_Generator:
    def __init__(self):
        self.instructions = []  # Lista para guardar las instrucciones TAC
        self.temp_count = 0     # Contador para variables temporales (t0, t1, t2...)
        self.label_count = 0    # Contador para etiquetas (L0, L1, L2...)

    def new_temp(self):
        """Crea una nueva variable temporal y la devuelve."""
        temp_name = f"t{self.temp_count}"
        self.temp_count += 1
        return temp_name

    def new_label(self):
        """Crea una nueva etiqueta y la devuelve."""
        label_name = f"L{self.label_count}"
        self.label_count += 1
        return label_name

    def add_instruction(self, op, arg1=None, arg2=None, result=None):
        """Añade una instrucción a la lista."""
        self.instructions.append({'op': op, 'arg1': arg1, 'arg2': arg2, 'result': result})

    def __str__(self):
        """Genera una representación en texto del código IR."""
        output = "## CÓDIGO INTERMEDIO (TAC)\n"
        for inst in self.instructions:
            op = inst['op']
            if op in ['+', '-', '*', '/', '<', '>', '>=', '<=', '==', '!=']:
                # Formato: result = arg1 op arg2
                output += f"  {inst['result']} = {inst['arg1']} {op} {inst['arg2']}\n"
            elif op == '=':
                # Formato: result = arg1
                output += f"  {inst['result']} = {inst['arg1']}\n"
            elif op == 'if_false_goto':
                # Formato: if_false arg1 goto result
                output += f"  if_false {inst['arg1']} goto {inst['result']}\n"
            elif op == 'goto':
                # Formato: goto result
                output += f"  goto {inst['result']}\n"
            elif op.endswith(':'):
                # Formato: op (ej. L1:)
                output += f"{op}\n"
        return output