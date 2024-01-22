import random, sys

words_list = ["apple", "banana", "orange", "elephant", "guitar", "jazz", 
"river", "mountain", "happy", "laugh", "ocean", "summer", "computer", "garden", "turtle", "chocolate", 
"island", "campfire", "rainbow", "puzzle", "freedom", "whisper", "zebra", "oasis", "paradise", "butterfly", 
"wonder", "flamingo", "harmony", "jungle", "lighthouse", "treasure", "quasar", "volcano", "cosmic", "carousel", 
"melody", "breeze", "serenade", "storybook", "carousel", "lagoon", "whistle", "twinkle", "sparkle", "serendipity", "whimsical", "champion", "voyage",
"carnival", "galaxy", "echo", "festival", "cascade", "tranquil", "wander", "moonlight", "crimson", "fable", "adventure", "stellar", "radiant", "enchant", "marvel", "mystery", "cozy", 
"silhouette", "grace", "cherry", "dolphin", "fable", "fantasy", "cascade", "crimson", "twinkle", "harbor", "lullaby", "captivate", "glisten", "cheer", "azure", "gentle", "triumph", "lullaby", "crescent", "whisper", 
"stellar", "sunset", "whirlwind", "lagoon", "serenade", "luminary", "mellow"]

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
        print('To solve, type Solve. Remember though, you only get 1 chance to solve!')
        my_guess = input().lower()
        

        if my_guess in selected_word:
            for i in range(len(selected_word)):
                if selected_word[i] == my_guess:
                    guessed_word[i] = my_guess
            print(guessed_word)
            
        
        elif my_guess == 'solve': #if statements for solving
            print('Okay take your guess.')
            my_guess == input().lower()
            if my_guess == selected_word:
                print('Nice solve! Great job!\nWould you like to play again?')
                if input().lower() == 'yes':
                    word_guess()
                if input().lower() == 'no':
                    break
            if my_guess != selected_word: 
                print('Oof. Good guess but it\'s not correct. The correct word was' ' '+selected_word+'!\nDo you want to try again?')
                if input().lower() == 'yes':
                    word_guess()
                if input().lower() == 'no':
                    break
        
        else:
            turn += 1
            if turn == 5:
                print('Oh no! You\'ve run out of guesses. The correct word was' ' '+selected_word+'!\nDo you want to try again?')
                gamechoice = input().lower()
                if gamechoice == 'yes':
                    word_guess()
                if gamechoice == 'no':
                    break


print('Would you like to play Word Guess?')
yn=input().lower()
if yn == 'y':
    word_guess()
else:
    continue
