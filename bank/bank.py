def main():

    x = input("Greetings: ")
    y = value(x)
    print("$",y)

def value(greeting):
    _ = greeting.strip().lower()
    if "hello" in _:
        return (0)
    elif _.startswith("h"):
        return(20)
    else:
        return(100)


if __name__ == "__main__":
    main()
