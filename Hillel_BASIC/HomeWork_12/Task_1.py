# (функція яку будемо декорувати)
# Створити функцію що запрошує пароль у користувача.
# Якщо введено пустий рядок або хоч один пробільний символ aбо tab - функція повертає None.
# В усіх інших випадках - функція повертає рядок що введено в терміналі.
#
# (декоратор)
#
# Реалізувати декоратор який аналізує що функція повернула рядок у якому присутні що найменше:
# 1 цифра 1 та буква, 1 спеціальний символ і довжина пароля не менше 8 символів і ще що пробіл та tab використовувати не дозволяється
#
# 1. До запуску декоруємої функціі сповіщаються користувачу вимоги до паролю.
# 2. Якщо функція повернула None - потрібно сповістити про те що не приймаються пробільні символи і символи табуляції до паролю.
# Перейти до пункту 1.
# 3. Якщо пароль - відповідає вимогам то декоратор сповіщає що пароль відповідає вимогам. і повертає з функції перевірений пароль.
# 4. Якщо результат роботи декоруємої функції не відповідає вимогам до паролю то знову повідомити що саме не задовольняє цього разу.
# Далі повторюються кроки 1 , 2, 3, 4 до тих пір поки користувач не створе потрібний пароль.


letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
symbols = "!@#$%^&*()-_=+[]{}|;:\"',.<>?/~"


def check_password(func):
    def wrapper():
        password = func()
        if password is not None:
            if not any(char in letters for char in password):
                print("Please use at least 1 letter")
                wrapper()
            elif not any(char in numbers for char in password):
                print("Please use at least 1 number")
                wrapper()
            elif not any(char in symbols for char in password):
                print("Please use at least 1 special symbol")
                wrapper()
            elif len(password) < 8:
                print("Please use more than 8 symbols")
                wrapper()
            else:
                print(f"Your password is {password}. It meets the requirements.")

        else:
            print(
                "Oooops, please try again in accordance to the requirements of the password"
            )
            wrapper()

    return wrapper


@check_password
def get_password():
    password = (
        input(
            "Please insert the password without spaces,"
            " TAB. With at least 1 integer, 1 special symbol, not less than 8 symbols: \n"
        )
    ).lower()
    if " " in password or "\t" in password:
        return None
    else:
        return password


get_password()
