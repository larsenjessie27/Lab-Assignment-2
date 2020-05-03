from LibraryItem import LibraryItem
from datetime import datetime, timedelta


class Periodical(LibraryItem):
    def __init__(self, call_num, period_title, volume, issue, subject):

        LibraryItem.__init__(self, call_num)
        self.__period_title = period_title
        self.__volume = volume
        self.__issue = issue
        self.__subject = subject

    def set_date_due(self):

        self.__dueDate = self.__checkOutDate + timedelta(7)

    def __str__(self):

        self.__period_string = "Periodical Title: " + self.__period_title + "\n" \
        "Volume: " + self.__volume + "\n" \
        "Issue: " + self.__issue + "\n" \
        "Subject: " + self.__subject + "\n" \
        "Call number: " + self.call_num + "\n"
        if self.checkedOut:
            self.__period_string = self.__period_string + "Checked out: Yes" + "\n" + "Date out: " + str(self.dateCheckedOut) + "\n" \
            "Date due: " + str(self.__dueDate)
        else:
            self.__period_string = self.__period_string + "Checked out: No" + "\n"
        return self.__period_string
