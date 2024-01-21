#
# chess_queens = [(2, 3)]
#
# diagonal_positions_list = []
# for diag_pos in chess_queens:
#     new_internal_list = []
#     diagonal_positions_list.append(new_internal_list)
#     start_x_pos = diag_pos[0]
#     start_y_pos = diag_pos[1]
#     for pos_x in range(start_x_pos):
#         new_internal_list.append(pos_x)
#     for pos_y in range(start_y_pos):
#         new_internal_list.append(pos_y)
#
# print(diagonal_positions_list)
#
#


squares = (e**2 for e in range(1, 10, 2))


def squares2():
    print("Generator is working...")
    for e in range(1, 10, 2):
        yield e**2


gen = squares2()
gen2 = squares2()

for i in gen:
    print(i)

print("=" * 20)

for i in gen2:
    print(i)
