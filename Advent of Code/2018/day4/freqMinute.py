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
        

#record how often each guard spent each minute asleep
guards= {}
for shift in shifts:
    
    guard = int(shift[0].action.split(" ")[1][1:]) #extract guard number
    previousDt = shift[0].dt
    for event in shift[1:]:
        
        if event.action == "falls asleep":
            previousDt = event.dt
            
        else:
            minutesAsleep = (event.dt - previousDt).seconds // 60
            
            for i in range(minutesAsleep):
                absMinute = previousDt.minute + i
                
                if guard in guards and absMinute in guards[guard]:
                    guards[guard][absMinute] += 1
                else:
                    if guard not in guards:
                        guards[guard] = {}
                    guards[guard][absMinute] = 1;
                    
            previousDt = event.dt

#compare each guard's most slept minute to find the max
maxSlept = 0
for guard in guards:
    for minute in guards[guard]:
        if guards[guard][minute] > maxSlept:
            maxSlept = guards[guard][minute]
            solution = guard * minute

print(solution)
    
                
                      
                           
