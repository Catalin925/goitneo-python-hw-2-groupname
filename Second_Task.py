from First_Task import parse_input, add_contact, change_contact

from collections import UserDict;

def main():
    print("Welcome!", "I am your assistent bot! ")
    contact:dict = {}
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "terminate", "abort"]:
            print("Goodbye!")
            break
        elif command in ["hi", "hello"]:
            print ("What can I do for you?")
        elif command == "add":
            print(add_contact(*args, contact))
        else:
            print("Sorry, that's an invalid command. Try again.")

class Field:
    def __init__(self, value, name):
        self.value = value
        self.name = name

    def __str__(self):
        return str(self.value)

         
    
class Name(Field):
        def get_name(self):
            return self.value
        def set_name(self):
            return self.value
        
class Phone(Field):
        def get_phone(self):
             return self.value

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, name, phone):
         phones = Field(name, phone)
         self.phones.append(phone)
    
    def delete_phone(self, name):
         for phone in self.phones:
              if phone.name == name:
                   self.phones.remove(phone)
                   break
        
    def edit_phone(self, name, phone):
         for phone in self.phones:
              self.phones[phone] = input("Please provide the new phone number: ")
              break
    
    def find_phone(self, name, phone):
         for key in self.phones:
             print(self.phones[key])
             
class AddressBook(UserDict):
     def __init__(self, initial_data=None):
        super().__init__(initial_data)

     def __setitem__(self, name, phone):
        super().__setitem__(name, phone)

     def __getitem__(self, name):
        return super().__getitem__(name)

     def __delitem__(self, name):
        super().__delitem__(name)

     def __str__(self):
        return f"This is my book."
