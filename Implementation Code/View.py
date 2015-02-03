from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from RadioButtonWidget import *
from DialogBox import *
from RecordDialogBox import *

class DisplayWidget(QWidget):
    """The Widget that shows the main layout"""

    def __inti__(self):
        super().__init__()
        self.stacked_layout = QStackedLayout()
        self.model = None
        self.setLayout(self.stacked_layout)
    #
    #table display funcions
    #

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
            self.model = QSqlQueryModel()
        self.model.setQuery(query)
        self.display_table()
        self.table.setModel(self.model)
        self.table.show()

    #
    #get user input from a search Functions
    #

    def get_user_input(self,current_table):
        if current_table == 0:
           self.line_1 = self.rider_search.line_edit_1.text()
           self.line_2 = self.rider_search.line_edit_2.text()
           self.line_3 = self.rider_search.line_edit_3.text()     
        elif current_table == 1:
            self.line_1 = self.club_search.line_edit_1.text()
            self.line_2 = self.club_search.line_edit_2.text()   
        elif current_table == 2:
            self.line_1 = self.event_type_search.line_edit_1.text()
            self.line_2 = self.event_type_search.line_edit_2.text()
            self.line_3 = self.event_type_search.line_edit_3.text()
        elif current_table == 3:
            self.line_1 = self.course_search.line_edit_1.text()
            self.line_2 = self.course_search.line_edit_2.text()
            self.line_3 = self.course_search.line_edit_3.text()
        elif current_table == 4:
            self.line_1 = self.event_reference_search.line_edit_1.text()
            self.line_2 = self.event_reference_search.line_edit_2.text()
        elif current_table == 5:
            self.line_1 = self.event_search.line_edit_1.text()
            self.line_2 = self.event_search.line_edit_2.text()
            self.line_3 = self.event_search.line_edit_3.text()
            self.line_4 = self.event_search.line_edit_4.text()
        elif current_table == 6:
            self.line_1 = self.record_search.line_edit_1.text()
            self.line_2 = self.record_search.line_edit_2.text()
            self.line_3 = self.record_search.line_edit_3.text()
            self.line_4 = self.record_search.line_edit_4.text()
            self.line_5 = self.record_search.line_edit_5.text()
            self.line_6 = self.record_search.line_edit_6.text()
        elif current_table == 7:
            self.line_1 = self.event_points_search.line_edit_1.text()
            self.line_2 = self.event_points_search.line_edit_2.text()
            self.line_3 = self.event_points_search.line_edit_3.text()
            self.line_4 = self.event_points_search.line_edit_4.text()
        elif current_table == 8:
            self.line_1 = self.club_refernce_add.line_edit_1.text()
            self.line_2 = self.club_refernce_add.line_edit_2.text()
            self.line_3 = self.club_refernce_add.line_edit_3.text()
            self.line_4 = self.club_refernce_add.line_edit_4.text()
            self.line_5 = self.club_refernce_add.line_edit_5.text()
                

    def get_user_input_add(self,current_table):
        if current_table == 0:
            self.line_add_1 = self.rider_add.line_edit_1.text()
            self.line_add_2 = self.rider_add.line_edit_2.text()
        elif current_table == 1:
            self.line_add_1 = self.club_add.line_edit_1.text()
        elif current_table == 2:
            self.line_add_1 = self.event_type_add.line_edit_1.text()
            self.line_add_2 = self.event_type_add.line_edit_2.text()
        elif current_table == 3:
            self.line_add_1 = self.course_add.line_edit_1.text()
            self.line_add_2 = self.course_add.line_edit_2.text()
        elif current_table == 4:
             self.line_add_1 = self.event_reference_add.line_edit_1.text()
        elif current_table == 5:
            self.line_add_1 = self.event_add.line_edit_1.text()
            self.line_add_2 = self.event_add.line_edit_2.text()
            self.line_add_3 = self.event_add.line_edit_3.text()
        elif current_table == 6:
            self.line_add_1 = self.record_add.line_edit_1.text()
            self.line_add_2 = self.record_add.line_edit_2.text()
            self.line_add_3 = self.record_add.line_edit_3.text()
            self.line_add_4 = self.record_add.line_edit_4.text()
            self.line_add_5 = self.record_add.line_edit_5.text()
        elif current_table == 7:
            self.line_add_1 = self.event_points_add.line_edit_1.text()
            self.line_add_2 = self.event_points_add.line_edit_2.text()
            self.line_add_3 = self.event_points_add.line_edit_3.text()
        elif current_table == 8:
            self.line_add_1 = self.club_refernce_add.line_edit_1.text()
            self.line_add_2 = self.club_refernce_add.line_edit_2.text()
            self.line_add_3 = self.club_refernce_add.line_edit_3.text()
            self.line_add_4 = self.club_refernce_add.line_edit_4.text()
        
                
    def get_ID(self):
        self.line_1 = self.delete_dialog.line_edit_1.text()
        

    #
    #add data function
    #

    def add_data_rider(self,current_table):
        if not hasattr(self,"rider_add"):
            self.options = ["Forename", "Surname"]
            self.title_main = "Add Data"
            self.title_box = "Rider Add Data"
            self.rider_add = DialogBox(self.options,self.title_main,self.title_box)
            self.rider_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1,self.line_add_2
        else:
            self.rider_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1,self.line_add_2

    def add_data_club(self,current_table):
        if not hasattr(self,"club_add"):
            self.options = ["Club Name"]
            self.title_main = "Add Data"
            self.title_box = "Club Add Data"
            self.club_add = DialogBox(self.options,self.title_main,self.title_box)
            self.club_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1
        else:
            self.club_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1
            
    def add_data_event_type(self,current_table):
        if not hasattr(self,"event_type_add"):
            self.options = ["Event Type","Event ReferenceID"]
            self.title_main = "Add Data"
            self.title_box = "Event Type Add Data"
            self.event_type_add = DialogBox(self.options,self.title_main,self.title_box)
            self.event_type_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1,self.line_add_2
        else:
            self.event_type_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1,self.line_add_2

    def add_data_course(self,current_table):
        if not hasattr(self,"course_add"):
            self.options = ["Course Code","Course Distance"]
            self.title_main = "Add Data"
            self.title_box = "Course Add Data"
            self.course_add = DialogBox(self.options,self.title_main,self.title_box)
            self.course_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1,self.line_add_2
        else:
            self.course_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1,self.line_add_2
        
    def add_data_event_reference(self,current_table):
        if not hasattr(self,"event_reference_add"):
            self.options = ["EventID"]
            self.title_main = "Add Data"
            self.title_box = "Event Reference Add Data"
            self.event_reference_add = DialogBox(self.options,self.title_main,self.title_box)
            self.event_reference_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1
        else:
            self.event_reference_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1  

    def add_data_event(self,current_table):
        if not hasattr(self,"event_add"):
            self.options = ["Date","CourseID","Laps"]
            self.title_main = "Add Data"
            self.title_box = "Event Add Data"
            self.event_add = DialogBox(self.options,self.title_main,self.title_box)
            self.event_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_1,self.line_2,self.line_3
        else:
            self.event_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1,self.line_add_2,self.line_add_3

    def add_data_record(self,current_table):
        if not hasattr(self,"record_add"):
            self.options = ["Ride Time","Age","Handicap Mod","EventID","RiderID"]
            self.title_main = "Add Data"
            self.title_box = "Record Add Data"
            self.record_add = RecordDialogBox(self.options,self.title_main,self.title_box)
            self.record_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1,self.line_add_2,self.line_add_3,self.line_add_4,self.line_add_5
        else:
            self.record_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1,self.line_add_2,self.line_add_3,self.line_add_4,self.line_add_5

    def add_data_event_points(self,current_table):
        if not hasattr(self,"event_points_add"):
            self.options = ["Event Points Type","Event Points","RecordID"]
            self.title_main = "Add Data"
            self.title_box = "Event Points Add Data"
            self.event_points_add = DialogBox(self.options,self.title_main,self.title_box)
            self.event_points_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1,self.line_add_2,self.line_add_3
        else:
            self.event_points_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1,self.line_add_2,self.line_add_3

    def add_data_club_reference(self,current_table):
        if not hasattr(self,"club_reference_add"):
            self.options = ["Date Joined","Date Left","RiderID","ClubID"]
            self.title_main = "Add Data"
            self.title_box = "Club Refernce Add Data"
            self.club_refernce_add = DialogBox(self.options,self.title_main,self.title_box)
            self.club_refernce_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1,self.line_add_2,self.line_add_3,self.line_add_4
        else:
            self.club_refernce_add.exec_()
            self.get_user_input_add(current_table)
            return self.line_add_1,self.line_add_2,self.line_add_3,self.line_add_4

            
    #
    #search data functions
    #        

    def search_rider(self,current_table):
        if not hasattr(self,"rider_search"):
            self.options = ["Rider ID", "Forename", "Surname"]
            self.title_main = "Search"
            self.title_box = "Rider Search"
            self.rider_search = DialogBox(self.options,self.title_main,self.title_box)
            self.rider_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3
        else:
            self.rider_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3
        
    def search_club(self,current_table):
        if not hasattr(self,"club_search"):
            self.options = ["ClubID", "Club Name"]
            self.title_main = "Search"
            self.title_box = "Club Search"
            self.club_search = DialogBox(self.options,self.title_main,self.title_box)
            self.club_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2
        else:
            self.club_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2

    def search_event_type(self,current_table):
        if not hasattr(self,"event_type_search"):
            self.options = ["Event TypeID", "Event Type","Event ReferenceID"]
            self.title_main = "Search"
            self.title_box = "Event Type Search"
            self.event_type_search = DialogBox(self.options,self.title_main,self.title_box)
            self.event_type_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3
        else:
            self.event_type_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3

    def search_course(self,current_table):
        if not hasattr(self,"course_search"):
            self.options = ["CourseID", "Course Code","Course Distance"]
            self.title_main = "Search"
            self.title_box = "Course Search"
            self.course_search = DialogBox(self.options,self.title_main,self.title_box)
            self.course_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3
        else:
            self.course_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3


    def search_event_reference(self,current_table):
        if not hasattr(self,"event_reference_search"):
            self.options = ["Event ReferncerID", "EventID"]
            self.title_main = "Search"
            self.title_box = "Event Reference Search"
            self.event_reference_search = DialogBox(self.options,self.title_main,self.title_box)
            self.event_reference_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2
        else:
            self.event_reference_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2


    def search_event(self,current_table):
        if not hasattr(self,"event_search"):
            self.options = ["EventID", "Date","CourseID","Laps"]
            self.title_main = "Search"
            self.title_box = "Event Search"
            self.event_search = DialogBox(self.options,self.title_main,self.title_box)
            self.event_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3,line_4
        else:
            self.event_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3,line_4

    def search_record(self,current_table):
        if not hasattr(self,"record_search"):
            self.options = ["RecordID", "Ride Time","Age","Handicap Mod","EventID","RiderID"]
            self.title_main = "Search"
            self.title_box = "Record Search"
            self.record_search = DialogBox(self.options,self.title_main,self.title_box)
            self.record_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3,line_4,line_5,line_6
        else:
            self.record_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3,line_4,line_5,line_6
        
    def search_event_points(self,current_table):
        if not hasattr(self,"event_points_search"):
            self.options = ["Event PointsID", "Event Points Type","RecordID"]
            self.title_main = "Search"
            self.title_box = "Event Points Search"
            self.event_search = DialogBox(self.options,self.title_main,self.title_box)
            self.event_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3
        else:
            self.event_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3
        
    def search_club_reference(self,current_table):
        if not hasattr(self,"club_reference_search"):
            self.options = ["Club RefernceID", "Date Joined","Date Left","RiderID","ClubID"]
            self.title_main = "Search"
            self.title_box = "Club Refernce Search"
            self.club_refernce_search = DialogBox(self.options,self.title_main,self.title_box)
            self.club_refernce_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3,line_4,line_5
        else:
            self.club_refernce_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3,line_4,line_5

    def delete_data(self,current_table):
        if not hasattr(self,"delete_dialog"):
            self.options = ["ID of option"]
            self.title_main = "Delete"
            self.title_box ="ID of item to be deleted"
            self.delete_dialog = DialogBox(self.options,self.title_main,self.title_box)
            self.delete_dialog.exec_()
            self.get_ID()
            return self.line_1
        else:
            self.delete_dialog.exec_()
            self.get_ID()
            return self.line_1
            
