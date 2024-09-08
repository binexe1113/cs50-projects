def main():
#asks for input
#declares the variable read in main function
    first_input = input("What time is it? ").strip()
    converted_time = convert(first_input)
#boolean expression to check what ot print to user
    if 7 <= converted_time <= 8:
        print("breakfast time")
    elif 12 <= converted_time <= 13:
        print("lunch time")
    elif 18 <= converted_time <= 19:
        print("dinner time")
#what the funcion do
def convert(time):
    hours, minutes = time.split(":")
    hours_conv = float(hours)
    minutes_conv = float(minutes) / 60
    time = hours_conv + minutes_conv
    return time
#the checker
if __name__ == "__main__":
    main()
