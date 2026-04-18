from antlr4 import *
from Expr3Lexer import Expr3Lexer
from Expr3Parser import Expr3Parser


input_stream = InputStream("3+4*5")

lexer = Expr3Lexer(input_stream)
token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("TOKENS:")

for token in token_stream.tokens:
    if token.type != Token.EOF:

        if token.type < len(lexer.symbolicNames) and lexer.symbolicNames[token.type] is not None:
            token_name = lexer.symbolicNames[token.type]
        else:
            token_name = lexer.literalNames[token.type]

        print(f"Texto: {token.text}  Tipo: {token_name}")

parser = Expr3Parser(token_stream)

tree = parser.expr()

print("\nÁRBOL SINTÁCTICO:")
print(tree.toStringTree(recog=parser))