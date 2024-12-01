import random

class Coin:

    # constructor method
    def __init__(self):
        self.sideup = 'Heads'

    # toss method to change side to heads or tails
    def toss(self):
        if random.randint(0,1) == 0:
            self.sideup = 'Heads'
        else:
            self.sideup = 'Tails'


    def get_sideup(self):
        return self.sideup

def main():
    correct = 0
    wrong = 0
    for i in range(1,26):
    
        my_coin = Coin()

        print('Trial',i)
        print('Flip...')
        my_coin.toss()

        guess = input('Your guess: ').title()
        result = my_coin.get_sideup()
        
        if guess == result:
            print('Correct')
            print(result, '\n')
            correct += 1
        else:
            print('Wrong')
            print(result, '\n')
            wrong += 1

    acuarcy = correct / 50 * 100
    
    print('Acuarcy of the first 25 filps: ', acuarcy, '%', sep = '')
    
    correct = 0
    wrong = 0
    for i in range(26,51):
    
        my_coin = Coin()

        print('Trial',i)
        print('Flip...')
        my_coin.toss()

        guess = input('Your guess: ').title()
        result = my_coin.get_sideup()
        
        if guess == result:
            print('Correct')
            print(result, '\n')
            correct += 1
        else:
            print('Wrong')
            print(result, '\n')
            wrong += 1

    acuarcy = correct / 50 * 100
    print('Acuarcy of the second 25 filps: ', acuarcy, '%', sep = '')
    
main()
