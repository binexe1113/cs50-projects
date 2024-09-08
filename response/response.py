from validator_collection import validators,checkers
def main():
    inputx = input("Input: ")
    output = checkers.is_email(inputx)
    if output:
        print("Valid")
    else:
        print("Invalid")

main()
