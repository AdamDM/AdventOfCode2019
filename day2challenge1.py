def get_int_ops():
    with open("day2input.txt", "r") as input_file:
        int_ops = list(map(int, input_file.readline().split(",")))
    return int_ops


def run_int_ops(int_ops):
    current_position = 0
    while True:
        print(int_ops)
        current_value = int_ops[current_position]
        if current_value == 99:
            return int_ops[0]
        elif current_value == 1:
            int_ops[int_ops[current_position + 3]] = int_ops[int_ops[current_position + 1]] \
                                                     + int_ops[int_ops[current_position + 2]]
        elif current_value == 2:
            int_ops[int_ops[current_position + 3]] = int_ops[int_ops[current_position + 1]] \
                                                     * int_ops[int_ops[current_position + 2]]
        else:
            raise Exception
        current_position = current_position + 4


if __name__ == "__main__":
    print(run_int_ops(get_int_ops()))
