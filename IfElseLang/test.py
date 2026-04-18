from antlr4 import *
from generated.IfElseLangLexer import IfElseLangLexer
from generated.IfElseLangParser import IfElseLangParser
from antlr4.tree.Tree import TerminalNode

# === Entrada de prueba ===
input_text = """a = 10;
b = 20;
if (a > b) {
max = a;
} else {
if (a == b) {
    max = a;
} else {
    max = b;
}
}
"""

# === Crear flujo de entrada ===
input_stream = InputStream(input_text)

# === Fase léxica ===
lexer = IfElseLangLexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("## TOKENS")

rule_names = lexer.ruleNames

print(f"{'TOKEN================::{rule_names[0]}':<12} -> '{token_stream.tokens[0].text}' @ {token_stream.tokens[0].line}:{token_stream.tokens[0].column}")

print("====================================")
for token in token_stream.tokens:
    if token.type != Token.EOF:
        # Obtener nombre correcto del token
        if 0 < token.type <= len(rule_names):
            name = rule_names[token.type - 1]
        else:
            name = str(token.type)

        print(f"{name:<12} -> '{token.text}' @ {token.line}:{token.column}")

# === Fase sintáctica ===
parser = IfElseLangParser(token_stream)

print("\n## ÁRBOL SINTÁCTICO (toStringTree)")
tree = parser.program()
print(tree.toStringTree(recog=parser))

# === Representación indentada ===
def pretty_tree(node, rule_names, level=0):
    indent = "  " * level

    if isinstance(node, TerminalNode):
        return f"{indent}TOKEN({node.getText()})"
    else:
        rule_name = rule_names[node.getRuleIndex()]
        result = f"{indent}{rule_name}"

        for child in node.children or []:
            result += "\n" + pretty_tree(child, rule_names, level + 1)

        return result

print("\n## ÁRBOL SINTÁCTICO (Indentado)")
print(pretty_tree(tree, parser.ruleNames))