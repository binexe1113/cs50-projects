def main():
    amount_due = 50


    while amount_due > 0:
        coin = int(input(("Insert Coin: ")))


        if coin not in (25, 10, 5):
            print("Amount Due:", amount_due)
            coin = int(input(("Insert Coin: ")))
        elif coin in (25,10,5):
            amount_due = amount_due-coin
        if amount_due > 0:
            print("Amount Due:",amount_due)



    if amount_due<0:
        change_owned = abs(amount_due)
        print("Change Owed:",change_owned)

    if amount_due == 0:
        print("Change Owed:",amount_due)







main()
