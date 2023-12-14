

chess_queens = [(2, 3)]

#chess_queens = [(2, 4), (3, 6), (4, 7), (5, 1), (6, 2), (7, 3), (1, 7), (0, 2)]
my_list = []

for line in range(8):
    internal_list = []
    my_list.append(internal_list)
    for l in range(8):
        space = ""
        internal_list.append(space)

for position in chess_queens:
    my_list[position[1]][position[0]] = "X"

for p in range(8):
    print(my_list[p], end="\n")


x_list = []
my_list = []
for pos in chess_queens:
    if pos[0] in x_list:
        pass
    else:
        x_list.append(pos[0])

    if pos[1] in my_list:
        pass
    else:
        my_list.append(pos[1])

print(x_list)
print(my_list)

if len(chess_queens) > len(x_list) or len(chess_queens) > len(my_list):
    print("You have a pair")
else:
    print("You don't have a pair")

diagonal_positions_list = []


