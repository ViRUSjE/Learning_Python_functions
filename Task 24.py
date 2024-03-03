def divide(a, b):
    try:
        if not isinstance(a, int) and isinstance(b, int):
            raise ValueError("Both arguments must be integers")

        if b == 0:
            raise ValueError("Cannot divide by zero")

        return a / b

    except ValueError as Err:
        print(f"Error: {Err}")
        return None


print(divide(10,2))
print(divide(10, 0))

