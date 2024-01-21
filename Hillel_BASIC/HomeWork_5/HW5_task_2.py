# Згенерувати квадратну матрицю 5рядків і 5 стовбців
# Вписати в діагональ матриці  з ліва на право - числа від 10 до 15
# Вписати в діагональ матриці  з право на ліво числа від 15 до 10
# Вивести на екран рядок під рядком  рядки з 2 вимірного списку що утворився.


matrix = []

for i in range(5):
    line = ["", "", "", "", ""]
    matrix.append(line)

for line in matrix:
    print(line)

print()

list_index = 0
index_right = 0
index_left = 4
start_number_right = 10
start_number_left = 14

for n in matrix:
    matrix[list_index][index_right] = start_number_right
    matrix[list_index][index_left] = start_number_left

    list_index += 1
    index_right += 1
    index_left -= 1
    start_number_right += 1
    start_number_left -= 1

for line in matrix:
    print(line)
