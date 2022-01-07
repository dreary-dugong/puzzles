
def main():

    aim = 0
    depth = 0
    position = 0

    with open("input.txt") as f:
        for line in f:

            command, units = line.split(" ")
            units = int(units)

            if command == "up":
                aim -= units
            elif command == "down":
                aim += units
            elif command == "forward":
                position += units
                depth += aim * units

    print(f"{aim=} {depth=} {position=}")
    print(f"{depth*position=}")

if __name__ == "__main__":
    main()
