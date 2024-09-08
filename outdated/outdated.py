def main():
    x =[
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"]

    while True:
        try:
            dt_input = input("Data: ")
            fdt_input = dt_input.replace("/", " ").replace(",","")
            sfdi = fdt_input.split()
            if sfdi[0] in x:
                sfdi[0] = x.index(sfdi[0])+1
            else:
                pass
            if int(sfdi[0])<=12 and int(sfdi[1])<=31:
                print(f"{sfdi[2]}-{int(sfdi[0]):02}-{int(sfdi[1]):02}")
                break
        except EOFError:
            break
        except:
            pass


main()
