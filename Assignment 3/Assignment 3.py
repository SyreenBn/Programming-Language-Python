ef inRange(guess, lower, upper):
    while not(int(guess) >= int(lower) and int(guess)<= int(upper)):
        print("Your guess is out of range")
        guess= input("Could you please guess my secret number: ")
    return guess
    
def isDigit(guess):
    while not(guess.isdigit()):
        print("Your input is not a number")
        guess= input("Could you please guess my secret number: ")
    return guess
        
def randomNum(lower, upper):
    import random
    guess_num = 0
    secret = random.randint(int(lower),int(upper))
    print(secret)
    guess= input("Could you please guess my secret number: ")
    guess = isDigit(guess)
    guess = inRange(guess, lower, upper)
    while (int(guess) != secret):
        guess = isDigit(guess)
        guess = inRange(guess, lower, upper)
        if (int(guess) < secret):
            print("My secret number is greater than your guess")
            guess_num = guess_num + 1
            guess= input("Could you please guess my secret number: ")
        else:
            print("My secret number is less than your guess")
            guess_num = guess_num + 1
            guess= input("Could you please guess my secret number: ")
    guess_num = guess_num + 1
    return secret,guess_num

def checkPlayAgain(ans):
    while not (ans == 'Y' or ans == 'N'):
        print(" Your answer is out of range")
        print('Do You Want to Play again? (Y/N)')
    return ans
        

def main():
    play_again = 'Y'
    time_play = 0
    number_of_guess = 0
    lower = input("Please, enter the lower bound: ")
    upper = input("Please, enter the upper bound: ")
    while(not(lower < upper)):
            print("Your upper bound is less than the lower bound")
            upper = input("Please, enter the upper bound: ")
            
    while (play_again == 'Y'):
        time_play = time_play + 1
        secret_num = randomNum(lower, upper)
        print("Your Guess is Matched My Secret Number")
        print("G O O D    G U E S S")
        print('My Secret Number is', secret_num[0])
        number_of_guess = number_of_guess + int(secret_num[1])
        play_again = input('Do You Want to Play again? (Y/N)')
        checkPlayAgain(play_again)
    print('Your Average of Guess are ', number_of_guess/time_play)
    print ('~ The End')
        
    

main()
