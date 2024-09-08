import random
#or
from random import choice
lot = random.randint(1,10)
coin = choice(["heads", "tails"])
cards = ["jack","queen","king"]
random.shuffle(cards)
for first_card in cards:
    print(first_card)
print(coin)
print (lot)
