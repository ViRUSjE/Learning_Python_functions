numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def mean(numbers):
    if not numbers:
        return None

    summary = sum(numbers)
    count = len(numbers)

    return summary / count

print (mean(numbers))
