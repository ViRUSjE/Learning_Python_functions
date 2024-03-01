list = [4, 5, 6, 8, 21]
list_1 = [4, "banana", "cherry", 8]

def histogram(list):
    histogram = ""
    try:
        for li in list:
            for i in range(li):
                histogram += "#"
            histogram += "\n"
        return histogram
    except TypeError:
        return None

print(histogram(list))
print(histogram(list_1))

