#!/usr/bin/env python3

# Title: Wizard inventory
# Name: Lauren P
# Date: 10/4/2023
# Description: DMD 1060

# Define functions
def showtitle():
    print ("The Wizard Inventory program")
    
def showmenu():
    print ("COMMAND MENU")
    print ("show - Show all items")
    print ("grab - Grab an item") #append adds to list
    print ("edit - Edit an item")
    print ("drop - Drop an item")
    print ("exit - Exit program")

def show(inventory): #shows items
    for number, item in enumerate(inventory, start=1):
        print (number, ". ", item)

def grab(inventory): #adds item
    if len(inventory) == 4:
        print ("You can't carry any more items. Drop something first.")
    else:
        newitem = input("Name: ")
        print (newitem, "was added.")
        inventory.insert(3, newitem)

def edit(inventory): #item[num] = newitem
    number = int(input("Number: "))
    if number < 1 or number > len(inventory):
        print("silly wizard, that's not an item in your list! :3")
    else:
        item = input("Updated name: ")
        inventory[number-1]=item
        print ("Item number", number, "was updated.")

def drop(inventory): #drops item
    number = int(input("Number: "))
    if number < 1 or number > len(inventory):
        print("silly wizard, that's not an item in your list! :3")
        drop(inventory)
        
    else:
        if number == 1:
            print(inventory[0], "was dropped.")
            inventory.pop(0)
        if number == 2:
            print(inventory[1], "was dropped.")
            inventory.pop(1)
        if number == 3:
            print(inventory[2], "was dropped.")
            inventory.pop(2)
        if number == 4:
            print(inventory[3], "was dropped.")
            inventory.pop(3)

def end(): #ends program
    print ("Bye!")

# Define main function 
def main():
    inventory = ["wooden staff", "wizard hat", "cloth shoes"]
    showtitle()
    showmenu()
    #get input
    while True:
        command = input("Command :")
        if command.lower() == "show":
            show(inventory)
        elif command.lower() == "grab":
            grab(inventory)
        elif command.lower() == "edit":
            edit(inventory)
        elif command.lower() == "drop":
            drop(inventory)
        elif command.lower() == "exit":
            end()
            break
        else:
            print ("Invalid entry, please enter show, grab, edit, drop, or exit. \n")
    

if __name__ == "__main__":
    main()




