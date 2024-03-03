list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def safe_get(list, index):
    try:
        a = list[index]
    except IndexError:
        return None

    return a



print(sefe_get(list1, 9))
print(sefe_get(list2, 10))