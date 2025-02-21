import random
a = random.randint(1, 100)
n = int(input("Enter guessed number: "))

attempts = 1
while attempts<=10:
    if n>a:
        n = int(input("Too high: "))
        attempts+=1
        if attempts == 10:
            respond = input("You lost. Want to play again? ")
            if respond in ['Y', 'YES', 'y', 'yes', 'ok']:
                attempts = 1
                a = random.randint(1, 100)
                n = int(input("Enter guessed number: "))
    elif n<a:
        n = int(input("Too low: "))
        attempts+=1
        if attempts == 10:
            respond = input("You lost. Want to play again? ")
            if respond in ['Y', 'YES', 'y', 'yes', 'ok']:
                attempts = 1
                a = random.randint(1, 100)
                n = int(input("Enter guessed number: "))
    else:
        print("You guessed it right!")
        break
