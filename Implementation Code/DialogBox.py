from PyQt4.QtGui import *

class DialogBox(QDialog):
    def __init__(self,options,title_main,title_box):
        super().__init__()
        self.setWindowTitle(title_main)

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
            #self.line_edit_1.text()  gets the text form a line edit
            
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
    def run_dialog(self):
        self.open()
        

    def end(self):
        self.done()
        self.hide()
        
    def return_data(self):
        try:
            self.line_1 = self.line_edit_1.text()
        except:
            self.done()
        
        try:
            self.line_2 = self.line_edit_2.text()
        except:
            self.done()
            return self.line_1
            

        try:
            self.line_3 = self.line_edit_3.text()
        except:
            self.done()
            return self.line_1,self.line2
            

        try:
            self.line_4 = self.line_edit_4.text()
        except:
            self.done()
            return self.line_1,self.line_2,self.line_3
            

        try:
            self.line_5 = self.line_edit_5.text()
        except:
            self.done()
            return self.line_1,self.line_2,self.line_3,self.line_4
            
        try:
            self.line_6 = self.line_edit_6.text()
        except:
            self.done()
            return self.line_1,self.line_2,self.line_3,self.line_4,self.line_5


        self.done()
        return self.line_1,self.line_2,self.line_3,self.line_4,self.line_5,self.line_6
                  
       
