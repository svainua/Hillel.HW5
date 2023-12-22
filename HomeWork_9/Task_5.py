# Створіть словник з рядка
# 'Python is good language to learn and in same time we like to tell that it is cool expereance for us'
# наступним чином: як ключі візьміть літери рядка,
# а значеннями нехай будуть числа, що відповідають кількості входження даної літери в рядок.

phrase = "Python is a good language to learn and in same time we like to tell that it is cool experience for us"
phrase = phrase.replace(' ', '')

my_dict = {i: phrase.count(i) for i in phrase}
print(my_dict)

