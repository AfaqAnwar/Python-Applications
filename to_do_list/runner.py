from to_do_list.list import list


"""
Simple To-Do List.
Script that allows for the creation of a savable to-do list using the list.py object.
@Author Afaq Anwar
@Version 02/22/2019
"""


list_application = list()

print("Welcome to your list!" + "\n" + "Here are your current items..." + "\n")

list_application.display_items()

print("To add items type 'add' then when finished type 'quit' If you need to delete items type 'delete'" + "\n")

current_input = input("\n" + "Waiting for response...")

while current_input != "add" and current_input != "quit" and current_input != "delete":
    current_input = input("\n" + "Please type a valid option, 'add', 'delete, or 'quit'")

if current_input.lower() == "add":
    current_input = input("Add an item...")
    while current_input != "quit":
        list_application.add_item(current_input)
        current_input = input("\n" + "Add an item...")
elif current_input.lower() == "delete":
    print("\n" + "Current List Items: " + "\n")
    list_application.display_items()
    current_input = input("Specify an item to remove")
    while current_input != "quit":
        try:
            list_application.delete_item(current_input)
        except Exception as e:
            print("Error while deleting the requested item.")
        if list_application.get_list_size() == 0:
            print("List is empty..." + "\n" + "You may quit by typing 'quit")
            current_input = input("Waiting for a response...")
        else:
            print("\n" + "Update List Items: " + "\n")
            list_application.display_items()
            current_input = input("Specify an item to remove")
elif current_input.lower() == "quit":
    print("Okay, closing the application...")
    exit()
else:
    print("That is not a valid option")

print("\n" + "Here are all the items on your list..." + "\n")

list_application.display_items()

print("Would you like to save this list?")
response = input("Waiting for response...")

while response.lower() != "yes" and response.lower() != "no":
    print(response.lower())
    response = input("Please input yes or no...")

if response.lower() == "yes":
    list_application.save_list()
    print("List has been saved!")
elif response.lower() == "no":
    print("Okay, closing the application...")
