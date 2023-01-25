from gen.XMLParserListener import XMLParserListener
from gen.XMLParser import XMLParser


class Child():
    def __init__(self):
        self.func = ""
        self.value = ""


class XMLListenerToAst(XMLParserListener):
    def __init__(self):
        self.astTree = []
        self.root = ""
        self.init = "False"

    def enterElement(self, ctx: XMLParser.ElementContext):
        self.root = str(ctx.Name()[0])

    def enterAttribute(self, ctx: XMLParser.AttributeContext):
        temp = Child()

        if str(ctx.Name()) == "init":
            self.init = str(ctx.STRING())


        if str(ctx.Name()) == "objectName":
            self.root = str(ctx.STRING())
        else:
            temp.func = str(ctx.Name())
            temp.value = str(ctx.STRING())
            self.astTree.append(temp)

    def printingAst(self):
        print(self.root)
        print("|")
        for i in range(len(self.astTree)):
            print("|___________",
                  self.astTree[i].func, "--->", self.astTree[i].value)
            if i != len(self.astTree)-1:
                print("|")
