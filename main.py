from antlr4 import *

from gen.XMLLexer import XMLLexer
from gen.XMLParser import XMLParser

from QLCDNumber.feature_tree_getter import FeatureTreeGetter


def main(input_text):
    input_stream = InputStream(input_text)
    lexer = XMLLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = XMLParser(stream)
    document_ctx = parser.document()
    feature_tree_getter = FeatureTreeGetter()
    feature_tree_getter.visitDocument(document_ctx)
    print(feature_tree_getter.feature_tree)
    print(feature_tree_getter.feature_tree[0].attribute()[0].Name().getText())


if __name__ == '__main__':
    main("<class>"
            "<function>"
                "<CLabel objectName=\"qlabel\" method=\"init\" parameter=\"\"/>"
            "<QLCDNumber objectName=\"lcdNumber\" method=\"init\" parameter=\"\"/>"
            "</function>"
            "<function>"
                "<QLCDNumber objectName=\"lcdNumber\" method=\"set\" parameter=\"2\"/>"
            "</function>"
         "</class>")
