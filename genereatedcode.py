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
		my_object = QRadioButton()
		my_object.setText("salam")
		my_object.setIcon(QIcon("img.svg"))
		my_object.setIconSize(QSize(30,30))
		my_object.isChecked("True")
		layout.addWidget(radiobutton,0,1)
app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())