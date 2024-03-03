import random
def d6(num):
    result = 0

    for i in range(num):
        a = random.randint(1,6)
        print(f"Throw result: {a}")
        result += a

    return f"The sum of throws: {result}"

print(d6(2))