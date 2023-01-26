from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSize
from PyQt5.QtGui import QIcon
import sys


class Window(QWidget):
	def __init__(self):
		QWidget.__init__(self)
		layout = QGridLayout()
		self.setLayout(layout)
		#my_object
		my_object = QLCDNumber()
		my_object.setStyleSheet('background-color:yellow; color:blue')
		my_object.display('12:23')
		layout.addWidget(my_object, 0, 1)


app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())
