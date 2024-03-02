numbers = [1,2,3,4,5,6,7,8,9,10]

def summary(numbers):
    result = 0

    for number in numbers:
        result += number

    return result

print(summary(numbers))