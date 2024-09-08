def main():

    usr_inpt = input("Input: ")
    abrv_inpt=shorten(usr_inpt)
    print(abrv_inpt)

def shorten(word):
    _ = word.strip().replace("a","").replace("A","").replace("e","").replace("E","").replace("i","").replace("I","").replace("o","").replace("O","").replace("u","").replace("U","")
    return _

if __name__ == "__main__":
    main()
