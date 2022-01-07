character_truth_key = {1:{"c","f"}, 2:{"a","c","d","e","g"},3:{"a","c","d","f","g"},
        4:{"b","c","d","f"},5:{"a","b","d","f","g"},6:{"a","b","d","e","f","g"},
        7:{"a","c","f"},8:{"a","b","c","d","e","f","g"},9:{"a","b","c","d","f","g"},
        0:{"a","b","c","e","f","g"}} 



def get_displays(infile):
    nums = []
    with open(infile) as f:
        for line in f:
            line = line.strip(" \n")
            context_data= line.split(" | ")[0]
            output_data = line.split(" | ")[1]

            context_nums = set(context_data.split(" "))
            output_nums = set(output_data.split(" ")) 
            both_nums = (context_nums, output_nums)
            
            nums.append(both_nums)

    return nums

def check_display_output(display_output, inverted_nums_key):
    """return true if the the display output has been ascertained"""
    for character in display_output:
        if len(inverted_nums_key[character]) < 7:
            return False
    return True

def sync_keys(inverted_nums_key, inverted_signal_key):
    """make the keys consistent"""
    
    #1: eliminate possible numbers for characters if
    #signals don't support them
    for character, numset in inverted_nums_key.items():
        poss_nums = set(range(10)) - numset
        for number in poss_nums:
            poss_truths = character_truth_key[number]
            is_valid = True
            for truth in poss_truths:
                truthFound = False
                for signal in character:
                    possSignals =  character_truth_key[8] - inverted_signal_key[signal]
                    print(signal, possSignals)
                    for possSignal in possSignals:
                        if truth == possSignal:
                            truthFound = True
                            break
                if not truthFound:
                    is_valid = False
                    break
            if not is_valid:
                inverted_nums_key[character].add(number)
    
    #2: eliminate possible truths for signals if possible numbers
    #don't support them
    

    return inverted_nums_key, inverted_signal_key
                
def main():
    inputfile = "testSmall.txt"
    displays = get_displays(inputfile)


    total_output = 0 #this will be our program output
    for display in displays: #process each one seperately


        #initiate data structures
        display_context = display[0]
        display_output = display[1]
        display_all = display_context.union(display_output)

        inverted_nums_key = dict() #the numbers  each characters CAN'T be
        for character in display_all:
            inverted_nums_key[character] = set()
        inverted_signal_key = dict() #the truths each signal CAN'T be
        for character in display_all:
            for signal in character:
                if signal not in inverted_signal_key:
                    inverted_signal_key[signal] = set()


        #logic 1: load possible numbers based on length
        for character in display_all:
            for n in character_truth_key:
                if len(character_truth_key[n]) == len(character):
                    inverted_nums_key[character].add(n)

        inverted_nums_key, inverted_signal_key = sync_keys(inverted_nums_key, inverted_signal_key)                    

        print(display)
        print(character_truth_key)
        print(inverted_nums_key, inverted_signal_key)
        
        

        #logic 2: reduce signals based on overlap between numbers


def debug_sync():
    inverted_nums_key = {"af":{2,3,4,5,6,7,8,9,0}, "abcde":{1,3,4,6,7,8,9,0}}
    inverted_signal_key = {"a":{"b"}, "b":{"b"}, "c":{"b"}, "d":{"b"}, "e":{"b"}, "f":{"b"}}
    ink, isk = sync_keys(inverted_nums_key, inverted_signal_key)
    print(f"{ink=}\n{isk=}")
    

if __name__ == "__main__":
    main()



