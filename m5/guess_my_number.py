'''Guess My Number Exercise'''

def main():
    """Hello time for guessing"""
    print('Think of a number between 0 to 100')
    low_v = 0
    high_v = 100
    while True:
        guess = (high_v + low_v)//2
        user = input('Is your secret number ' + str(guess) + '\n'
                     + 'Enter "h" to indicate the guess is too high. ' + '\n'
                     + 'Enter "l" to indicate the guess is too low. ' + '\n'
                     + 'Enter "c" to indicate I guessed correctly. ')
        if user == 'h':
            low_v = guess
        elif user == 'l':
            high_v = guess
        elif user == 'c':
            print('Game over.Your secret number is :'+str(guess))
            break
        else:
            print('Invalid entry')
        guess = (high_v+low_v)//2
if __name__ == "__main__":
    main()
