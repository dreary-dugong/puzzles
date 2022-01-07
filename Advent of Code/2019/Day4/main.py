def hasRepeatingDigits(n):
    """return true if two adjacent digits in n repeat"""
    digits = getDigits(n);
    i = 0;
    while True:
        current = digits[i];
        strand = 0;
        if digits[i] == current:
            while i < len(digits) and digits[i] == current:
                strand += 1;
                i += 1;
        else:
            i += 1
        if strand == 2:
            return True;
        if i>=len(digits):
            return False;

    
def getDigits(n):
    """return digits of n in a list"""
    output = [];
    for i in range(len(list(str(n)))):
        output.append(int(str(n)[i]));
    return output;

output = 0; #num of intermediate numbers that qualify
minimum = 188888 #low end of range
maximum = 657474 #high end of range
n = minimum;

while n < maximum:

    #assume valid starting number
    if hasRepeatingDigits(n):
        output+=1
    n+=1
    
    digits = getDigits(n); #list of digits in number
    string = str(digits[0]); #used to reassemble fixed digits
    
    for i in range(len(digits)-1):
        
        if digits[i+1] < digits[i]: #if the number decreases
            digits[i+1] += (digits[i] - digits[i+1]);
            
        string += str(digits[i+1]);
    n = int(string);


print(output);
        
        
    
    
