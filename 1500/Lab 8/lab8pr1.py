"""Marc Ojalvo and Daniel Licht
CMPS 1500
Thursday 3:30-4:45
Lab 8 Part 1
04/11/2018"""

class MilClock:

    def __init__(self, hours, minutes):
        """ The time Constructor 
            Args:
                self: object of type MilClock
                hours (str): Number of hours
                minutes (str): Number of minutes
            Returns:
                None
        """
        self.hours = int(hours)
        self.minutes = int(minutes)

    def __str__(self):
        """ Overloading of str function
            Args:
                self: Object of type MilClock
            Returns:
                s (str): The militatry time formatted in hh:mm
        """
        if len(str(self.hours)) == 1:
            self.hours = '0' + str(self.hours)
        if len(str(self.minutes)) == 1:
            self.minutes = '0' + str(self.minutes)           
        s = str(self.hours) + ':' + str(self.minutes)
        return s

    def addOne(self):
        """ Adds one minute to the time
            Args:
                self: Object of type MilClock
            Returns:
                A minute added to the time
        """
        self.minutes = int(self.minutes)
        self.hours = int(self.hours)
        self.minutes += 1
        if self.minutes == 60:
            self.minutes = 0
            self.hours += 1
            if self.hours == 24:
                self.hours = 00
        return 
        

    
        
