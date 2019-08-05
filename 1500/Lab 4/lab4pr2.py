"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 4 Part 2
02/21/2018"""

'''This program asks a user for a file containing names and majors.
If the file exists it reads names and majors into a dictionary
as keys and values, respectively. If it does not exist it creates a new
file and saves it. The program allows a user to add a student and major,
delete a student and major, change the major of an existing student,
and display all students and their majors.'''

#imports function to determine if file already exists or not
import os.path

#**Only can read file correctly if it is a .txt file and if
#name and major pairs are written <name>:<major> with a new line
#after every major**
def read_file(filename):
    """Reads file if it exists, otherwise creates a new file.
    Args:
        filename (str): Name of file
    Returns:
        majors (dict): dictionary of names of students and majors or
        an empty dictionary if the file does not exist
    """
   
    wordlist = []
    majors={}
    
    #reads file
    if os.path.isfile(filename) == True:
        f = open(filename, 'r')
        text = f.readlines()
        f.close()
        
        #converts file into dictionary
        for i in range(len(text)):
            wordlist += text[i].split(':')

        for i in range(1,len(wordlist),2):
            wordlist[i] = wordlist[i][0:-1]

        for i in range(0,len(wordlist),2):
            majors[wordlist[i]] = wordlist[i+1]
    else:
        f = open(filename, 'w')
        f.close()
    return majors

def write_file(majors):
    """Writes new dictionary into file and saves
    Args:
        filename (str): Name of file
    Returns:
        written file
    """
    #format students and majors properly to be written into text file
    #in order to be work for next run
    output = ''

    for key, value in majors.items():
        output += key + ':' + value + '\n'

    ouput = output[0:-1]

    #saves text into users file 
    f = open(filename, 'w')
    f.write(output)
    f.close()
    return
    

                
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

#ask user for file name
filename = input('Enter file name here: ')

#calls read_file function
majors = read_file(filename)

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

#calls write_file function
write_file(majors)
        







