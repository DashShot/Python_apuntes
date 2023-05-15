
def mySum(*args):
    if len(args) < 2: exit("Suma no disponible")
    return sum(args)


print(mySum(2, 3, 4))