#This is the main program for phonebook.py
#All nested functions are within
def main():
    import pickle
    #This creates an empty Dictionary
    phonebook = {}
    output_file = open('phonebook.dat', 'wb')
    output_file.close()
    #This nested function creates a yes/no question after every window
    #Asks if they want to return to the Main menu or exit program
    def mainmenu():
        MainMen = (input('Return to Main Menu? y/n? Then Enter.: '))
        if MainMen == 'y':
            Menu()
        elif MainMen == 'n':
            quit()
        #Exception handling if user enters anything but y or no
        else:
            print('Try typing y or n, no caps')
            mainmenu()
    #This nested function asks the user if they want to add another entry
    #Used in option 1 when added entries to the dictionary
    def NewEntry():
        NewEnt = (input('Do you want to add another entry? y/n? Then enter.:'))
        if NewEnt == 'y':
            print('Enter the name, followed by the number.')
            new = {(input('Name: ')):(input('Number: '))}
            phonebook.update(new)
            print()
            output_file = open('phonebook.dat', 'wb')
            pickle.dump(phonebook, output_file)
            output_file.close()
            print('Phonebook entry added.')
            print()

        #This breaks the loop
        elif NewEnt == 'n':
            #line 11
            mainmenu()
        #exception handling incase user enters anything but  y or no
        else:
            print('You must enter y or n, no caps.')
        #Loops function back onto itself until the user is done entering entries
        NewEntry()
        print()
    # This function asks the user if they want to enter a new search
    def NewSearch():
        NewSrch = (input('Do you want to search another name? y/n, then enter.'))
        if NewSrch == 'y':
            print('Enter the name of the entry you looking for, then hit enter.')
            name = phonebook.get(input('Name: '),'Entry not found.')
            print()
            print(name)
            print()
            
        #This breaks the loop
        elif NewSrch == 'n':
            #line 11
            mainmenu()
            print()
        #exception handling if user enters anything but y or no
        else:
            print('You must enter either y or n, no caps.')
        #Loops function until n is given 
        NewSearch()
        print()

    def AreYouSure():
        response = (input('Are you sure you want to delete an entry? y/n? Then enter:'))
        if response == 'y':
            print("Enter who you'd like to delete, then enter.")
            del phonebook[(input('Name: '))]
            print()
            output_file = open('phonebook.dat', 'wb')
            pickle.dump(phonebook, output_file)
            output_file.close()
            print('Phonebook entry deleted.')
            print()
            mainmenu()
            if response == 'n':
                mainmenu()
            else:
                print('You must enter either y or n, no caps.')
        print()
        AreYouSure()
    print()
#This displays the main menu of the program
#It appears first and gives options to the user to choose from.
    def Menu():
        #Stores the menu options into a set to be called upon
        MenuSet = set([1,2,3,4,5])
        print()
        print('Welcome to my Phonebook Program!')
        print('Choose from one of the following options.')
        print()

        #Lists Main Menu option 1-5 for user to pick from.
        # menu being pulled from set in for structure takes away randomization of a set storage
        for num in MenuSet:
            if num == 1:
                print('1. Add an Entry into your phonebook.')
            if num == 2:
                print('2. Delete an entry from your phonebook') 
            if num == 3:
                print('3. Search your phonebook by name.')
            if num == 4:
                print('4. Display you entire phonebook.')
            if num == 5:
                print('5. Exit the program.')
        print()
        #This determines which section to take the user to depending on their choice.
        choice = int(input('Enter Choice: '))
        #Menu option 1 code. Add an entry
        if choice == 1:
            print('Enter the name, followed by the number, then enter.')
            new = {(input('Name: ')):(input('Number: '))}
            phonebook.update(new)
            print()
            output_file = open('phonebook.dat', 'wb')
            pickle.dump(phonebook, output_file)
            output_file.close()
            print('Phonebook entry added.')
            print()
            #This function asks user if they want to add another entry or return to main menu
            #Function found on line 23.
            NewEntry()
            print()
            #This function asks the user if they want to return to the main menu or exit the program.
            mainmenu()

        #Menu option 2 code. Delete entry.
        elif choice == 2:
            AreYouSure()
            mainmenu()
            
        #menu option 3 code. Search the Phonebook.
        elif choice == 3:
            print('Enter the name of the entry you looking for, then hit enter.')
            #Search the dictionary for the variable to the key given.
            name = phonebook.get(input('Name: '),'Entry not found.')
            print()
            print(name)
            print()
            NewSearch()
        #menu option 4 code. Display the entire phonebook
        elif choice == 4:
            print()
            print(phonebook)
            print()

            mainmenu()
        elif choice == 5:
            #built in code to exit program
            quit()
        else:
            print('You must choose a number between 1-5.')
            mainmenu()
    #This initiates the Main Menu function after the Main Program has been run
    Menu()
#This initiates the Main Program
main()