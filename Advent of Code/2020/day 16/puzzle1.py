#constants
INPUT_FILE = "testInput1.txt"

#read input
with open("testInput1.txt") as file:
    unparsed_fields, our, nearby = file.read().split("\n\n")

#parse data
class Field():
    def __init__(self, name, ranges):
        self.name = name
        self.ranges = []
        for r in ranges:
            self.ranges.append(Range(r))
    def __str__(self):
        return self.name + ": " + str([str(r) for r in self.ranges])
            
class Range():
    def __init__(self, r):
        self.min = r[0]
        self.max = r[1]
    def is_valid(n):
        return n >= self.min and n <= self.max
    def __str__(self):
        return str(self.min) + "-" + str(self.max)
            
fields = [] #list of fields to check

for u_field in unparsed_fields.split("\n"):
    curr_name, etc = u_field.replace("\n", "").split(": ")
    curr_u_ranges = etc.split(" or ")
    curr_ranges = [ran.split("-") for ran in curr_u_ranges]

    fields.append(Field(curr_name, curr_ranges))

nearby_tickets = [ticket.split(",") for ticket in nearby.split(":\n")[1].split("\n")]


#processing
num_invalid = 0
for ticket in nearby_tickets:
    valid_ticket = False
    for field in fields:
        valid_field = False
        for value in ticket:
            valid_value = False
            for r in field.ranges:
                if 











                
    for value in ticket:
        valid_value = False
        for field in fields:
            for r in field.ranges:
                if is_valid(value):
                    valid_value = True

