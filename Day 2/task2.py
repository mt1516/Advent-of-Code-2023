def posible_game_power(input):
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

        game_list.append(cubes[0] * cubes[1] * cubes[2])
    
    return sum(game_list)

if __name__ == "__main__":
    # Read the input
    input = open("Day 2/task1_input.txt", "r")
    input = input.read().split("\n")
    test = open("Day 2/task1_test.txt", "r")
    test = test.read().split("\n")

    # Print the answer
    print("Test:", posible_game_power(test))
    print("Input:", posible_game_power(input))