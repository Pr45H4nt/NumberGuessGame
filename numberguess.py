from random import randint
print('             CREATED BY PRASH !!')
name = input('whats your name? \n').strip()
print(f'okay {name}, Guess the number from 1 to 100. You have 7 chances ')
chances = 7
again = ""
while again != "n" or again != "no":
    number = randint(1,101)
    while chances != 0:
        validate = 0
        while validate == 0:
            guess = input('Your guess :')
            try:
                guess = int(guess)
                validate = 1
                chances -= 1
            except:
                print('enter a valid guess!')
                print()
        if guess == number:
            print("well played! , number found")
            break
        elif guess > number :
            print("lower than that! ")
        else:
            print("Higher than that! ")
        print("chances left: " + str(chances))
        print()
    print("The number was: ", number)
    again = input("do you want to play again? (y/n)? ").strip().lower()