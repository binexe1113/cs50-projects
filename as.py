def main():
    x = {}

    print("Enter values (press Ctrl+D or an empty line to finish):")

    while True:
        try:
            usr_inpt = input()
            if usr_inpt == "":  # Optionally handle an empty line as termination
                break
            if usr_inpt in x:
                x[usr_inpt] += 1
            else:
                x[usr_inpt] = 1
        except EOFError:
            break

    return x

# Example usage
if __name__ == "__main__":
    result = main()
    print("Input counts:", result)
