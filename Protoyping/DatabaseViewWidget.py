from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4.QtSql import *

class DatabaseViewWidget(QWidget):
    """Database view widget"""

    def __init__(self):
        super().__init__()
        self.tabed_layout = QStackedLayout()
        self.modle = None
        self.setLayout(self.stacked_layout)
        

    def display_results_layout(self):
        self.results_table
