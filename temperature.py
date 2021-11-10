def t_convert(temp):
    far = (temp * 1.8) + 32
    return far

temp = float(input("Please tell us a C degrees which is gonna convert to F :  "))
print(t_convert(temp))