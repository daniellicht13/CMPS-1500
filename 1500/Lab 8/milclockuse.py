from MilClock import *
def addMinutes(clock, n):
    ''' add n minutes to the clock '''

    for x in range(n):
        clock.addOne()
        
hallClock = MilClock(5,0)
print('We wake up at', hallClock)
addMinutes(hallClock, 30)
print('We get up at', hallClock)
addMinutes(hallClock, 40)
print('We are sleepy again by', hallClock)



wristWatch = MilClock(23,0)
print('Last tram leaves at', wristWatch)
addMinutes(wristWatch,59)
print('Today ends at', wristWatch)
wristWatch.addOne()
print('Tomorrow starts at', wristWatch)
