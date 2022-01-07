
def main():

    vertical, horizontal = 0, 0
    with open("input.txt") as f:
        for line in f:
            direction, units = line.split(" ")
            units = int(units)

            if direction == "up":
                vertical -= units
            elif direction == "down":
                vertical += units
            else:
                horizontal += units
    
    print(f"{vertical=}{horizontal=}")
    print("Final: " + str(vertical*horizontal))

if __name__ == "__main__":
    main()
