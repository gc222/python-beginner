import time
import stdiomask

class user:
    def __init__(self):
        self.fName = None
        self.lName = None
        self.age = None
        self.email = None
        self.username = None
        self.password = None

    def register(self):
        self.fName = input("First name: ")
        self.lName = input("Last name: ")
        self.age = input("Age: ")
        self.email = input("Email: ")
        self.username = input("Create a Username: ")
        self.password = stdiomask.getpass("Create a Password: ")

    def login(self):
        un_input = input("\nUsername: ")
        pw_input = stdiomask.getpass()

        self.verification(un_input, pw_input)

    def verification(self, un_input, pw_input):
        if self.username == un_input and self.password == pw_input:
            print("Permission Granted.")
            time.sleep(3)
            print("Please wait ...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("...")
            time.sleep(2)
            print("We're in!")
        elif self.fName == un_input and self.lName != pw_input:
            print("Permission Denied. \nCheck your password!")
        elif self.fName != un_input and self.lName == pw_input:
            print("Permission Denied. \n Check your username!")
        else:
            print("Permission Denied. You should create a new account...")


user1 = user()
user1.register()
user1.login()
