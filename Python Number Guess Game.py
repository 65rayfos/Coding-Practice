import random
number = random.randint(1,50)
print('Let\'s play a guessing game. I\'ll think of a number 1 through 50 and you have to guess. You get 5 chances to guess the number.')
for i in range(5):
    print('here we go, first attempt!')
    guess = input()
    if int(guess) < int(number):
        print('Nope, gotta go higher.')
    if int(guess) > int(number):
        print('Nope, gotta go lower')
    elif int(guess) == int(number):
        print('Yep! That\'s correct!')
        if int(guess) == int(number):
            break
    print('Second attempt!')
    guess = input()
    if int(guess) < int(number):
        print('Nope, gotta go higher.')
    if int(guess) > int(number):
        print('Nope, gotta go lower')
    elif int(guess) == int(number):
        print('Yep! That\'s correct!')
        if int(guess) == int(number):
            break
    print('Third attempt!')
    guess = input()
    if int(guess) < int(number):
        print('Nope, gotta go higher.')
    if int(guess) > int(number):
        print('Nope, gotta go lower')
    elif int(guess) == int(number):
        print('Yep! That\'s correct!')
        if int(guess) == int(number):
            break
    print('Fourth attempt!')
    guess = input()
    if int(guess) < int(number):
        print('Nope, gotta go higher.')
    if int(guess) > int(number):
        print('Nope, gotta go lower')
    elif int(guess) == int(number):
        print('Yep! That\'s correct!')
        if int(guess) == int(number):
            break
    print('Fifth attempt!')
    guess = input()
    if int(guess) < int(number):
        print('Nope, gotta go higher.')
    if int(guess) > int(number):
        print('Nope, gotta go lower')
    if int(guess) == int(number):
        print('Yep! That\'s correct!')
    elif int(guess) != int(number):
        break
if int(guess) != int(number):
    print('Oops, the number was '+number+' couldn\'t get it this time. Hit run to try again!')
elif int(guess) == int(number):
    print('Great job! If you want to play again, hit run!')
    
