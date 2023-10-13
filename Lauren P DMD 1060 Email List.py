#!/usr/bin/env python3

# Title: contact manager
# Name: Lauren P
# Date: 10/12/2023
# Description: DMD 1060

# Define functions
def showtitle():
    print ("Contact Manager \n")
    
def showmenu():
    print ("COMMAND MENU")
    print ("list - Display all contacts")
    print ("view - View a contact") #note to self- append adds to list
    print ("add - Add a contact")
    print ("del - Delete a contact")
    print ("exit - Exit program")
    print (" ")

def showlist(contacts): #shows contacts
    if len(contacts) == 0:
        print("No contacts. \n")
        return
    else:
        i = 1
        for row in contacts:
            print(str(i) + ". " + row[0])
            i += 1
        print()

def view(contacts): 
    number = int(input("Number: "))
    if number < 1 or number > len(contacts):
        print("Invalid contact number.")

    else:
        print("Name: ",contacts[number-1][0])
        print("Email: ",contacts[number-1][1])
        print("Phone: ",contacts[number-1][2])
        print(" ")

def add(contacts): #adds a contact
    name = input("Name :")
    email = input("Email :")
    pnumber = input("Phone :")
    newcontact = []
    newcontact.append(name)
    newcontact.append(email)
    newcontact.append(pnumber)
    contacts.append(newcontact)
    print(newcontact[0] + " was added.\n")   

def delete(contacts): #drops a contact
    number = int(input("Number: "))
    if number < 1 or number > len(contacts):
        print("Invalid contact number.")
        delete()
        
    else:
        contact = contacts.pop(number-1)
        print(contact[0] + " was deleted.\n")

def end(): #ends program
    print ("Bye!")

# Define main function 
def main():
    contacts = [["Eric Idle", "eric@ericidle.com", "207-946-0958"],
                ["Hatsune Miku", "mikuhatsune39@vocaloid.com", "393-939-3939"]]
    showtitle()
    showmenu()
    #get input
    while True:
        command = input("Command: ")
        if command.lower() == "list":
            showlist(contacts)
        elif command.lower() == "view":
            view(contacts)
        elif command.lower() == "add":
            add(contacts)
        elif command.lower() == "del":
            delete(contacts)
        elif command.lower() == "exit":
            end()
            break
        else:
            print ("Invalid command. \n")
    

if __name__ == "__main__":
    main()




