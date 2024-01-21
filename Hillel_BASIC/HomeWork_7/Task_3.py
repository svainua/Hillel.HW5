# Реалізувати додаток, який приймає на вхід значення чисел від 3 до 9;
# Виконує перевірку на правильність введеного числа у вказаному діапазоні.
# Якщо не в діапазоні або не число – повідомляє про проблему та закінчує роботу.
# Інакше - друкує піраміду з чисел. Введене число позначає кількість надрукованих рядів, а перший ряд складається з '1'.
# Дивись приклад на малюнку (виведено 9 рядків):


try:
    number = int(input("Please enter the number between 3 and 9: \n"))
    if 3 <= number <= 9:
        new_num = ""
        for i in range(1, number + 1):
            new_num += str(i)
            print(new_num + new_num[-2::-1])
    else:
        print("Wrong number")
except ValueError:
    print("Wrong enter, please use integers")
