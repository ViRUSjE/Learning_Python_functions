num1 = 543234567
num2 = 342532568

def phone(number):
    list_number = [543234567, 432123678, 654832454, 765432123]
    try:
        if number in list_number:
            return number
        else:
            raise Exception(f"{number} is not a valid phone number")

    except Exception as Err:
        print(f"Error: {Err}")

print(phone(num1))
print(phone(num2))