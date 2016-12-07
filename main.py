from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QVBoxLayout, QSizePolicy
#from PyQt5.QtCore import QObject
import sys
from input_dialog import InputDialog
from report_dialog import ReportDialog

class MainWindow(QDialog):
	def __init__(self, parent=None):
		QDialog.__init__(self, parent)
		self.setWindowTitle('В ФМС')
		self.inputButton = QPushButton("Ввод данных")
		self.inputButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.reportButton = QPushButton("Отчет")
		self.reportButton.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
		self.layout = QVBoxLayout()
		self.layout.addWidget(self.inputButton)
		self.layout.addWidget(self.reportButton)
		self.setLayout(self.layout)
		
		self.inputButton.clicked.connect(self.input)
		self.reportButton.clicked.connect(self.report)
		
	def input(self):
		self.dialog = InputDialog()
		self.dialog.show()
			
	def report(self):
		self.dialog = ReportDialog()
		self.dialog.show()
			
if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MainWindow()
	window.resize(400, 300)
	window.show()
	sys.exit(app.exec_())