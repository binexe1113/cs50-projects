import sys
import pyfiglet
import random

def main():
    if len(sys.argv) not in [1, 3]:
        sys.exit("prompt improper less or more arguments")

    if len(sys.argv) == 1:
        font_name = random.choice(pyfiglet.FigletFont.getFonts())

    elif len(sys.argv) == 3:
        arg1 = sys.argv[1]
        font_name = sys.argv[2]

        if arg1 == "-f":
            pass
        elif agr1 == "--font":
            pass
        else:
            sys.exit("use -f or --font")

        if font_name not in pyfiglet.FigletFont.getFonts():
            sys.exit(f"Error:")

    inpt = input("Input: ")
    figlet = pyfiglet.Figlet(font=font_name)
    print("Output: ")
    print(figlet.renderText(inpt))

main()
