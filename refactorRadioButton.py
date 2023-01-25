from antlr4 import *
from gen.XMLLexer import XMLLexer
from gen.XMLParser import XMLParser
from ASTListener import XMLListenerToAst
from map import map
import os

input_stream = FileStream(r""+"input.xml")

output_address = "genereatedcode.py"
if os.path.exists(output_address):
    os.remove(output_address)

output = open(r"" + output_address, "a")

lexer = XMLLexer(input_stream)

token = lexer.nextToken()
refactored = []
while token.type != Token.EOF:
    if token.text == "lcdNumber":
        text = "<lcdNumber "
        token = lexer.nextToken()
        while token.type != lexer.SLASH_CLOSE:
            text += token.text
            token = lexer.nextToken()
        text += token.text
        refactored.append(text)
    token = lexer.nextToken()


# create ast
astsList = []
for text in refactored:
    input_stream = InputStream(text)
    lexer = XMLLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = XMLParser(token_stream)
    parseTree = parser.document()
    walker = ParseTreeWalker()
    listener = XMLListenerToAst()
    walker.walk(t=parseTree, listener=listener)
    astsList.append(listener)

for i in astsList:
    i.printingAst()
    print("\n\n")


# generate code
pyQt5 = "from PyQt5.QtWidgets import *\n"
pyQt5core =   "from PyQt5.QtCore import QSize\n"
pyQtgu= "from PyQt5.QtGui import QIcon\n"
sys="import sys\nclass Window(QWidget):\n"
def__init__="\tdef __init__(self):\n"
QWid= "\t\tQWidget.__init__(self)\n"
lay="\t\tlayout = QGridLayout()\n"
selfset="\t\tself.setLayout(layout)\n"
output.write(pyQt5)
output.write(pyQt5core)
output.write(pyQtgu)
output.write(sys)
output.write(def__init__)
output.write(QWid)
output.write(lay)
output.write(selfset)
functions = map().functions
counter = 1
for i in astsList:
    temp = "\t\t#" + i.root[1:-1] + "\n"
    output.write(temp)
    if  "True" in i.init:
        temp = f'\t\t{i.root[1:-1]} = QRadioButton()\n'
    output.write(temp)
    for j in i.astTree:
        func = j.func
        if func in functions:
            if func == "iconsize" or func== "down":
                j.value = j.value[1:-1]
            temp = "\t\t" +f"{i.root[1:-1]}." + functions[func] + j.value
            if func == "icon" or func == "iconsize":
                temp += "))\n"
            else:
                temp += ")\n"
            output.write(temp)
    temp = f"\t\tlayout.addWidget(radiobutton,0,{str(counter)})\n"
    output.write(temp)
    counter += 1
footer = "app = QApplication(sys.argv)\n"
screen = "screen = Window()\n"
screenShow = "screen.show()\n"
sysExit = "sys.exit(app.exec_())"
output.write(footer)
output.write(screen)
output.write(screenShow)
output.write(sysExit)
