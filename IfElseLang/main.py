
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener 

from generated.IfElseLangLexer import IfElseLangLexer
from generated.IfElseLangParser import IfElseLangParser
from semantic_analyzer.SemanticVisitor import SemanticVisitor

class MyErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        # Lanza una excepción para detener la ejecución de inmediato
        raise Exception(f"Error de sintaxis en la línea {line}:{column} - {msg}")

def main():
    try:
        input_stream = FileStream("input.txt", encoding='utf-8')
        lexer = IfElseLangLexer(input_stream)
        lexer.removeErrorListeners()
        lexer.addErrorListener(MyErrorListener()) # Ahora Python sabe qué es MyErrorListener

        stream = CommonTokenStream(lexer)
        parser = IfElseLangParser(stream)
        parser.removeErrorListeners()
        parser.addErrorListener(MyErrorListener())

        tree = parser.program()
        print("Análisis sintáctico completado sin errores.")

        visitor = SemanticVisitor() 
        visitor.visit(tree)
        print("Análisis semántico completado.") 

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()