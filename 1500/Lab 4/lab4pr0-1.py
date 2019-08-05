## Copy all function definitions from IDLE to here


## look_up 
def look_up(d):
    """Prints out a major associated with a name in the dictionary
    Args:
        d (dict): Dictionary of names and majors
    Returns:
        str: Major associated with name
        or
        str: Message saying 'Not found.'
    """
    name = input('Enter a name: ')
    if name in majors.keys():
        print(majors.get(name))
    else:
        print('Not found.')
    return

## add
def add(d):
    """Adds an entry of a given name and major to the dictionary
    Args:
        d (dict): Dictionary of names and majors
    Returns:
        str: Dictionary with new name and major adde
        or
        str: Message saying 'A person with this name already exists in the system.'
    """
    name = input('Enter a name: ')
    major = input('Enter a major: ')
    if name not in majors.keys():
        majors[name] = major
    else:
        print('A person with this name already exists in the system.')
    return   

## change 
def change(d):
    """Changes the major of an existing name in the dictionary
    Args:
        d (dict): Dictionary of names and majors
    Returns:
        str: Updated dictionary of names and major
        or
        str: Message saying 'That name is not found.'
    """
    name = input('Enter a name: ')
    if name in majors.keys():
        major = input('Enter the new major: ')
        majors[name] = major
    else:
        print('That name is not found.')
    return

## delete 
def delete(d):
    """Deletes an entry of a given name from the dictionary
    Args:
        d (dict): Dictionary of names and majors
    Returns:
        str: Dictionary without removed name and major
        or
        str: Message saying 'That name is not found.'
    """
    name = input('Enter a name: ')
    if name in majors.keys():
        del majors[name]
    else:
        print('That name is not found.')
    return
## display
def display(d):
    """ Displays all dictionary entries, one name/major pair per line
    Args:
        d (dict): Dictionary of names and majors
    Returns:
        str: Display of all entries as "<name> is a wizard in <major>"
    """
    for name, major in majors.items():
        print(name, 'is a wizard in', major)
    return


## get_menu_choice 
def get_menu_choice():
    """ Displays all possible choices for editing/viewing dictionary
    Args:
        None
    Returns:
        User's choice
    """
    print('Majors of College Students')
    print('---------------------------')
    print("1. Look up a student's major")
    print('2. Add a new student')
    print('3. Change a major')
    print('4. Delete a student')
    print('5. Display all students')
    print('6. Quit the program\n')
    choice = input('Enter your choice: ')

    if choice not in '123456':
        while choice not in '123456':
            choice = input('Enter a valid choice: ')          
    return choice

## The main part of your program
majors = {'Harry':'Computer Science', 'Hermione':'Mathematics','Ron':'English'}
choice = '0'

while choice != '6':

        choice = get_menu_choice()

        if choice == '1':
            look_up(majors)
        elif choice == '2':
            add(majors)
        elif choice == '3':
            change(majors)
        elif choice == '4':
            delete(majors)
        elif choice == '5':
            display(majors)
