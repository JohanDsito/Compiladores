from antlr4 import *
from Saludo2Lexer import Saludo2Lexer
from Saludo2Parser import Saludo2Parser


input_stream = InputStream("hola Juan")


lexer = Saludo2Lexer(input_stream)


token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("TOKENS:")

for token in token_stream.tokens:
    if token.type != Token.EOF:

        if token.type < len(lexer.symbolicNames):
            token_name = lexer.symbolicNames[token.type]
        else:
            token_name = str(token.type)

        print(f"Texto: {token.text}  Tipo: {token_name}")

# Crear parser
parser = Saludo2Parser(token_stream)

# Regla inicial
tree = parser.saludo()

print("\nÁRBOL SINTÁCTICO:")
print(tree.toStringTree(recog=parser))