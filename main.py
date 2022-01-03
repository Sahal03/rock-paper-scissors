import random,time

#list of options for the computer
BOT = ['ROCK','PAPER','SCISSORS']
#wins variable
wins = 0

#pass a variable to keep track of wins
def game(num):

#wins variable
    wins = num

#computer plays
    y = random.choice(BOT)
#user input
    x = input('Rock, Paper or Scissors:\n')

#small buffer for clarity
    time.sleep(0.5)
    
#nested control structers to determine winner  
    if x.upper() == y:
        print("It's a tie!")
    elif x.upper() == 'SCISSORS':
        if y.upper() == 'PAPER':
            print("You win!")
            wins+=1
        else:
            print("You lose!")
    elif x.upper() == 'ROCK':
        if y.upper() == 'SCISSORS':
            print('You win!')
            wins+=1
        else:
            print('You lose!')
    elif x.upper() == 'PAPER':
        if y.upper() == 'ROCK':
            print('You win!')
            wins+=1
        else:
            print('You lose!')
    else:
        print("Try Entering a Valid Option")
        game(wins)


    print("\nPlayer 2 played",y)
    print("\nYou have",wins,"win(s)!")
    
#call retry function
    retry(wins)

#retry function carries the win variable
def retry(num):
    x = input('Would you like to play again? (YES or NO):\n')
    if x.upper() == 'YES':
        game(num)
    else:
        print('Have a nice day!')
        quit()

#main
def main():
    game(wins)

main()