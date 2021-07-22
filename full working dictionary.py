information = {
    'name': 'Slava',
}
command_list = ('''   
Add, Remove, Change, View, Quit
''')                #create a backup function

print("Welcome to our Dictionary. ")
while True:
    print("Select a command:")
    print(command_list)
    order = input("> ")
    if order.upper() == "ADD":
      key = input('Select a new key index: ')
      value = input(f'Select a value for '+key+' : ')
      information[key] = value
      print("Item add successfully!")
    elif order.upper() == "CHANGE":
        want_to_change = True
        while want_to_change:
            print("You are now changing a value. Please select the key index: ")
            print(information.keys())
            key = input(">").lower()
            print("Change the value")    #add an if statement to make it only change, confonds with add
            value = input(">")
            information.update({key: value})
            want_to_change = False
            print("Want to change something else?")
            choice1 = input("> ")
            if choice1.upper() == "YES":
               want_to_change = True
    elif order.upper() == "REMOVE":
        print("Select the key you want to remove:")
        print(information.keys())
        key = input("> ")
        print(f"Are you sure you want to delete " +key+ "? ")
        choice = input("> ")
        if choice.upper() == "YES":
            del information[key]
            print("Item deleted successfully!")
    elif order.upper() == "VIEW":
        print(information.items())
    elif order.upper() == "QUIT":
        break
    else:
        print("Sorry, I don't understand your demand.")



