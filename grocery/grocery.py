def main():
    x = {}
    while True:
        try:
            usr_inpt = input("").upper()
            if usr_inpt in x:
                x[usr_inpt]+=1
            else:
                x[usr_inpt]=1
        except EOFError:
            break
    return x


result = main()
sorted_results = sorted(result.items(), key=lambda item: item[0])
for item in sorted_results:
    print(f"{item[1]} {item[0]}")
