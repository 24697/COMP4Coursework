import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from RadioButtonWidget import *
from Connection import *
from View import *

class MainWindow(QMainWindow):
    """Creates the main window"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Team Cambridge Database Manager")

        self.current_table = 0
        

        
        #Menu Bar
        self.add_data = QAction("Add Data",self)
        self.edit_data = QAction("Edit Data",self)
        self.delete_data = QAction("Delete Data",self)
        self.search = QAction("Search",self)

        self.rider = QAction("Rider",self)
        self.club = QAction("Club",self)
        self.event_type = QAction("Event Type",self)
        self.course = QAction("Course",self)
        self.event_reference = QAction("Event Reference",self)
        self.event = QAction("Event",self)
        self.record = QAction("Record",self)
        self.event_points = QAction("Event Points",self)
        self.club_reference = QAction("Club Reference",self)
        
        self.menu = QMenuBar()

        self.file_menu = self.menu.addMenu("Data")
        self.table_menu = self.menu.addMenu("Tables")

        
        self.file_menu.addAction(self.add_data)
        self.file_menu.addAction(self.edit_data)
        self.file_menu.addAction(self.delete_data)

        self.table_menu.addAction(self.rider)
        self.table_menu.addAction(self.club)
        self.table_menu.addAction(self.event_type)
        self.table_menu.addAction(self.course)
        self.table_menu.addAction(self.event_reference)
        self.table_menu.addAction(self.event)
        self.table_menu.addAction(self.record)
        self.table_menu.addAction(self.event_points)
        self.table_menu.addAction(self.club_reference)

        self.setMenuBar(self.menu)

        self.add_data.triggered.connect(self.add_data_connection)
        self.edit_data.triggered.connect(self.edit_data_connection)
        self.delete_data.triggered.connect(self.delete_data_connection)
        self.search.triggered.connect(self.search_connection)

        self.rider.triggered.connect(self.rider_connection)
        self.club.triggered.connect(self.club_connection)
        self.event_type.triggered.connect(self.event_type_connection)
        self.course.triggered.connect(self.course_connection)
        self.event_reference.triggered.connect(self.event_reference_connection)
        self.event.triggered.connect(self.event_connection)
        self.record.triggered.connect(self.record_connection)
        self.event_points.triggered.connect(self.event_points_connection)
        self.club_reference.triggered.connect(self.club_reference_connection)
        

        #Tool Bar
        self.toolbar = QToolBar()
        
        self.toolbar.addAction(self.add_data)
        self.toolbar.addAction(self.edit_data)
        self.toolbar.addAction(self.delete_data)
        self.toolbar.addAction(self.search)

        self.addToolBar(self.toolbar)

    def rider_connection(self):
        print("Change current table to Rider")
        self.current_table = 0
        self.display_table()
        
    def club_connection(self):
        print("Change current table to club")
        self.current_table = 1
        self.display_table()
        
    def event_type_connection(self):
        print("Change current table to event type")
        self.current_table = 2
        self.display_table()
        
    def course_connection(self):
        print("Change current table to course")
        self.current_table = 3
        self.display_table()
        
    def event_reference_connection(self):
        print("Change current table to event refernece")
        self.current_table = 4
        self.display_table()
        
    def event_connection(self):
        print("Change current table to event")
        self.current_table = 5
        self.display_table()
        
    def record_connection(self):
        print("Change current table to record")
        self.current_table = 6
        self.display_table()
        
    def event_points_connection(self):
        print("Change current table to event points")
        self.current_table = 7
        self.display_table()
        
    def club_reference_connection(self):
        print("Change current table to club refernece")
        self.current_table = 8
        self.display_table()
        

    def add_data_connection(self):
        if self.current_table == 0:
            self.display.add_data_rider()
            
        elif self.current_table == 1:
            self.display.add_data_club()
            
        elif self.current_table == 2:
            self.display.add_data_event_type()
            
        elif self.current_table == 3:
            self.display.add_data_course()
            
        elif self.current_table == 4:
            self.display.add_data_event_reference()
            
        elif self.current_table == 5:
            self.display.add_data_event()
            
        elif self.current_table == 6:
            self.display.add_data_record()
            
        elif self.current_table == 7:
            self.display.add_data_event_points()
            
        elif self.current_table == 8:
            self.display.add_data_club_reference()

    def edit_data_connection(self):
        print("edit data")

    def delete_data_connection(self):
        print("delete data")

    def search_connection(self):
        self.display.search(self.current_table)

    def open_database_connection(self):
        path = QFileDialog.getOpenFileName()
        print(path)
        self.connection = SQLConnection(path)
        ok = self.connection.open_database()
        print(ok)

    def display_table(self):
        if not hasattr(self,"display"):
            self.display = DisplayWidget()
        self.setCentralWidget(self.display)
        self.model_query = self.connection.get_all(self.current_table)
        self.display.show_data(self.model_query)
        
def main():
    database_application = QApplication(sys.argv)
    manager_window = MainWindow()
    manager_window.show()
    manager_window.raise_()
    manager_window.open_database_connection()
    manager_window.display_table()
    database_application.exec_()
    

if __name__ == "__main__":
    main()
