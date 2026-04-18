from antlr4 import *
from Expr2Lexer import Expr2Lexer
from Expr2Parser import Expr2Parser


input_stream = InputStream("3+4*5")

lexer = Expr2Lexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("TOKENS:")

for token in token_stream.tokens:
    if token.type != Token.EOF:

        if token.type < len(lexer.symbolicNames):
            token_name = lexer.symbolicNames[token.type]
        else:
            token_name = lexer.literalNames[token.type]

        print(f"Texto: {token.text}  Tipo: {token_name}")

parser = Expr2Parser(token_stream)

tree = parser.prog()

print("\nÁRBOL SINTÁCTICO:")
print(tree.toStringTree(recog=parser))