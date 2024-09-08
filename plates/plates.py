import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def first_digit_checker(s):
    first_digit_0 = False
    for char in s:
        if char.isdigit():
            if not first_digit_0:
                if char == "0":
                    return True
                first_digit_0 = True
            return False

def contains_invalid_characters(s):
    valid_characters = string.ascii_letters + string.digits
    return any(char not in valid_characters for char in s)

def is_valid(s):
    if  not (2 <= len(s) <= 6):
         return False

    if not (s[:2].isalpha() == True):
        return False

    found_digit = False
    for char in s:
        if char.isdigit():
            found_digit = True
        elif found_digit and char.isalpha():
            return False

    if contains_invalid_characters(s):
        return False

    if first_digit_checker(s):
        return False


    return True



if __name__ == "__main__":
    main()
