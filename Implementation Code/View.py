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

    def get_user_input(self,current_table):
        if current_table == 0:
            self.riderID = self.rider_search.line_edit_1.text()
            self.forename = self.rider_search.line_edit_2.text()
            self.surname = self.rider_search.line_edit_3.text()
            print(riderID)
            print(forename)
            print(surname)
            return riderID,forename,surname

    def add_data_rider(self):
        if not hasattr(self,"rider_add"):
            self.options = ["Forename", "Surname"]
            self.title_main = "Add Data"
            self.title_box = "Rider Add Data"
            self.rider_add = DialogBox(self.options,self.title_main,self.title_box)
        else:
            self.rider_add.open()

    def add_data_club(self):
        if not hasattr(self,"club_add"):
            self.options = ["Club Name"]
            self.title_main = "Add Data"
            self.title_box = "Club Add Data"
            self.club_add = DialogBox(self.options,self.title_main,self.title_box)
        else:
            self.club_add.open()

    def add_data_event_type(self):
        if not hasattr(self,"event_type_add"):
            self.options = ["Event Type","Event ReferenceID"]
            self.title_main = "Add Data"
            self.title_box = "Event Type Add Data"
            self.event_type_add = DialogBox(self.options,self.title_main,self.title_box)
        else:
            self.event_type_add.open()

    def add_data_course(self):
        if not hasattr(self,"course_add"):
            self.options = ["Course Code","Course Distance"]
            self.title_main = "Add Data"
            self.title_box = "Course Add Data"
            self.course_add = DialogBox(self.options,self.title_main,self.title_box)
        else:
            self.course_add.open()

    def add_data_event_reference(self):
        if not hasattr(self,"event_reference_add"):
            self.options = ["EventID"]
            self.title_main = "Add Data"
            self.title_box = "Event Reference Add Data"
            self.event_reference_add = DialogBox(self.options,self.title_main,self.title_box)
        else:
            self.event_refernece_add.open()

    def add_data_event(self):
        if not hasattr(self,"event_add"):
            self.options = ["Date","CourseID","Laps"]
            self.title_main = "Add Data"
            self.title_box = "Event Add Data"
            self.event_add = DialogBox(self.options,self.title_main,self.title_box)
        else:
            self.event_add.open()

    def add_data_record(self):
        if not hasattr(self,"record_add"):
            self.options = ["Ride Time","Age","Handicap Mod","EventID","RiderID"]
            self.title_main = "Add Data"
            self.title_box = "Record Add Data"
            self.record_add = DialogBox(self.options,self.title_main,self.title_box)
        else:
            self.record_add.open()

    def add_data_event_points(self):
        if not hasattr(self,"event_points_add"):
            self.options = ["Event Points Type","RecordID"]
            self.title_main = "Add Data"
            self.title_box = "Event Points Add Data"
            self.event_add = DialogBox(self.options,self.title_main,self.title_box)
        else:
            self.event_points_add.open()

    def add_data_club_reference(self):
        if not hasattr(self,"club_reference_add"):
            self.options = ["Date Joined","Date Left","RiderID","ClubID"]
            self.title_main = "Add Data"
            self.title_box = "Club Refernce Add Data"
            self.club_refernce_add = DialogBox(self.options,self.title_main,self.title_box)
        else:
            self.club_refernce_add.open()

    def search(self,current_table):
        if current_table == 0:
            if not hasattr(self,"rider_search"):
                self.options = ["Rider ID", "Forename", "Surname"]
                self.title_main = "Search"
                self.title_box = "Rider Search"
                self.rider_search = DialogBox(self.options,self.title_main,self.title_box)
                self.rider_search.run_dialog()
                self.rider_search.clicked.connect(self.get_user_input)
            else:
                self.rider_search.run_dialog()
                self.rider_search.clicked.connect(self.get_user_input)
            
        elif current_table == 1:
            if not hasattr(self,"club_search"):
                self.options = ["ClubID", "Club Name"]
                self.title_main = "Search"
                self.title_box = "Club Search"
                self.club_search = DialogBox(self.options,self.title_main,self.title_box)
            else:
                self.club_search.open()

        elif current_table == 2:
            if not hasattr(self,"event_type_search"):
                self.options = ["Event TypeID", "Event Type","Event ReferenceID"]
                self.title_main = "Search"
                self.title_box = "Event Type Search"
                self.event_type_search = DialogBox(self.options,self.title_main,self.title_box)
            else:
                self.event_type_search.open()

        elif current_table == 3:
            if not hasattr(self,"course_search"):
                self.options = ["CourseID", "Course Code","Course Distance"]
                self.title_main = "Search"
                self.title_box = "Course Search"
                self.course_search = DialogBox(self.options,self.title_main,self.title_box)
            else:
                self.course_search.open()

        elif current_table == 4:
            if not hasattr(self,"event_reference_search"):
                self.options = ["Event ReferncerID", "EventID"]
                self.title_main = "Search"
                self.title_box = "Event Reference Search"
                self.event_reference_search = DialogBox(self.options,self.title_main,self.title_box)
            else:
                self.event_refernece_search.open()

        elif current_table == 5:
            if not hasattr(self,"event_search"):
                self.options = ["EventID", "Date","CourseID","Laps"]
                self.title_main = "Search"
                self.title_box = "Event Search"
                self.event_search = DialogBox(self.options,self.title_main,self.title_box)
            else:
                self.event_search.open()

        elif current_table == 6:
            if not hasattr(self,"record_search"):
                self.options = ["RecordID", "Ride Time","Age","Handicap Mod","EventID","RiderID"]
                self.title_main = "Search"
                self.title_box = "Record Search"
                self.record_search = DialogBox(self.options,self.title_main,self.title_box)
            else:
                self.record_search.open()

        elif current_table == 7:
            if not hasattr(self,"event_points_search"):
                self.options = ["Event PointsID", "Event Points Type","RecordID"]
                self.title_main = "Search"
                self.title_box = "Event Points Search"
                self.event_search = DialogBox(self.options,self.title_main,self.title_box)
            else:
                self.event_points_search.open()

        elif current_table == 8:
            if not hasattr(self,"club_reference_search"):
                self.options = ["Club RefernceID", "Date Joined","Date Left","RiderID","ClubID"]
                self.title_main = "Search"
                self.title_box = "Club Refernce Search"
                self.club_refernce_search = DialogBox(self.options,self.title_main,self.title_box)
            else:
                self.club_refernce_search.open()
