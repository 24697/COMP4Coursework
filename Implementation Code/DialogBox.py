from PyQt.QtGui import *

class DialogBox(QDialog,options,title_main,title_box):
    def __init__(self):
        super.__init__()

        self.setWindowTitle(title_main)

        #create the box and set the title
        self.group_box = QGroupBox()
        self.group_box.setTitle(title_box)

        #add a layout
        self.group_box.setLayout = QVBoxLayout()


        #add widget to the QVBoxLayout
        self.line_edit_name = "line_edit_1"
        for count in range(len(options)):
            
