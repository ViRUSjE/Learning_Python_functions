def div():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a/b
        print(f"{result}")
    except ZeroDivisionError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")

div()