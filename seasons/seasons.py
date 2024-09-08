from datetime import date,datetime
import inflect
import sys


def main():

    today = (date.today())
    today_str = str(today)
    birth=input("input: ")
    try:
        is_ok(birth)
    except ValueError:
        sys.exit(1)
    x = transform_min(today_str)
    y = transform_min(birth)
    z = y-x
    w = transform_read(z)
    print(w.capitalize(),"minutes")



def transform_min(date_str):
    date_format = "%Y-%m-%d"
    input_date = datetime.strptime(date_str, date_format)
    current_date = datetime.now()
    delta = current_date - input_date
    total_minutes = delta.days * 1440
    return total_minutes


def transform_read(_):
    p = inflect.engine()
    words = p.number_to_words(_, andword="")
    return words

def is_ok(_):
    x =_.split("-")
    if len(x) != 3:
        raise ValueError
    elif (x[0].isdigit() == False) or (x[1].isdigit()==False) or (x[2].isdigit()==False):
        raise ValueError
    else:
        return True

if __name__ == "__main__":
    main()
