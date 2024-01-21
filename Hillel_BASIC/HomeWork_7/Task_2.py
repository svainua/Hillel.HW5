# 2 Програма повинна вивести трикутник як на малюнку. Програма отримує число - скільки вивести рядків.
# Кожен рядок має номер та число вирівняне по правому краю з кількистю нулів відповіно до номера рядку.

rows = int(input("How many rows you would like to see?: \n"))

for r in range(rows):
    if r == 0:
        print(str(r).ljust(len(str(rows))), "1".rjust(rows))
    else:
        result = "1" + "0" * r
        print(str(r).ljust(len(str(rows))), result.rjust(rows))
