def main():

    codex = {1:{"c","f"}, 2:{"a","c","d","e","g"},
            3:{"a","c","d","f","g"},4:{"b","c","d","f"},
            5:{"a","b","d","f","g"},6:{"a","b","d","e","f","g"},
            7:{"a","c","f"},8:{"a","b","c","d","e","f","g"},
            9:{"a","b","c","d","f","g"}, 0:{"a","b","c","e","f","g"}}

    unique = {2:1, 4:4, 7:8, 7:3}

    out = 0
    with open("input.txt") as f:
        for line in f:
            line = line.replace("\n", "")
            patterns, output = line.split(" | ")
            patterns = patterns.split(" ")
            output = output.split(" ")

            numbers = patterns + output #combined list of numbers
            code = {"a":set(), "b":set(), "c":set(), "d":set(), 
                    "e":set(), "f":set(), "g":set()} 
            key = dict()

            #restrict possibilities
            #based on unique numbers
            for number in numbers:
                if len(number) in unique:
                    digit = unique[len(number)]
                    for signal in number:
                        for letter in codex[8]-codex[digit]:
                            code[signal].add(letter)

            #restrict possibilities based on whether a signal can
            #be present due to  known restrictions
            change = True
            while change:
                for number in numbers:
                    imposs_values = []
                    for i in range(10):
                        if len(codex[i]) != len(number):
                            imposs_values.append(i)
                    
                    poss_values = set(range(10)) - imposs_values

                    for value in poss_values:
                        needed_signals = codex[value]
                        for signal in needed_signals:
                            possible_sources = codex[8] - code[signal]
                            is_valid_value = False
                            for possible_source in possible_sources:
                                if possible_source in number:
                                    is_valid_value = True
                            if not is_valid_value:
                                imposs_values.add(
                              



                    








            
if __name__ == "__main__":
    main()
