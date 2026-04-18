# WhileLang — Analizador Semantico con ANTLR4

## Estructura del Proyecto

```
/workspace
├── WhileLang.g4
├── input.txt
├── test.py
├── main.py
├── generated/
│   ├── WhileLangLexer.py
│   ├── WhileLangParser.py
│   ├── WhileLangListener.py
│   └── WhileLangVisitor.py
└── semantic_analyzer/
    ├── __init__.py
    ├── SymbolTable.py
    └── SemanticVisitor.py
```

## Requisitos

- Python 3.8+
- Java (para ANTLR4)
- antlr4-python3-runtime

```bash
pip install antlr4-python3-runtime
```

## Generacion del Parser (comando exacto)

```bash
java -jar antlr-4.13.1-complete.jar -Dlanguage=Python3 -visitor -o generated WhileLang.g4
```

## Ejecucion

### Ejecutar todos los casos de prueba
```bash
python test.py
```

### Analizar un archivo especifico
```bash
python main.py input.txt
```
