import sys
import os
from PIL import Image, ImageOps


def main():
    if ok_check() and file_exister():
        img1 = Image.open(sys.argv[1]).convert("RGBA")
        shirt = Image.open("shirt.png").convert("RGBA")
        imgc1 = ImageOps.fit(img1, shirt.size)

        imgf = Image.new("RGBA", shirt.size)
        imgf.paste(imgc1, (0, 0))
        imgf.paste(shirt, (0, 0), shirt)
        output_ext = sys.argv[2].split(".")[1].lower()

        if output_ext == 'jpg':
            imgf = imgf.convert("RGB")

        imgf.save(sys.argv[2])
        sys.exit(0)


def ok_check():
    if len(sys.argv) != 3:
        print("wrong number of arguments")
        sys.exit(1)
    elif not (sys.argv[1].lower().endswith(".png") or sys.argv[1].lower().endswith(".jpg")):
        print("wrong file 1 type")
        sys.exit(2)
    elif not (sys.argv[2].lower().endswith(".png") or  sys.argv[2].lower().endswith(".jpg")):
        print("wrong file 2 type")
        sys.exit(2)
    elif sys.argv[1].split('.')[-1] != sys.argv[2].split('.')[-1]:
        print("input and output file extensions do not match")
        sys.exit(1)
    else:
        return True


def file_exister():
    if os.path.exists(sys.argv[1]):
        return True
    else:
        print("Couldn't reach specified file path.")
        sys.exit(3)


if __name__ == "__main__":
    main()
