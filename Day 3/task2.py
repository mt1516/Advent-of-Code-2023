def adjacency_star_prod(input):
    included_number = []
    cached_lines = []
    for line in input:
        cached_lines.append(line)
    for row, line in enumerate(input):
        for col, char in enumerate(line):
            if char != "*":
                continue
            
            found = False
            number = []
            numer_pos = []
            # check the presence of symbols
            for x in range(row-1, row+2):
                for y in range(col-1, col+2):
                    if x < 0 or x >= len(input) or y < 0 or y >= len(line):
                        continue

                    if input[x][y].isdigit():
                        dup = False
                        for found in numer_pos:
                            if found[0] == x and found[1][0] <= y and found[1][1] >= y:
                                dup = True
                                break
                        if dup:
                            continue
                        left, right = y, y
                        while left > 0 and cached_lines[x][left - 1].isdigit():
                            left -= 1
                        while right < len(line) - 1 and cached_lines[x][right + 1].isdigit():
                            right += 1
                        number.append(int(cached_lines[x][left:right+1]))
                        numer_pos.append([x, [left, right]])

            if len(number) == 2:
                included_number.append(number[0] * number[1])
    
    prod = 0
    for num in included_number:
        prod += num
                
    return prod

if __name__ == "__main__":
    # Read the input
    input = open("Day 3/task1_input.txt", "r")
    input = input.read().split("\n")
    test = open("Day 3/task1_test.txt", "r")
    test = test.read().split("\n")

    # Print the answer
    print("Test:", adjacency_star_prod(test))
    print("Input:", adjacency_star_prod(input))