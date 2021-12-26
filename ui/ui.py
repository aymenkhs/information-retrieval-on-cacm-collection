import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi

from main_interface import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)

	def search_by_query(self):
		if self.ModelChoice.currentText() == 'Le Model Boolean':
			QMessageBox.about(self, "Model Error",
			"This function isn't available for this model, please select the vectorial model in order to continue")
		else:
			pass

	def search_by_input(self):

		query = self.QueryInput.text()

		if query == "":
			QMessageBox.about(self, "the query must not be empty",
			"please write your query before clicking the search button")
			return

		if self.ModelChoice.currentText() == 'Le Model Boolean':
			# call the boolean model
			pass
		else:
			# call the vectoriel model
			pass


if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())
