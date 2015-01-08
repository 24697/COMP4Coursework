import sys

from PyQt4.QtCore import *
from PyQt4.QtGui import *

from RadioButtonWidget import *

class MainWindow(QMainWindow):
    """Creates the main window"""

    def __init__(self):
        super().__init__()
        self.setWindowTitle = ("Team Cambridge Database Manager")
        #self.test_radio_button_layout()

        
        

    def test_radio_button_layout(self):
        self.radio_button_tester = RadioButtonWidget("Radio Button Test",  "Please select an option",("Exit","Begin"))
        self.instantitate_button = QPushButton("Test")

        self.inital_Layout = QVBoxLayout()
        self.inital_Layout.addWidget(self.radio_button_tester)
        self.inital_Layout.addWidget(self.instantitate_button)
        
        self.select_option_widget = QWidget()
        self.select_option_widget.setLayout(self.inital_Layout)

        self.setCentralWidget(self.select_option_widget)

def main():
    database_application = QApplication(sys.argv)
    manager_window = MainWindow()
    manager_window.show()
    manager_window.raise_()
    database_application.exec_()

if __name__ == "__main__":
    main()
