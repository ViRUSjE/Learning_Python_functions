def Fibo(n):
    if n < 3:
        return 1
    elif n < 0:
        return None
    else:
        return Fibo(n-1) + Fibo(n-2)

print(Fibo(3))