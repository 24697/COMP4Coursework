from PyQt4.QtGui import *
from HandicapCal import *

class RecordDialogBox(QDialog):
    def __init__(self,options,title_main,title_box,path):
        super().__init__()
        self.setWindowTitle(title_main)
        self.setModal(2)
        self.path = path

        #create the box and set the title
        self.group_box = QGroupBox()
        self.group_box.setTitle(title_box)

        #add a layout
        self.group_box_layout = QVBoxLayout()
        self.group_box.setLayout(self.group_box_layout)

        #create the layout for the dialog box
        self.layout = QVBoxLayout()
        
        #add the gourp box to the dialog layout
        self.layout.addWidget(self.group_box)
        
        #sets the layout of the dialog box
        self.setLayout(self.layout)

        #add line edit widget to the QVBoxLayout
        if len(options) > 0:
            self.line_edit_1 = QLineEdit()
            self.line_edit_1.setText(options[0])
            self.group_box_layout.addWidget(self.line_edit_1)
            
        if len(options) > 1:
            self.line_edit_2 = QLineEdit()
            self.line_edit_2.setText(options[1])
            self.group_box_layout.addWidget(self.line_edit_2)
            
        if len(options) > 2:
            self.line_edit_3 = QLineEdit()
            self.line_edit_3.setText(options[2])
            self.group_box_layout.addWidget(self.line_edit_3)
            
        if len(options) > 3:
            self.line_edit_4 = QLineEdit()
            self.line_edit_4.setText(options[3])
            self.group_box_layout.addWidget(self.line_edit_4)
            
        if len(options) > 4:
            self.line_edit_5 = QLineEdit()
            self.line_edit_5.setText(options[4])
            self.group_box_layout.addWidget(self.line_edit_5)
        if len(options) > 5:

            self.line_edit_6 = QLineEdit()
            self.line_edit_6.setText(options[5])
            self.group_box_layout.addWidget(self.line_edit_6)

        #create the push button and add it to the dialog box
        self.ok_button = QPushButton()
        self.ok_button.setText("OK")

        self.handicap_button = QPushButton()
        self.handicap_button.setText("Cal Handicap")

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.ok_button)
        self.button_layout.addWidget(self.handicap_button)
        
        self.layout.addLayout(self.button_layout)
        
        self.handicap_button.clicked.connect(self.cal_connect)
        self.ok_button.clicked.connect(self.close)
        
    def cal_connect(self):
        self.eventID = self.line_edit_4.text()
        self.riderID = self.line_edit_5.text()
        cal_handicap(self.eventID,self.riderID,self.path)
