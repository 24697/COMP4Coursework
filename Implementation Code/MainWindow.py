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
        

        
        #Menu Bar
        self.add_data = QAction("Add Data",self)
        self.edit_data = QAction("Edit Data",self)
        self.delete_data = QAction("Delete Data",self)
        self.open_database = QAction("Open Database",self)
        
        self.menu = QMenuBar()

        self.file_menu = self.menu.addMenu("Data")

        self.file_menu.addAction(self.open_database)
        self.file_menu.addAction(self.add_data)
        self.file_menu.addAction(self.edit_data)
        self.file_menu.addAction(self.delete_data)

        self.setMenuBar(self.menu)

        self.add_data.triggered.connect(self.add_data_connection)
        self.edit_data.triggered.connect(self.edit_data_connection)
        self.delete_data.triggered.connect(self.delete_data_connection)
        self.open_database.triggered.connect(self.open_database_connection)

        #Tool Bar
        self.toolbar = QToolBar()
        
        self.toolbar.addAction(self.add_data)
        self.toolbar.addAction(self.edit_data)
        self.toolbar.addAction(self.delete_data)

        self.addToolBar(self.toolbar)
        
        

    def add_data_connection(self):
        print("add data")

    def edit_data_connection(self):
        print("edit data")

    def delete_data_connection(self):
        print("delete data")

    def open_database_connection(self):
        path = QFileDialog.getOpenFileName()
        print(path)
        self.connection = SQLConnection(path)
        ok = self.connection.open_database()
        print(ok)

    def display_table(self):
        if not hasattr(self,"table_widget"):
            self.table_widget = DisplayWidget()
        self.setCentralWidget(self.tabel_widget)
        query = self.connectio.find_
        
def main():
    database_application = QApplication(sys.argv)
    manager_window = MainWindow()
    manager_window.show()
    manager_window.raise_()
    database_application.exec_()

if __name__ == "__main__":
    main()
