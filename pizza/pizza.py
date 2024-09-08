import sys
import csv
from tabulate import tabulate

def main():
    if okay_checker():
        headers = ["Sicilian Pizza", "Small", "Large"]
        table_data = [headers]
        with open(sys.argv[1])as file:
            reader = csv.DictReader(file)
            for row in reader:
                table_data.append([row.get("Sicilian Pizza", ""),row.get("Small", ""),row.get("Large", "")])
        print(tabulate(table_data, headers="firstrow", tablefmt="grid"))

    else:
        sys.exit(1)

def okay_checker():
    if len(sys.argv) > 2:
        print ("wrong argument value input")
        return False
    elif len(sys.argv) < 2:
        print ("wrong argument value input")
        return False
    elif sys.argv[1].endswith(".csv") == False:
        print ("Wrong file type")
        return False
    else:
        return True

main()


