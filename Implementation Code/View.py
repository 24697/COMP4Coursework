from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from RadioButtonWidget import *

class DisplayWidget(QWidget):
    """The Widget that shows the main layout"""

    def __inti__(self):
        super().__init__()
        self.stacked_layout = QStackedLayout()
        self.model = None
        self.setLayout(self.stacked_layout)

    def display_table(self):
        self.table = QTableView()
        self.table_layout = QVBoxLayout()
        self.table_layout = addWidget(self.table)
        self.table_widget = QWidget()
        self.table_widget.setLayout(self.table_layout)
        self.stacked_layout.addWidget(self.table_widget)

    def show_data(self):
        if not self.model or not isinstance(self.model,"QsqlQuerModel"):
            self.model = QsqlQueryModel()
            
        self.model.setQuery(query)
        self.table.setModel(self.model)
        self.table.show()

    def show_table(self):
        pass
        
        
if __name__ == "__main__":
    test = CenteralWidget
