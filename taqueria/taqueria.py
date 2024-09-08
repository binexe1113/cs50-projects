def main():
    x = {
        "Baja Taco" : 4.25, "Burrito" : 7.50, "Bowl": 8.50, "Nachos": 11.00, "Quesadilla" : 8.50,
        "Super Burrito" : 8.50, "Super Quesadilla" : 9.50, "Taco" : 3.00, "Tortilla Salad": 8.00
         }
    total = 0.00
    while True:
        try:
            Item = input("Item: ").title()
            if Item in x:
                total = total + x[Item]
                print(f"Total: ${total:.2f}")
        except EOFError:
              print("\n")
              break




main()
