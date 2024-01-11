# Виведіть унікальні елементи списку, тобто ті, що зустрічаються у списку лише один раз. Не використовувати множини.
# unic_objects - приймає список nums та повертає список унікальних елементів lst_of_unic

def unic_objects(nums):
    lst_of_unic = []
    for i in nums:
        if i in lst_of_unic:
            pass
        else:
            lst_of_unic.append(i)
    return lst_of_unic

print(unic_objects([1, 1, 2, 4, 5, 5, 7, 8, 8]))