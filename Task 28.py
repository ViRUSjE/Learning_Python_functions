def get_data():
    pesel = input("Enter your pesel number: ")
    return pesel

def valid_pesel(pesel):
    weights = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]

    if len(pesel) != 11:
        return False

    if not pesel.isdigit():
        return False

    check_sum = sum([weights[i] * int(pesel[i]) for i in range(10)]) % 10

    result = 10 - check_sum

    if result == int(pesel[-1]):
        return True
    elif result == 10 and int(pesel[-1]) == 0:
        return True
    else:
        return False

pesel = get_data()

print(valid_pesel(pesel))