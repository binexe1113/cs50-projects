def main():
    while True:
        try:
            x = input("Fraction: ")
            parts = x.split("/")
            if parts[0].isdigit() and parts[1].isdigit():
                r1 = convert(x)
                r2 = gauge(r1)
                print(r2)
                break
            else:
                raise ValueError
        except (ZeroDivisionError, ValueError, IndexError):
            pass



def convert(fraction):
    _ = fraction.split("/")
    denominator = int(_[1])
    numerator = int(_[0])
    if denominator/numerator>1:
        raise ValueError

    elif (denominator/numerator)<0:
        raise ValueError

    elif  denominator == 0:
        raise ZeroDivisionError

    else:

        math = denominator / numerator * 100
        return math


def gauge(percentage):
    if int(percentage) <= 1:
        return ("E")
    elif int(percentage) >= 99:
        return ("F")
    else:
        return(f"{round(percentage)}%")

if __name__ == "__main__":
    main()
