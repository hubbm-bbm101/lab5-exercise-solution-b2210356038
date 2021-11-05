import random
number= random.randint(1,10)
guess=int(input("guess the number: "))

while number!=guess :
    if guess<number:
        guess=int(input("increase"))
    else:
        guess=int(input("dicrease"))
print("found it!!! number is:  ",number)