def sum_of_numbers(input):
    # Sum of all the numbers
    sum = 0
    for i in input:
        # check if the line is empty
        if not i:
            continue

        for j in i:
            if j.isdigit():
                first_number = j
                break
        for j in reversed(i):
            if j.isdigit():
                second_number = j
                break
        
        # check if second number exist
        if not second_number:
            second_number = first_number

        number = int(first_number + second_number)
        sum += number
    
    return sum


if __name__ == "__main__":
    # Read the input
    input = open("Day 1/task1_input.txt", "r")
    input = input.read().split("\n")
    test = open("Day 1/task1_test.txt", "r")
    test = test.read().split("\n")

    # Print the answer
    print("Test:", sum_of_numbers(test))    
    print("Input:", sum_of_numbers(input))