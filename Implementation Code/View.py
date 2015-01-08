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
        self.table_layout.addWidget(self.table)
        self.table_widget = QWidget()
        self.table_widget.setLayout(self.table_layout)
        if not hasattr(self,"stacked_layout"):
            self.stacked_layout = QStackedLayout()
            self.setLayout(self.stacked_layout)
        self.stacked_layout.addWidget(self.table_widget)

    def show_data(self,query):
        if not hasattr(self,"model"):
            print("Pass2-1")
            self.model = QSqlQueryModel()
        print("Pass2-2")
        self.model.setQuery(query)
        print("Pass2-3")
        self.display_table()
        self.table.setModel(self.model)
        print("Pass2-4")
        self.table.show()
        print("Pass2-5")


    def add_data_rider(self):
        pass

    def add_data_club(self):
        pass

    def add_data_event_type(self):
        pass

    def add_data_course(self):
        pass

    def add_data_event_reference(self):
        pass

    def add_data_event(self):
        pass

    def add_data_record(self):
        pass

    def add_data_event_points(self):
        pass

    def add_data_club_refernece(self):
        pass

    def search(current_table):
        if current_table == 0:
            print("Search function for Rider table")
        elif current_table == 1:
            print("Search function for club table")
            
