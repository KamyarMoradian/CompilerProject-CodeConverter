import os

from configuration import METHOD_LIB


class CodeGenerator:
    def __init__(self, output_address, asts_list):
        self.asts_list = asts_list
        if os.path.exists(output_address):
            os.remove(output_address)
        output = open(r"" + output_address, "a")
        self.output = output

    def generate_code(self):
        with open('layout.txt') as fh:
            layout_lines = fh.readlines()
        for line in layout_lines:
            self.output.write(line)

        counter = 1
        for i in self.asts_list:
            temp = "\t\t#" + i.root[1:-1] + "\n"
            self.output.write(temp)
            if "True" in i.init:
                temp = f'\t\t{i.root[1:-1]} = QRadioButton()\n'
            self.output.write(temp)
            for j in i.astTree:
                func = j.func
                if func in METHOD_LIB:
                    if func == "iconsize" or func == "down":
                        j.value = j.value[1:-1]
                    temp = "\t\t" + f"{i.root[1:-1]}." + METHOD_LIB[func] + j.value
                    if func == "icon" or func == "iconsize":
                        temp += "))\n"
                    else:
                        temp += ")\n"
                    self.output.write(temp)
            temp = f"\t\tlayout.addWidget(radiobutton,0,{str(counter)})\n"
            self.output.write(temp)
            counter += 1

        with open('footer.txt') as fh:
            layout_lines = fh.readlines()
        for line in layout_lines:
            self.output.write(line)
