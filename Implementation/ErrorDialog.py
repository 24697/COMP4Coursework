from PyQt4.QtCore import *
from PyQt4.QtGui import *

class error_box(QDialog):
    def __init__(self,error_mes,title_main,title_box):
        super().__init__()
        self.setWindowTitle(title_main)
        self.setModal(2)
        
        
        #create the box and set the title
        self.group_box = QGroupBox()
        self.group_box.setTitle(title_box)
        
        #add a layout
        self.group_box_layout = QVBoxLayout()
        self.group_box.setLayout(self.group_box_layout)

        #create the layout for the error message
        self.layout = QVBoxLayout()

        #add the gourp box to the dialog layout
        self.layout.addWidget(self.group_box)
        
        #sets the layout of the dialog box
        self.setLayout(self.layout)

        #create the error message
        self.error = QString()
        self.error.insert(error_mes)

        #add error message to the QVBoxLayout
        self.layout.addWidget(self.error)

        #create the push button and add it to the dialog box
        self.ok_button = QPushButton()
        self.ok_button.setText("OK")
        self.layout.addWidget(self.ok_button)
