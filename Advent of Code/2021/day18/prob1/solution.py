def get_fsnums(infile):
    #for now, everything is string operations
    fsnums = []
    with open(infile) as f:
        for line in f:
            fsnums.append(line.strip())
    return fsnums


def fs_add(fsn1, fsn2):
    unreduced = "[" + fsn1 + "," + fsn2 + "]"
    reduced = fs_reduce(unreduced)
    return reduced

def fs_reduce(fsn):
    changed = True
    while changed:
        if can_explode(fsn):
            fsn = fs_explode(fsn)
        elif can_split(fsn):
            fsn = fs_split(fsn)
        else:
            changed = False
    return fsn

def can_explode(fsn):
    depthMeter = 0
    for c in fsn:
        if c == "[":
            depthMeter += 1
        elif c == "]":
            depthMeter -= 1
        if depthMeter == 4:
            return True
    return False

def can_split(fsn):
    #if we have 2 digits in a row, a number is >= 10
    prevWasDigit = False
    for c in fsn:
        currIsDigit = c.isnumeric()
        if currIsDigit and prevWasDigit:
            return True
        prevWasDigit = currIsDigit
    return False

def fs_explode(fsn):
    lastDigitIndex 
    

def fs_split(fsn):
    pass

def get_magnitude(fsn):

def main():
    infile = "testinput.txt"
    fsnums = get_fsnums(infile)

    total = fsnums[0]
    for fsn in fsnums[1:]:
        total = fs_add(total, fsn)

    out = get_magnitude(total)
    print(out)


