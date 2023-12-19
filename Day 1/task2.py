def sum_of_numbers_alphabet(input):
    # Sum of all the numbers
    sum = 0
    # Dictionary for replacing words with numbers
    # Keep the beginning and the end of the word to avoid replacing common letters
    digit_map = {"one": "o1e", "two": "t2o", "three": "t3e", "four": "f4r", "five": "f5e",
                "six": "s6x", "seven": "s7n", "eight": "e8t", "nine": "n9e"}
    
    for i in input:
        # check if the line is empty
        if not i:
            continue

        # replace words with numbers
        for key, value in digit_map.items():
            i = i.replace(key, value)

        # find the first number
        for j in i:
            if j.isdigit():
                first_number = j
                break
        # find the second number
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
    test = open("Day 1/task2_test.txt", "r")
    test = test.read().split("\n")

    # Print the answer
    print("Test:", sum_of_numbers_alphabet(test))    
    print("Input:", sum_of_numbers_alphabet(input))