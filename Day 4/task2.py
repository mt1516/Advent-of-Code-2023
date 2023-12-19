def scratch_copy_card(input):
    line_count = {}
    for n, line in enumerate(input):
        winning_numbers, my_numbers = line.split(" | ")
        winning_numbers = winning_numbers.strip().split(": ")[1].replace("  ", " ").split(" ")
        my_numbers = my_numbers.strip().replace("  ", " ").split(" ")

        doubles = len(set(winning_numbers) & set(my_numbers))

        try:
            line_count[n] += 1
        except:
            line_count[n] = 1
        
        if doubles:
            for i in range(1, doubles + 1):
                try:
                    line_count[n + i] += line_count[n]
                except:
                    line_count[n + i] = line_count[n]

    return sum(line_count.values())


if __name__ == "__main__":
    # Read the input
    input = open("Day 4/task1_input.txt", "r")
    input = input.read().split("\n")
    test = open("Day 4/task2_test.txt", "r")
    test = test.read().split("\n")

    # Print the answer
    print("Test:", scratch_copy_card(test))
    print("Input:", scratch_copy_card(input))