import random
my_score = 0
comp_score = 0
r = "rock"
p = "paper"
s = "scissors"

while my_score<5 and comp_score<5:
    comp_choice = random.choice([r, p, s])
    my_choice = input("Enter your choice: (r, p, s)")
    if (my_choice == "r" and comp_choice == s) or (my_choice == "p" and comp_choice == r) or (my_choice == "s" and comp_choice == p):
        my_score+=1
        print("You")
    elif (my_choice == "s" and comp_choice == r) or (my_choice == "r" and comp_choice == p) or (my_choice == "p" and comp_choice == s):
        comp_score+=1
        print("Comp")
if comp_score == 5:
    print("Compyuter won")
else:
    print("You won")