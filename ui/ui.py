import sys

from PyQt5.QtWidgets import (
    QApplication, QDialog, QMainWindow, QMessageBox
)
from PyQt5.uic import loadUi

from ui.main_interface import Ui_MainWindow

from src.pkl import load_results
from src.read_file import read_requests
from src.requests import Request
from src.evaluations import launch_all_evaluations, evaluate_vectorial_function

from src.tfidf import execute_tfidf
from src.boolean_model import boolean_model
from src.vectorial_model import vectorial_model, LIST_MEASURES_FUNCTIONS


class Window(QMainWindow, Ui_MainWindow):
	def __init__(self, parent=None):
		super().__init__(parent)
		self.setupUi(self)

		self.setup_values()
		self.setup_conections()

	def setup_values(self):
		read_requests()
		self.inverse_weight_matrix, self.inverse_structure = load_results()
		self.QueryText.setPlainText('inverse_structure')

	def setup_conections(self):
		self.SearchInput.clicked.connect(self.search_by_input)
		self.SearchQueryText.clicked.connect(self.search_by_query)

	def search_by_query(self):
		if self.ModelChoice.currentText() == 'Le Model Boolean':
			QMessageBox.about(self, "Model Error",
			"This function isn't available for this model, please select the vectorial model in order to continue")
		else:
			pass

	def search_by_input(self):
		query = self.QueryInput.toPlainText()
		if query == "":
			QMessageBox.about(self, "the query must not be empty",
			"please write your query before clicking the search button")
			return

		if self.ModelChoice.currentText() == 'Le Model Boolean':
			# call the boolean model
			selected_documents = boolean_model(query)
		else:
			# call the vectoriel model
			pass


		if not self.is_selection_empty(selected_documents):
			# show the content inside the list
			self.update_list(selected_documents)

	def is_selection_empty(self, selected_documents):
		if len(selected_documents) == 0:
			QMessageBox.about(self, "no document found",
			"No document has been found with this query and parameters")
			self.Result.clear()
			return True
		return False

	def update_list(self, selected_documents):
		# clear the list
		self.Result.clear()
		# add items
		for document in selected_documents:
			self.Result.addItem(document.id)

def launch_ui():
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())

if __name__ == "__main__":
	launch_ui()
