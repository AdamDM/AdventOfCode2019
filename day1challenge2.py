def calculate_fuel(mass):
    initial_fuel = calculate_base_fuel(mass)
    newly_added_mass = initial_fuel
    while newly_added_mass >= 9:
        newly_added_mass = calculate_base_fuel(newly_added_mass)
        initial_fuel += newly_added_mass
    return initial_fuel


def calculate_base_fuel(mass):
    return (mass // 3) - 2

# with open("day1input.txt", "r") as input_file:
#     fuel_count = 0
#     for line in input_file.readlines():
#         fuel_count += calculate_base_fuel(int(line))
#     newly_added_mass = fuel_count
#     while newly_added_mass >= 9:
#         newly_added_mass = calculate_base_fuel(newly_added_mass)
#         fuel_count += newly_added_mass
#
#     print(fuel_count)
#


with open("day1input.txt", "r") as input_file:
    fuel_count = 0
    for line in input_file.readlines():
        fuel_count += calculate_fuel(int(line))
    print(fuel_count)
