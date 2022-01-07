
def main():

    #load input into a list
    with open("input.txt") as f:
        report = f.readlines()
    report = [n.replace("\n", "") for n in report]

    oxyfil = [True] * len(report)
    cofil = [True] * len(report)
    i = 0
    while sum(oxyfil) > 1 or sum(cofil) > 1:

        #get digit to check for
        oxytotal = 0
        oxyones = 0
        cototal = 0
        coones = 0
        for j, n in enumerate(report):
            if oxyfil[j]:
                oxyones += int(n[i])
                oxytotal += 1
            if cofil[j]:
                coones += int(n[i])
                cototal += 1
        oxydigit = '1' if oxyones >= oxytotal - oxyones  else '0'
        codigit = '1' if coones <  cototal - coones else '0'

        #eliminate everything that doesn't have our digit
        for j, n in enumerate(report):
            if sum(oxyfil) > 1:
                if oxyfil[j] and n[i] != oxydigit:
                    oxyfil[j] = False

            if sum(cofil) > 1:
                if cofil[j] and n[i] != codigit:
                    cofil[j] = False

        i += 1

    oxybin = report[oxyfil.index(True)]
    cobin = report[cofil.index(True)]

    oxyint = 0
    coint = 0
    digitcount = len(oxybin)
    for i in range(digitcount):
        oxyint += 2**i * int(oxybin[digitcount - i - 1]) 
        coint += 2**i * int(cobin[digitcount - i - 1]) 
    
    print(f"{oxyint=} {coint=} {oxyint*coint=}")

if __name__ == "__main__":
    main()


                
