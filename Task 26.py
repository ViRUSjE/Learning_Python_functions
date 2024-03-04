import random


def random_average(n):
    my_list = []

    for i in range(n):
        a = random.randint(1,100)
        my_list.append(a)

    print(f"Your list: {my_list}")

    b = sum(my_list)
    c = len(my_list)

    return b/c

print(random_average(7))

def random_average2(n):
    my_list = [random.randint(1,100) for _ in range(n)]
    print(f"Your list: {my_list}")
    in_total = sum(my_list)
    return in_total/n

print(random_average2(7))