from LibraryItem import LibraryItem
from datetime import timedelta


class Book(LibraryItem):
    def __init__(self, call_num, book_title, author, genre):
        
        super(Book,self).__init__(call_num)
        self.__book_title = book_title
        self.__author = author
        self.__genre = genre


    def set_date_due(self):

        self.__dueDate = self.dateCheckedOut + timedelta(21)

    def __str__(self):

        self.__book_string = "Book name: " + self.__book_title + "\n" + \
        "Author: " + self.__author + "\n" + \
        "Genre: " + self.__genre + "\n" + \
        "Call Number: " + self.call_num + "\n"
        if self.checkedOut:
            self.__book_string = self.__book_string + "Checked out: Yes" + "\n" + "Date out: " + str(self.dateCheckedOut) + "\n" \
            "Date due: " + str(self.__dueDate) + "\n"

        else:
            self.__book_string = self.__book_string + "Checked out: No" + "\n"
        return self.__book_string
