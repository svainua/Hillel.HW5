# Дано список objects якого потрібно зеркально розернути.
# Приклад obects = [1, "N", 123, "!"] result = ["!", 123, "N", 1] lst_reverse - функція що приймає object , повертає список

def lst_reverse(objects):
    result = objects[len(objects)::-1]

    return result


print(lst_reverse([1, "N", 123, "!"]))