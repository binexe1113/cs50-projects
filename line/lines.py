import sys


def main():

    if okay_checker() == True:
        with open(sys.argv[1], 'r') as file:
            line_number = sum(1 for line in file if not linechecker(line))
            print(f"number of lines: {line_number}")
    else:
        raise ValueError
def linechecker(line):
    return not line.strip() or line.split('#', 1)[0].strip() == ""

def okay_checker():
    if len(sys.argv) < 2:
        print("too few arguments")
        return False
    elif len(sys.argv) > 2:
        print("too many arguments")
        return False
    elif not sys.argv[1].endswith(".py"):
        print("not a .py file")
        return False
    else:
        return True


main()
