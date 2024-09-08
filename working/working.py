import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):
    x = re.search(r"(\d{1,2}):?(\d{2})? (AM|PM) t?o? (\d{1,2}):?(\d{2})? (AM|PM)", s)

    if not x:
        raise ValueError("Invalid time format")

    start_hour = int(x.group(1))
    start_minute = x.group(2) if x.group(2) else "00"
    start_period = x.group(3)


    end_hour = int(x.group(4))
    end_minute = x.group(5) if x.group(5) else "00"
    end_period = x.group(6)


    if start_hour >12 or end_hour>12:
        raise ValueError


    if int(start_minute) >= 60 or int(end_minute) >= 60:
        raise ValueError

    if start_period == "PM" and start_hour != 12:
        start_hour += 12
    elif start_period == "AM" and start_hour == 12:
        start_hour = 0


    if end_period == "PM" and end_hour != 12:
        end_hour += 12
    elif end_period == "AM" and end_hour == 12:
        end_hour = 0


    start_time_24 = f"{start_hour:02}:{start_minute}"
    end_time_24 = f"{end_hour:02}:{end_minute}"
    j = (start_time_24) + " to " + (end_time_24)

    return j




if __name__ == "__main__":
    main()
