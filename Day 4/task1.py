def scratch(input):
    total_points = 0
    for line in input:
        winning_numbers, my_numbers = line.split(" | ")
        winning_numbers = winning_numbers.strip().split(": ")[1].replace("  ", " ").split(" ")
        my_numbers = my_numbers.strip().replace("  ", " ").split(" ")

        doubles = len(set(winning_numbers) & set(my_numbers))

        if doubles:
            total_points += 2 ** (doubles - 1)

    return total_points


if __name__ == "__main__":
    # Read the input
    input = open("Day 4/task1_input.txt", "r")
    input = input.read().split("\n")
    test = open("Day 4/task1_test.txt", "r")
    test = test.read().split("\n")

    # Print the answer
    print("Test:", scratch(test))
    print("Input:", scratch(input))