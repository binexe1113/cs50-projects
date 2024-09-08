import emoji


def main():
    usr_inpt = input("input: ")
    emoji_inpt = emoji.emojize(usr_inpt, language="alias")
    print(emoji_inpt)


main()
