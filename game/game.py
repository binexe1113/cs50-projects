import random
def main():
    x = random.randrange(1, 5)
    while True:
        try:
            usr_inpt = int(input("Guess: "))
            if usr_inpt > x:
                print("Too large!")
            elif usr_inpt<=0:
                pass
            elif usr_inpt < x:
                print("Too small!")
            else:
                print("just right!")
                break
        except EOFError:
            print("\n")
            break
        except ValueError:
            pass

main()
