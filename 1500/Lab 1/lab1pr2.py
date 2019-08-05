"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 1 Part 2
01/31/2018"""

date = input('Please enter date in MM/DD/YYYY format: ') 

if len(date) == 10:           #assigns string value to day and year and integer value to a month if user inputs date in MM/DD/YYYY format
    day = date[3:5]
    month = int(date[0:2]) - 1
    year = date[6:10]
elif len(date) == 8:      #if month and day are both single digit and user does not add 0
    day = '0' + date[2:3]
    month = int('0' + date[0:1]) - 1
    year = date[4:8]
elif len(date) == 9 and date[1] == '/' and date[0] != '0':     #if month is single digit and day is double digit and user does not add 0
    day = date[2:4]
    month = int('0' + date[0:1]) - 1
    year = date[5:9]
elif len(date) == 9 and date[1] != '/' and date[0] != '0':     #if month is double digit and day is single digit and user does not had 0
    day = '0' + date[3:4]
    month = int(date[0:2]) - 1
    year = date[5:9]
elif len(date) == 9 and date[1] != '/' and date[0] == '0':     #if month and day are both single digit but user only adds 0 to month
    day = date[0:2]
    month = int('0' + date[3:4]) - 1
    year = date[5:9]
elif len(date) == 9 and date[1] == '/' and date[2] == '0':     #if month and day are both single digit but user only adds 0 to day
    day = '0' + date[0:1]
    month = int(date[2:4]) - 1
    year = date[5:9]

L = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

month = L[month]        #converts the integer value assigned to month to a string of the name of the month 
   
print(month,day, end = '')
print ( ',', year )

