def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

def iterate_through(number):
    for i in range(1, number+1):
        print(is_even(i))

iterate_through(10)