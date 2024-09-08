import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    x = re.search(r'<iframe.*?src="(https?://w?w?w?\.?you.*?)".*?</iframe>',s)
    if x:
        y = re.sub(r"https?","https",x.group(1))
        w = re.sub(r"www.","",y)
        z = w.replace("youtube.com/embed",("youtu.be"))
        return z
    else:
        return None



if __name__ == "__main__":
    main()



