from antlr4 import *

from QLCDNumber.ast_listener import XMLListenerToAst
from QLCDNumber.feature_tree_getter import FeatureTreeGetter
from QLCDNumber.code_generator import CodeGenerator
from gen.XMLLexer import XMLLexer
from gen.XMLParser import XMLParser


input_stream = FileStream(r"" + "input.xml")

# Phase 1
lexer = XMLLexer(input_stream)
stream = CommonTokenStream(lexer)
parser = XMLParser(stream)
document_ctx = parser.document()
feature_tree_getter = FeatureTreeGetter()
feature_tree_getter.visitDocument(document_ctx)
for tree in feature_tree_getter.feature_tree:
    print(tree.getText())
print('-'*150)

# Phase 2
ast_list = []
for tree in feature_tree_getter.feature_tree:
    walker = ParseTreeWalker()
    listener = XMLListenerToAst()
    walker.walk(t=tree, listener=listener)
    ast_list.append(listener)

for i in ast_list:
    i.printingAst()
    print("\n\n")

# phase 3
code_generator = CodeGenerator('generated_code.py', ast_list)
code_generator.generate_code()
