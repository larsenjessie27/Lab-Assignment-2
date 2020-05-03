from datetime import datetime, timedelta, date


class LibraryItem:
    def __init__(self,call_num):

        self.call_num = call_num
        self.checkedOut = False
    def check_out(self):

        self.checkedOut = True
        self.dateCheckedOut = date.today()


    def get_call_number(self):

        return self.call_num
    def is_checked_out(self):
 
        return self.checkedOut

    def get_date_checked_out(self):
   
        return self.dateCheckedOut

    def get_date_due(self):

        return self.dueDate

    def __str__(self):

        self.__string = "Call number" + self.call_num + "Checked out: " + self.checkedOut
        return self.__string
