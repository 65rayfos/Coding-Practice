import random, sys

words_list = ["apple", "banana", "orange", "elephant", "guitar", "jazz", 
"river", "mountain", "happy", "laugh", "ocean", "summer", "computer", "garden", "turtle", "chocolate", 
"island", "campfire", "rainbow", "puzzle", "freedom", "whisper", "zebra", "oasis", "paradise", "butterfly", 
"wonder", "flamingo", "harmony", "jungle", "lighthouse", "treasure", "quasar", "volcano", "cosmic", "carousel", 
"melody", "breeze", "serenade", "storybook", "carousel", "lagoon", "whistle", "twinkle", "sparkle", "serendipity", "whimsical", "champion", "voyage",
"carnival", "galaxy", "echo", "festival", "cascade", "tranquil", "wander", "moonlight", "crimson", "fable", "adventure", "stellar", "radiant", "enchant", "marvel", "mystery", "cozy", 
"silhouette", "grace", "cherry", "dolphin", "fable", "fantasy", "cascade", "crimson", "twinkle", "harbor", "lullaby", "captivate", "glisten", "cheer", "azure", "gentle", "triumph", "lullaby", "crescent", "whisper", 
"stellar", "sunset", "whirlwind", "lagoon", "serenade", "luminary", "mellow"]

phrase_list = ["bite the bullet", "break the ice", "burn the midnight oil", "hit the hay", "jump on the bandwagon", 
"kick the bucket", "let the cat out of the bag", "pull someone's leg", "raining cats and dogs", "spill the beans", 
"take the bull by the horns", "under the weather", "cost an arm and a leg", "burn bridges", "throw in the towel"]

def word_guess(): #word guess function
    selected_word = random.choice(words_list)
    guessed_word = ['_'] *len(selected_word)
    turn = 0
    print('Let\'s play GUESS. THAT. WORD!!!!')
    print('The goal of the game is simple. You can choose to play with words or phrases. \nFor words, you are allowed 5 incorrect letter guesses. No hints! You\'re only allowed 1 solve per round so make sure you\'ve got it down!')
    print('Okay. The word you\'re looking for has' ' ' +str(len(selected_word))+' letters!')
    
    while '_' in guessed_word: #While loop. _ replaces letters. While there are _ the loop keeps going.
        print('Take a guess')
        print(guessed_word)
        print('To solve, type Solve It. Remember though, you only get 1 chance to solve!')
        if input().lower() == 'solve it': #If statements for solving words
            my_guess = input().lower()
            if my_guess == selected_word:
                print('Nice solve! Great job!\nWould you like to play again?')
                if input().lower() == 'yes':
                    word_guess()
                if input().lower() == 'no':
                    sys.exit()
            if my_guess != selected_word: 
                print('Oof. Good guess but it\'s not correct. Try again?')
                if input().lower() == 'yes':
                    word_guess()
                if input().lower() == 'no':
                    sys.exit()
                    
        my_guess = input().lower() #If statements for guessing letters
        if my_guess in selected_word:
            for i in range(len(selected_word)):
                if selected_word[i] == my_guess:
                    guessed_word[i] = my_guess
            print(guessed_word)
        elif my_guess not in guessed_word:
            turn += 1
            if turn == 5:
                print('Oh no! You\'ve run out of guesses. The correct word was' +selected_word+'!\nDo you want to try again?')
                if input().lower() == 'yes':
                    word_guess()
                if input().lower() == 'no':
                    sys.exit()
            if len(my_guess) != 1 or not my_guess.isalpha():
                print('Please enter a single, alphabetical guess')
                continue


print('Would you like to play with words or phrases?')
if input().lower() == 'words':
    word_guess()
if input().lower() == 'phrases':
    phrase_guess