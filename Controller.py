import LibraryItem
from Book import Book
from Periodical import Periodical
from datetime import date

class Controller:
    def __init__(self):

        self.__library_list = []
    def show_menu(self):

        print("------------- Menu -------------")
        print("1) Display collection")
        print("2) Check out materials")
        print("3) Quit")
        print("------------------------------------")

    def display_collection(self):

        for i in self.__library_list:
            print(i)

    def find_item(self, callNum):


        for i in self.__library_list:
            if callNum == i.get_call_number():
                return i

    def check_out_materials(self):

        call_number = input("Please enter the call number: ")
        item = self.find_item(call_number)
        if item is None:
            print("Call number not valid")
        elif item.is_checked_out():
            print("Item not available")
        else:
            item.check_out()
            item.set_date_due()
            print(item)


    def read_input(self):

        infile = open("input.txt", "r")
        line = infile.readline()
        line = infile.readline()
        for line in infile:
            line = line.rstrip("\n")
            line = line.split(',')
            item = None
            if line[0] == "B":
                item = Book(line[1], line[2], line[3], line[4])
            else:
                item = Periodical(line[1], line[2], line[3], line[4], line[5])
            self.__library_list.append(item)



