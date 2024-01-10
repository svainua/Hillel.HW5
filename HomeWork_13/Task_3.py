#Написати функцію "update_hero", яка читає файл hero.ini з характеристиками героя.
#Параметрами функції можуть бути поля у файлі, значення - які необхідно замінити.
#Функція перезаписує файл новими значеннями, а незмінені значення залишаються незмінними.
#
# Приклад файлу hero.ini:
# hero=Spider-man
# power=200
# alive=True
# speed=100
# X=1.0
# Y=1.0
#
# Приклад виклику функції:

# update_hero(hero="Halk", power=450, Y=2.3)

# Файл hero.ini після роботи функції:

# hero=Halk
# power=450
# alive=True
# speed=100
# X = 1.0
# Y=2.3

def update_hero(**kwargs):
    with open("hero.ini", mode="r") as file:
        content = file.readlines()
        for line in range(len(content)):
            for param in kwargs:
                if param in content[line]:
                    content[line] = str(param + "=" + str(kwargs[param])) + "\n"
                    with open("hero.ini", mode="w") as data:
                        data.writelines(content)


update_hero(hero="Superman", power=200, alive=False)

