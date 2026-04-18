from antlr4 import *
from Expr4Lexer import Expr4Lexer
from Expr4Parser import Expr4Parser


input_stream = InputStream("(3+4)*5")


lexer = Expr4Lexer(input_stream)


token_stream = CommonTokenStream(lexer)
token_stream.fill()

print("TOKENS:")

for token in token_stream.tokens:
    if token.type != Token.EOF:

        token_name = lexer.symbolicNames[token.type]

        if token_name is None:
            token_name = lexer.literalNames[token.type]

        print(f"Texto: {token.text}  Tipo: {token_name}")

# Parser
parser = Expr4Parser(token_stream)

tree = parser.expr()

print("\nÁRBOL SINTÁCTICO:")
print(tree.toStringTree(recog=parser))