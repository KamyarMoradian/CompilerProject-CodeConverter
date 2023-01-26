from gen.XMLParser import XMLParser
from gen.XMLParserVisitor import XMLParserVisitor


class FeatureTreeGetter(XMLParserVisitor):
    def __init__(self):
        self.feature_tree = []

    def visitDocument(self, ctx: XMLParser.DocumentContext):
        return self.visitChildren(ctx)

    def visitContent(self, ctx: XMLParser.ContentContext):
        return self.visitChildren(ctx)

    def visitElement(self, ctx: XMLParser.ElementContext):
        if ctx.Name(0) is not None and ctx.Name(0).getText() == "lcdnumber":
            self.feature_tree.append(ctx)
        return self.visitChildren(ctx)
