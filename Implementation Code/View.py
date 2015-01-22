from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtSql import *

from RadioButtonWidget import *
from DialogBox import *

class DisplayWidget(QWidget):
    """The Widget that shows the main layout"""

    def __inti__(self):
        super().__init__()
        self.stacked_layout = QStackedLayout()
        self.model = None
        self.setLayout(self.stacked_layout)

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

    def show_search(self,search_query):
        pass

    #
    #get user input from a search
    #

    def get_user_input(self,current_table):
        if current_table == 0:
            try:
               self.line_1 = self.rider_search.line_edit_1.text()
               self.line_2 = self.rider_search.line_edit_2.text()
               self.line_3 = self.rider_search.line_edit_3.text()
            except AttributeError:
                self.line_1 = self.rider_add.line_edit_1.text()
                self.line_2 = self.rider_add.line_edit_2.text()

               
        elif current_table == 1:
            try:
                self.line_1 = self.club_search.line_edit_1.text()
                self.line_2 = self.club_search.line_edit_2.text()
            except AttributeError:
                self.line_1 = self.club_add.line_edit_1.text()
            
        elif current_table == 2:
            try:
                self.line_1 = self.event_type_search.line_edit_1.text()
                self.line_2 = self.event_type_search.line_edit_2.text()
                self.line_3 = self.type_search.line_edit_3.text()
            except AttributeError:
                self.line_1 = self.event_type_add.line_edit_1.text()
                self.line_2 = self.event_type_add.line_edit_2.text()
            
        elif current_table == 3:
            try:
                self.line_1 = self.course_search.line_edit_1.text()
                self.line_2 = self.course_search.line_edit_2.text()
                self.line_3 = self.course_search.line_edit_3.text()
            except AttributeError:
                self.line_1 = self.course_add.line_edit_1.text()
                self.line_2 = self.course_add.line_edit_2.text()
            
        elif current_table == 4:
            try:
                self.line_1 = self.event_reference_search.line_edit_1.text()
                self.line_2 = self.event_reference_search.line_edit_2.text()
            except AttributeError:
                self.line_1 = self.event_reference_add.line_edit_1.text()

        elif current_table == 5:
            try:
                self.line_1 = self.event_search.line_edit_1.text()
                self.line_2 = self.event_search.line_edit_2.text()
                self.line_3 = self.event_search.line_edit_3.text()
                self.line_4 = self.event_search.line_edit_4.text()
            except AttributeError:
                self.line_1 = self.event_add.line_edit_1.text()
                self.line_2 = self.event_add.line_edit_2.text()
                self.line_3 = self.event_add.line_edit_3.text()

        elif current_table == 6:
            try:
                self.line_1 = self.record_search.line_edit_1.text()
                self.line_2 = self.record_search.line_edit_2.text()
                self.line_3 = self.record_search.line_edit_3.text()
                self.line_4 = self.record_search.line_edit_4.text()
                self.line_5 = self.record_search.line_edit_5.text()
                self.line_6 = self.record_search.line_edit_6.text()
            except AttributeError:
                self.line_1 = self.record_add.line_edit_1.text()
                self.line_2 = self.record_add.line_edit_2.text()
                self.line_3 = self.record_add.line_edit_3.text()
                self.line_4 = self.record_add.line_edit_4.text()
                self.line_5 = self.record_add.line_edit_5.text()
        
        elif current_table == 7:
            try:
                self.line_1 = self.event_points_search.line_edit_1.text()
                self.line_2 = self.event_points_search.line_edit_2.text()
                self.line_3 = self.event_points_search.line_edit_3.text()
                self.line_4 = self.event_points_search.line_edit_4.text()
            except AttributeError:
                self.line_1 = self.event_points_add.line_edit_1.text()
                self.line_2 = self.event_points_add.line_edit_2.text()
                self.line_3 = self.event_points_add.line_edit_3.text()

        elif current_table == 8:
            try:   
                self.line_1 = self.club_reference_search.line_edit_1.text()
                self.line_2 = self.club_reference_search.line_edit_2.text()
                self.line_3 = self.club_reference_search.line_edit_3.text()
                self.line_4 = self.club_reference_search.line_edit_4.text()
                self.line_5 = self.club_reference_search.line_edit_5.text()
            except AttributeError:
                self.line_1 = self.club_reference_search.line_edit_1.text()
                self.line_2 = self.club_reference_search.line_edit_2.text()
                self.line_3 = self.club_reference_search.line_edit_3.text()
                self.line_4 = self.club_reference_search.line_edit_4.text()

    #
    #Add Data Function
    #

    def add_data_rider(self,current_table):
        if not hasattr(self,"rider_add"):
            self.options = ["Forename", "Surname"]
            self.title_main = "Add Data"
            self.title_box = "Rider Add Data"
            self.rider_add = DialogBox(self.options,self.title_main,self.title_box)
            self.rider_add.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2
        else:
            self.rider_add.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2

    def add_data_club(self,current_table):
        if not hasattr(self,"club_add"):
            self.options = ["Club Name"]
            self.title_main = "Add Data"
            self.title_box = "Club Add Data"
            self.club_add = DialogBox(self.options,self.title_main,self.title_box)
            self.club_add.exec_()
            self.get_user_input(current_table)
            return self.line_1
        else:
            self.club_add.exec_()
            self.get_user_input(current_table)
            return self.line_1
            

    def add_data_event_type(self,current_table):
        if not hasattr(self,"event_type_add"):
            self.options = ["Event Type","Event ReferenceID"]
            self.title_main = "Add Data"
            self.title_box = "Event Type Add Data"
            self.event_type_add = DialogBox(self.options,self.title_main,self.title_box)
            self.event_type_add.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2
        else:
            self.event_type_add.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2

    def add_data_course(self,current_table):
        if not hasattr(self,"course_add"):
            self.options = ["Course Code","Course Distance"]
            self.title_main = "Add Data"
            self.title_box = "Course Add Data"
            self.course_add = DialogBox(self.options,self.title_main,self.title_box)
            self.event_type_add.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2
        else:
            self.event_type_add.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2
        
    def add_data_event_reference(self,current_table):
        if not hasattr(self,"event_reference_add"):
            self.options = ["EventID"]
            self.title_main = "Add Data"
            self.title_box = "Event Reference Add Data"
            self.event_reference_add = DialogBox(self.options,self.title_main,self.title_box)
            self.club_add.exec_()
            self.get_user_input(current_table)
            return self.line_1
        else:
            self.club_add.exec_()
            self.get_user_input(current_table)
            return self.line_1
##################################################
#                      FIX                       #
##################################################
        

    def add_data_event(self,current_table):
        if not hasattr(self,"event_add"):
            self.options = ["Date","CourseID","Laps"]
            self.title_main = "Add Data"
            self.title_box = "Event Add Data"
            self.event_add = DialogBox(self.options,self.title_main,self.title_box)
        else:
            self.event_add.open()

    def add_data_record(self,current_table):
        if not hasattr(self,"record_add"):
            self.options = ["Ride Time","Age","Handicap Mod","EventID","RiderID"]
            self.title_main = "Add Data"
            self.title_box = "Record Add Data"
            self.record_add = DialogBox(self.options,self.title_main,self.title_box)
        else:
            self.record_add.open()

    def add_data_event_points(self,current_table):
        if not hasattr(self,"event_points_add"):
            self.options = ["Event Points Type","RecordID"]
            self.title_main = "Add Data"
            self.title_box = "Event Points Add Data"
            self.event_add = DialogBox(self.options,self.title_main,self.title_box)
        else:
            self.event_points_add.open()

    def add_data_club_reference(self,current_table):
        if not hasattr(self,"club_reference_add"):
            self.options = ["Date Joined","Date Left","RiderID","ClubID"]
            self.title_main = "Add Data"
            self.title_box = "Club Refernce Add Data"
            self.club_refernce_add = DialogBox(self.options,self.title_main,self.title_box)
        else:
            self.club_refernce_add.open()
##################################################
#                      END FIX                   #
##################################################
            
    #
    #Search Data functions
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
        
        def search_club(self,current_talbe):
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
                return self.line_1,self.line_2

    def search_event_type(self,current_table):
        if not hasattr(self,"event_type_search"):
            self.options = ["Event TypeID", "Event Type","Event ReferenceID"]
            self.title_main = "Search"
            self.title_box = "Event Type Search"
            self.event_type_search = DialogBox(self.options,self.title_main,self.title_box)
            self.rider_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3
        else:
            self.club_search.exec_()
            return self.line_1,self.line_2,self.line_3

    def search_course(self,current_table):
        if not hasattr(self,"course_search"):
            self.options = ["CourseID", "Course Code","Course Distance"]
            self.title_main = "Search"
            self.title_box = "Course Search"
            self.course_search = DialogBox(self.options,self.title_main,self.title_box)
            self.rider_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3
        else:
            self.club_search.exec_()
            return self.line_1,self.line_2,self.line_3


    def search_event_reference(self,current_table):
        if not hasattr(self,"event_reference_search"):
            self.options = ["Event ReferncerID", "EventID"]
            self.title_main = "Search"
            self.title_box = "Event Reference Search"
            self.event_reference_search = DialogBox(self.options,self.title_main,self.title_box)
            self.rider_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2
        else:
            self.club_search.exec_()
            return self.line_1,self.line_2


    def search_event(self,current_table):
        if not hasattr(self,"event_search"):
            self.options = ["EventID", "Date","CourseID","Laps"]
            self.title_main = "Search"
            self.title_box = "Event Search"
            self.event_search = DialogBox(self.options,self.title_main,self.title_box)
            self.rider_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3,line_4
        else:
            self.club_search.exec_()
            return self.line_1,self.line_2,self.line_3,line_4

    def search_record(self,current_table):
        if not hasattr(self,"record_search"):
            self.options = ["RecordID", "Ride Time","Age","Handicap Mod","EventID","RiderID"]
            self.title_main = "Search"
            self.title_box = "Record Search"
            self.record_search = DialogBox(self.options,self.title_main,self.title_box)
            self.rider_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3,line_4,line_5,line_6
        else:
            self.club_search.exec_()
            return self.line_1,self.line_2,self.line_3,line_4,line_5,line_6
        
    def search_event_points(self,current_table):
        if not hasattr(self,"event_points_search"):
            self.options = ["Event PointsID", "Event Points Type","RecordID"]
            self.title_main = "Search"
            self.title_box = "Event Points Search"
            self.event_search = DialogBox(self.options,self.title_main,self.title_box)
            self.rider_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3
        else:
            self.club_search.exec_()
            return self.line_1,self.line_2,self.line_3
        
    def search_club_reference(self,current_table):
        if not hasattr(self,"club_reference_search"):
            self.options = ["Club RefernceID", "Date Joined","Date Left","RiderID","ClubID"]
            self.title_main = "Search"
            self.title_box = "Club Refernce Search"
            self.club_refernce_search = DialogBox(self.options,self.title_main,self.title_box)
            self.rider_search.exec_()
            self.get_user_input(current_table)
            return self.line_1,self.line_2,self.line_3,line_4,line_5
        else:
            self.club_search.exec_()
            return self.line_1,self.line_2,self.line_3,line_4,line_5
