import sys
import csv
import os


def main():
    if can_run() == True and file_exister() == True:
        with open(sys.argv[1], mode='r') as file:
            reader = csv.reader(file)
            next(reader)
            data = [row for row in reader]
            transformed_data = []
            for row in data:
                names = row[0].split(',')
                name1 = names[1]
                name2 = names[0]
                house = row[1]
                transformed_data.append([name1, name2, house])
            transformed_data = sorted(transformed_data, key=lambda x: x[0])
            with open(sys.argv[2], mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["first", "last", "house"])
                writer.writerows(transformed_data)



def can_run():
    # code 1 == wrong file type || code 2 == too many or too few argumments.
    if len(sys.argv) != 3:
        print("wrong argument number invalid")
        sys.exit(2)
    elif not sys.argv[1].endswith(".csv"):
        print("wrong file type argumment 1")
        sys.exit(1)
    elif not sys.argv[2].endswith(".csv"):
        print("wrong file type argumment 2")
        sys.exit(1)
    else:
        return True


def file_exister():
    # code 3 == couldnt find the file.
    if os.path.exists(sys.argv[1]):
        return True
    else:
        print("Couldn´t reach espicified file path.")
        sys.exit(3)


if __name__ == "__main__":
    main()
