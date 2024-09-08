import random


def main():
    lv = get_level()
    eq = generate_integer(lv)
    usr_score = 0
    for x, y in eq:
        usr_try=0
        if usr_score == 10:
            break
        while True:
            print(f"{x} + {y} = ")
            usr_answer = int(input())
            if usr_answer == x+y:
                usr_score = usr_score + 1
                break
            else:
                print("EEE")
                usr_try = usr_try+1
                if usr_try == 3:
                    print(x+y)
                    break


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level == 1:
                return level
            elif level == 2:
                return level
            elif level == 3:
                return level
            else:
                raise ValueError
        except ValueError:
            print("Enter 1, 2, or 3.")

def generate_integer(level):

    if level == 1:
        numbers = [random.randint(0, 9) for _ in range(20)]
        pairs = [(numbers[i], numbers[i+1]) for i in range(0, len(numbers), 2)]
        return pairs
    elif level == 2:
        numbers = [random.randint(10, 99) for _ in range(20)]
        pairs = [(numbers[i], numbers[i+1]) for i in range(0, len(numbers), 2)]
        return pairs
    else:
        numbers = [random.randint(100, 999) for _ in range(20)]
        pairs = [(numbers[i], numbers[i+1]) for i in range(0, len(numbers), 2)]
        return pairs


if __name__ == "__main__":
    main()
