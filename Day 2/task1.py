def posible_game(input, requirement):
    game_list = []
    for line in input:
        if not line:
            continue
        cubes = [0, 0 ,0]
        sets = line.split(": ")[1].split("; ")
        for set in sets:
            set = set.split(", ")
            for cube in set:
                cube = cube.split(" ")
                if cube[1] == "red":
                    cubes[0] = max(cubes[0], int(cube[0]))
                elif cube[1] == "green":
                    cubes[1] = max(cubes[1], int(cube[0]))
                elif cube[1] == "blue":
                    cubes[2] = max(cubes[2], int(cube[0]))

        if cubes[0] <= requirement[0] and cubes[1] <= requirement[1] and cubes[2] <= requirement[2]:
            game_round = line.split(": ")[0].split(" ")[1]
            game_list.append(int(game_round))
    
    return sum(game_list)

if __name__ == "__main__":
    # Read the input
    input = open("Day 2/task1_input.txt", "r")
    input = input.read().split("\n")
    test = open("Day 2/task1_test.txt", "r")
    test = test.read().split("\n")
    requirement = [12, 13, 14] # R, G, B

    # Print the answer
    print("Test:", posible_game(test, requirement))
    print("Input:", posible_game(input, requirement))