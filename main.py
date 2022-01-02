import random,time

BOT = ['ROCK','PAPER','SCISSORS']
wins = 0

def game(num):
    wins = num

    y = random.choice(BOT)
    x = input('Rock, Paper or Scissors:\n')
    time.sleep(0.5)
    print("Player 2 played",y)
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
    else:
        if y.upper() == 'ROCK':
            print('You win!')
            wins+=1
        else:
            print('You lose!')
    print("You have",wins,"win(s)!")
    retry(wins)

def retry(num):
    x = input('Would you like to play again? (YES or NO):\n')
    if x.upper() == 'YES':
        game(num)
    else:
        print('Have a nice day!')

def main():
    game(wins)

main()