def calculateFuel(mass):
    return (mass // 3) - 2


with open("day1input.txt", "r") as input_file:
    count = 0
    for line in input_file.readlines():
        count += calculateFuel(int(line))
    print(count)
    