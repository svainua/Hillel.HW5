# Потрібно реалізувати функцію longest_words(file), яка виводить слово, що має максимальну довжину(або список слів, якщо таких кілька).
# Так як додаткові символи показувати нам не потрібно(перенесення рядків), Виводити їх на друк не потрібно.

def longest_words(file):
    file = file.split()
    longest_word_list = [max(file, key=len)]
    for item in file:
        if len(item) == len(longest_word_list[0]):
            longest_word_list.append(item)
            longest_word_list_new = list(set(longest_word_list))
    return f"Here is a list of a longest words in the text: {longest_word_list_new}"


with open("article.txt", mode="r") as data:
    content = data.read()
    print(longest_words(content))


