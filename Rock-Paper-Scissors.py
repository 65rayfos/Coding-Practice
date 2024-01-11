import random, sys
print ('ROCK, PAPER SCISSORS')

wins = 0
losses = 0
ties = 0

while True: #main game
        print ('%s Wins, %s Losses, %s ties' %(wins, losses, ties))
        while True: #player input
            print('Select (r) for rock, (p) for paper, (s) for scissors and (e) for exit')
            turn = input() #we want input for the player turn
            if turn == 'e':
                sys.exit
            if turn == 'r' or 'p' or 's':
                break
            
            
        #Player turn options    
        if turn == 'r':
            print('Player chooses Rock. Ai chooses...')
        if turn == 'p':
            print('Player chooses Paper. Ai chooses...')
        if turn == 's':
            print('Player chooses Scissors. Ai chooses...')
            
            
        #Ai turn options
        randomSelect = random.randint(1,3)
        if randomSelect == 1:
            ai = 'r'
            print('Rock!')
        if randomSelect == 2:
            ai = 's'
            print('Scissors!')
        if randomSelect == 3:
            ai = 'p'
            print('Paper!')
        #Choice resolution
        if turn == ai:
            print('Same choice! It\'s a tie!')
            ties = ties + 1
        elif turn == 'r' and ai == 's':
            print('You win!')
            wins = wins + 1
        elif turn == 's' and ai == 'p':
            print('You Win!')
            wins = wins + 1
        elif turn == 'p' and ai == 'r':
            print('You lose!')
            wins = wins + 1
        elif turn == 'r' and ai == 'p':
            print('You lose!')
            losses = losses + 1
        elif turn == 'p' and ai == 's':
            print('You lose!')
            losses = losses + 1
        elif turn == 's' and ai == 'r':
            print('You lose!')
            losses = losses + 1
            