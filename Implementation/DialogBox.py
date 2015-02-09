from PyQt4.QtGui import *

class DialogBox(QDialog):
    def __init__(self,options,title_main,title_box):
        super().__init__()
        self.setWindowTitle(title_main)
        self.setModal(2)

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
        self.layout.addWidget(self.ok_button)

        self.ok_button.clicked.connect(self.close)
            
        

    
                  
       
