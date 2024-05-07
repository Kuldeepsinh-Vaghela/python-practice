# Create a class 'Time' and initialize it with hours and minutes.
# Create a method addTime() which should take two Time objects
# and add them.
# E.g.- (2 hour and 50 min)+(1 hr and 20 min) is (4 hr and 10 min)
# Create another method displayTime() which should print the time.
# Also, create a method displayMinute() which should display the
# total minutes in the Time.
# E.g.- (1 hr 2 min) should display 62 minutes


class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    
    def addTime(self, time_2):
        total_min = (self.hours * 60) + (time_2.hours * 60) + self.minutes + time_2.minutes
        total_hours = total_min // 60
        min_total = total_min % 60
        print(f"{total_hours}hr and {min_total}min")
    
    def displayTime(self):
        print(f"{self.hours}hr and {self.minutes}min")
    
    def displayMinute(self):
        print(f"Total Minutes in time is {(self.hours * 60) + self.minutes} minutes")


tme1 = Time(10,24)
tme2 =  Time(1,1)

tme1.addTime(tme2)
tme1.displayTime()
tme2.displayMinute()


