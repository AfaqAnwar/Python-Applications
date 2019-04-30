import pickle


"""
Custom List Object.
@Author Afaq Anwar
@Version 02/22/2019
"""


class list:
    """
    Main Constructor
    Loads the existing list if possible, otherwise generates a new list.
    """
    def __init__(self):
        try:
            file_object = open('to_do_list.pydata', 'rb')
            self.to_do_list = pickle.load(file_object)
            file_object.close()
        except:
            self.to_do_list = []

    # Add an item to the list.
    def add_item(self, item):
        self.to_do_list.append(item)
        print("Item Added!")

    # Delete a specified item from the list by specifying the number within the list (index + 1).
    def delete_item(self, item_num):
        del self.to_do_list[int(item_num) - 1]
        print("Item Removed!")

    # Returns the size of the list.
    def get_list_size(self):
        return len(self.to_do_list)

    # Display all the items of the list with a number.
    def display_items(self):
        count = 1
        for item in self.to_do_list:
            print(str(count) + ": " + item + "\n")
            count += 1

    # Saves the list as a .pydata file by pickling the list object.
    def save_list(self):
        try:
            saved_list = open('to_do_list.pydata', 'wb')
            pickle.dump(self.to_do_list, saved_list)
            saved_list.close()
        except Exception as e:
            print(e)
            print("\n" + "Couldn't save the list.")
