from PyQt.QtGui import *

class DialogBox(QDialog,options,title_main,title_box):
    def __init__(self):
        super.__init__()

        self.setWindowTitle(title_main)

        #create the box and set the title
        self.group_box = QGroupBox()
        self.group_box.setTitle(title_box)

        #add a layout
        self.group_box_layout.setLayout = QVBoxLayout()

        #add line edit widget to the QVBoxLayout
        if len(options) > 0:
            self.line_edit_1 = QLineEdit()
            self.line_edit_1.setText(options[0])
            self.group_box_layout.addWdiget(self.line_edit_1)
            
        if len(options) > 1:
            self.line_edit_2 = QLineEdit()
            self.line_edit_2.setText(options[1])
            self.group_box_layout.addWdiget(self.line_edit_2)
            
        if len(options) > 2:
            self.line_edit_3 = QLineEdit()
            self.line_edit_3.setText(options[2])
            self.group_box_layout.addWdiget(self.line_edit_3)
            
        if len(options) > 3:
            self.line_edit_4 = QLineEdit()
            self.line_edit_4.setText(options[3])
            self.group_box_layout.addWdiget(self.line_edit_4)
            
        if len(options) > 4:
            self.line_edit_5 = QLineEdit()
            self.line_edit_5.setText(options[4])
            self.group_box_layout.addWdiget(self.line_edit_5)
        if len(options) > 5:

            self.line_edit_6 = QLineEdit()
            self.line_edit_6.setText(options[5])
            self.group_box_layout.addWdiget(self.line_edit_6)
            
