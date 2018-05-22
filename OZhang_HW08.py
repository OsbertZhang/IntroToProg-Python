#-------------------------------------------------#
# Title: Classes and Methods - Objects
# Dev:   Osbert Zhang
# Date:  May 21th, 2018
# ChangeLog: (Who, When, What)
#   Osbert Zhang, 05/21/2018,
# Assignment 08 - Classes and Methods
#-------------------------------------------------#

#The basic form of this code was provided as part of the homework assignment document.
#The assignment is to create functions and methods to be able to proccess the data using the provided code.

#Create a new class to process the data for each entry of ID, Name, and Price
class Item(object):
    """Items to be Processed"""

    ID = None
    Name = None
    Price = None

    def __init__(self, ID, name, price):
        self.ID = ID
        self.Name = name
        self.Price = price

# Inherent Python string maker
# Couldn't get the python version to work so created manual string converter function below...
#    def __str__(self):
#        return self.ID + ',' + self.Name + ',' + self.Price

    def MakeString(self):
        """A function to return a string in a specific format"""
        return self.ID + ',' + self.Name + ',' + self.Price


#Processing
#I created a new class to encapsulate the functions that would read, write and process the data to the file.
class Processing():
    """Processing the Data"""
    strUserInput = None  # A string which holds user input

    def WriteProductUserInput(File):
        '''Function to get and write data'''
        try:
            print("Type in a Product Id, Name, and Price you want to add to the file")
            print("(Enter 'Exit' to quit!)")
            while(True):
                strUserInput = input("Enter the Id, Name, and Price (ex. 1,ProductA,9.99): ")
                if(strUserInput.lower() == "exit"):
                    break
                else:
                    lstInput = strUserInput.split(',')  #Comma as delimiter to split string for list
                    objPrdt = Item(lstInput[0], lstInput[1], lstInput[2]) #Pass components of input into Item() class
                    File.write(objPrdt.MakeString() + "\n") #Write to file
        except Exception as e:
            print("Error: " + str(e))
    #Note: This code currently doesn't check to see if the inputs are valid types. A limitation of this function is that
    #it will also break the loop if the input does not include 2 commas to create 3 indices for the list...
    #Code also doesn't check for duplicates...


    def ReadAllFileData(File, Message="Contents of File"):
        '''Function to Read Text File'''
        try:
            print(Message)
            File.seek(0)
            print(File.read())
        except Exception as e:
            print("Error: " + str(e))


#I/O
def main():
    """Main Program Functionality"""
    try:
        objFile = open("Products.txt", "r+")
        Processing.ReadAllFileData(objFile, "Here is the current data:")
        Processing.WriteProductUserInput(objFile)
        Processing.ReadAllFileData(objFile, "Here is the data that was saved:")
    except FileNotFoundError as e:
        print("Error: " + str(e) + "\n Please check the file name")
    except Exception as e:
        print("Error: " + str(e))
    finally:
        if (objFile != None): objFile.close()


#Code to actually run program
main()
input('Press the enter key to continue')

