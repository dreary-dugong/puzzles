#contsnts
INPUT_FILE = "input1.txt"
NUM_CYCLES = 6

#variables
active = set() #positions of current active cubes
to_activate = set() #positions of cubes to activate after the current cycle
to_deactivate = set() #positions of cubes to deactivate after the current cycle
to_check = set() #positions of cubes to check for (de)activation in the current cycle

#helper functions
def print_dim():
    """print the dimension based on current active cubes"""
    all_x = [x for x, y, z in active]
    all_y = [y for x, y, z in active]
    all_z = [z for x, y, z in active]

    xy_range = max(max([abs(x) for x in all_x]), max([abs(y) for y in all_y]))

    for curr_z in range(min(all_z), max(all_z) + 1):
        print("\nz=" + str(curr_z))
        for curr_y in range(-1*xy_range, xy_range+1):
            currLine = ""
            for curr_x in range(-1*xy_range, xy_range+1):
                if (curr_x, curr_y, curr_z) in active:
                    currLine += "#"
                else:
                    currLine += "."
            print(currLine)
    

def get_neighbors(cube):
    """get set of positions of a cube's neighbors"""
    
    MAX_CHANGE = 1
    INCS = range(-1*MAX_CHANGE, MAX_CHANGE+1)
    
    x, y, z, w = cube
    neighbors = set()
    for x_inc in INCS:
        for y_inc in INCS:
            for z_inc in INCS:
                for w_inc in INCS:
                    neighbors.add((x+x_inc, y+y_inc, z+z_inc, w+w_inc))
    return neighbors

def count_active_neighbors(cube):
    """get number of neighbors of a cube which are active"""
    global active
    num_active_neighbors = 0
    for neighbor in get_neighbors(cube):
        if neighbor in active:
            num_active_neighbors += 1
    return num_active_neighbors

#read input
fileLen = 0
with open(INPUT_FILE) as prefile:
    fileLen = len(prefile.readlines())

z = 0 #input only has one slice
w = 0
with open(INPUT_FILE) as file:
    y = -1 * (fileLen // 2)
    for line in file:
        x  = -1 * (len(line.replace("\n", "")) //2)
        for char in line:
            if char == "#":
                active.add((x, y, z,w))
            x += 1
        y += 1

#get initial state
"""
print("Before any cycles:")
print("Active: " + str(active))
print_dim();
"""

#execute cycles
for curr_cycle in range(NUM_CYCLES):

    #reset vars
    to_activate = set()
    to_deactivate = set()
    to_check = set()

    #which cubes do we check this cycle?
    #(the ones with at least one active neighbor,
    #including itself)
    for cube in active:
        to_check.update(get_neighbors(cube))

    #now we check them
    for cube in to_check:

        #does it need to be deactivated
        if cube in active:
            if (count_active_neighbors(cube) - 1) not in (2,3):
                to_deactivate.add(cube)

        #does it need to be activated
        else:
            if count_active_neighbors(cube) == 3:
                to_activate.add(cube)

    #now update active
    active.update(to_activate)
    active.difference_update(to_deactivate)

    #visual representation after each cycle for debugging
    """
    print("\n\nAfter " + str(curr_cycle + 1) + " cycles: ")
    print_dim()
    """


#give output (number of active cubes after all cycles)
print(len(active))    
    
