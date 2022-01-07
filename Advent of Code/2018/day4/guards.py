from datetime import datetime #used to store date time info

class event:

    def __init__(self, dt, actionString):
        self.dt = dt
        self.action = actionString

    def __lt__(self, other):
        assert type(self) == type(other)
        return self.dt < other.dt
    def __gt__(self, other):
        assert type(self) == type(other)
        return self.dt > other.dt
    def __eq__(self, other):
        assert type(self) == type(other)
        return self.dt == other.dt
    def __str__(self):
        return str(self.dt) + " " + self.action;

#read file
filename = "input.txt"
events = []
with open(filename, 'r') as f:
    for line in f:
        line = line.replace("\n", "");
        dt = datetime.fromisoformat(line[line.index("[")+1:line.index("]")].replace(" ", "T"))
        eventString = line[line.index("]")+2:]
        events.append(event(dt, eventString))


#list of events in chronolgical order
events.sort();


#separate events into shift subgroups
shifts = []
currShift = [events[0]]
for event in events[1:]:
    if event.action != "falls asleep" and event.action != "wakes up":
        shifts.append(currShift);
        currShift = [event]
    else:
        currShift.append(event)
        
#record the total time each guard slept across all shifts
guards = {}
for shift in shifts:
    guard = int(shift[0].action.split(" ")[1][1:]) #extract guard number
    previousDt = shift[0].dt
    for event in shift[1:]:
        if event.action == "falls asleep":
            previousDt = event.dt
        else:
            minutesAsleep = (event.dt - previousDt).seconds // 60 
            if guard in guards:
                guards[guard] += minutesAsleep
            else:
                guards[guard] = minutesAsleep
            previousDt = event.dt

#find the guard who spent the most time asleep
maxSleep = 0
for guard in guards:
    if guards[guard] > maxSleep:
        maxSleep = guards[guard]
        sleepiestGuard = guard

#go back through the sleepist guard's shifts and tally every minute they spend sleeping
minutes = {}
for shift in shifts:
    guard = int(shift[0].action.split(" ")[1][1:]) #extract guard number
    if guard == sleepiestGuard:
        previousDt = shift[0].dt
        for event in shift[1:]:
            if event.action == "falls asleep":
                previousDt = event.dt
            else:
                minutesAsleep = (event.dt - previousDt).seconds // 60 
                for i in range(minutesAsleep):
                    absMinute = previousDt.minute + i
                    if absMinute in minutes:
                        minutes[absMinute] += 1
                    else:
                        minutes[absMinute] = 1;
                previousDt = event.dt

#find the absolute minute when the guard slept the most
maxSlept = 0
for minute in minutes:
    if minutes[minute] > maxSlept:
        maxSlept = minutes[minute]
        maxAbsMinute = minute

print(sleepiestGuard * maxAbsMinute)
    
                
                      
                           
