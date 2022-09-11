# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# Change Log:
# MSteinauer, 9.9.2022, Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    """ Saves data from a List to a File

            :param file_name: (string) with name of file:
            :param list_of_data: (list) you want filled with file data:
            :return: nothing
    """
    objectFile = open(file_name, "ab")
    for row in list_of_data:
        pickle.dump(row, objectFile)
    objectFile.close()


def read_data_from_file(file_name):
    """ Reads data from File to a List

            :param file_name: (string) with name of file
            :return objectFileData: (list) of file data
    """
    print(f"Reading data from {file_name}...")
    objectFile = open(file_name, "rb")
    objectFileData = []
    while True:
        try:
            objectFileData.append(pickle.load(objectFile))
        except EOFError:
            print("No more data in file. Closing file...")
            break
    objectFile.close()
    return objectFileData

def id_name_input():
    """ Gets ID and Name input from a user

        :param: none
        :return input ID: (int) ID input by user, inputName: (str) Name input by user
    """
    try:
        inputID = int(input("Enter Id: "))
    except ValueError:
        print("Please enter a number for the Id")
        inputID = int(input("Enter Id: "))
    inputName = input("Enter Name: ")
    return inputID, inputName

# Presentation ------------------------------------ #
id, name = id_name_input()
lstCustomer = [id, name]

save_data_to_file(strFileName, lstCustomer)

allCustomers = read_data_from_file(strFileName)
print("The current data is: ")
for i in range(0,len(allCustomers),2):
    print(allCustomers[i], allCustomers[i + 1])