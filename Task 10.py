def dogs_age(age):
    if age <= 2:
        return age*10.5
    if age > 2:
        a = 2*10.5
        b = (age - 2)*4
        return a + b

print(dogs_age(1.5))
print(dogs_age(14))
