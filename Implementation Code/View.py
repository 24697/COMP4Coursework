from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from RadioButtonWidget import *
from DialogBox import *

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
            self.model = QSqlQueryModel()
        self.model.setQuery(query)
        self.display_table()
        self.table.setModel(self.model)
        self.table.show()

    def get_user_input(self,current_table):
        if current_table == 0:
            riderID = self.rider_search.line_1
            forename = self.rider_search.line_2
            surname = self.rider_search.line_3
            return riderID,forename,surname

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

    def search(self,current_table):
        if current_table == 0:
            self.options = ["Rider ID", "Forename", "Surname"]
            self.title_main = "Search"
            if not hasattr(self,"rider_search"):
                print("Search function for Rider table")
                self.options = ["Rider ID", "Forename", "Surname"]
                self.title_main = "Search"
                self.title_box = "Rider Search"
                self.rider_search = DialogBox(self.options,self.title_main,self.title_box)
            else:
                self.rider_search.open()
            

                
