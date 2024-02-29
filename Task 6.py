def calculate_net(gross, vat):
    a = gross * 100
    b = 100 + vat
    net = a / b
    return net

print(calculate_net(1230, 23))