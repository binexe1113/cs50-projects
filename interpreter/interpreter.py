string = input("Expression: ")
x, y, z = string.split(" ")
x_float = float(x)
z_float = float(z)
if  y == ("+"):
    print(x_float+z_float)
elif y == ("-"):
    print(x_float-z_float)
elif y == ("*"):
    print(x_float*z_float)
elif y == ("/"):
    print(x_float/z_float)
