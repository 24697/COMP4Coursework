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

    def get_search_data(self,current_table):
        if current_table == 0:
            self.riderID = self.search.line_edit_1.text()
            self.forename = self.search.line_edit_2.text()
            self.surname = self.search.line_edit_3.text()
            print(self.riderID)
            print(self.forename)
            print(self.surname)


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
            print("Search function for Rider table")
            self.options = ["Rider ID", "Forename", "Surname"]
            self.title_main = "Search"
            self.title_box = "Rider Search"
            self.search = DialogBox(self.options,self.title_main,self.title_box)
            self.search.show()
            #self.done = False
            #while self.done == False:
            #    if self.search.ok_button.clicked:
            #        self.done == True
            #        self.search.ok_button.clicked.connect(self.get_search_data(current_table))
            #        self.search.hide()
            #    else:
            #        pass
            self.search.ok_button.clicked.connect(self.get_search_data(current_table))
        elif current_table == 1:
            print("Search function for club table")
            
