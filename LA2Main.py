from Controller import Controller


def main():

    control = Controller()
    control.read_input()

    response = ""
    quit_flag = False
    print("Before While-Loop")
    while quit_flag is False:
        control.show_menu()
        response = input("Please choose an option: ")

        if response == "1":
            control.display_collection()
        elif response == "2":
            control.check_out_materials()
        elif response == "3":
            quit_flag = True
        else:
            print("Invalid response")
    print("Goodbye!")

main()
