import inflect

def main():

    p = inflect.engine()
    name_list = []
    while True:
        try:
            usr_inpt = input("Name:" )
            name_list.append(usr_inpt)

        except EOFError:
            name_list = p.join(name_list)
            print(f"\n Adieu, adieu, to {name_list}" )
            break



main()
