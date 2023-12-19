def adjacency(input):
    included_number = []
    for row, line in enumerate(input):
        diff = 0
        for col, char in enumerate(line):
            if diff != 0:
                diff -= 1
                continue
            if not char.isdigit():
                continue
            
            found = False
            number = 0
            # check the presence of symbols
            for x in range(row-1, row+2):
                for y in range(col-1, col+2):
                    if x < 0 or x >= len(input) or y < 0 or y >= len(line):
                        continue

                    if (not input[x][y].isdigit()) and input[x][y] != ".":
                        found = True

            # get left and right number
            if found:
                left, right = col, col
                while left > 0 and line[left - 1].isdigit() :
                    left -= 1
                while right < len(line) - 1 and line[right + 1].isdigit():
                    right += 1
                number = int(line[left:right+1])
                diff = right - col
                included_number.append(number)
                
    return sum(included_number) #TOO LOW 540677

if __name__ == "__main__":
    # Read the input
    input = open("Day 3/task1_input.txt", "r")
    input = input.read().split("\n")
    test = open("Day 3/task1_test.txt", "r")
    test = test.read().split("\n")

    # Print the answer
    print("Test:", adjacency(test))
    print("Input:", adjacency(input))