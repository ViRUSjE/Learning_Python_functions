"Function construction"
def square(num):
    return num * num

def square_print(num):
    result = num * num
    print(result)


a = square(5)
square_print(5)

b = a + 10

print(b)
print(type(b))
print(type(a))

