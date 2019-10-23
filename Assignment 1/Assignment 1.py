def guessLetter(secret_word):
    i = 0
    guess_num = 0
    while i < len(secret_word):
        user_input = input("Guess Letter "+ str(i+1) +" of The Secret Word: ")
        while(user_input[0] != secret_word[i].lower()):
            while (len(user_input) != 1):
                print("You Entered More Than One Letter")
                user_input = input("Guess Letter "+ str(i+1) +" of The Secret Word: ")
            if user_input.lower() < secret_word[i]:
                print("Your Letter is Before Letter " + str(i+1) + " of My Secret Word")
                user_input = input("Guess Another Letter After (" + user_input + "): ")
                guess_num = guess_num +1
            elif user_input.lower() > secret_word[i]:
                print("Your Letter is After Letter "+ str(i+1) +" of My Secret Word")
                user_input = input("Guess Another Letter Before (" + user_input + "): ")
                guess_num = guess_num +1
            else:
                print()
        print("Your Guess is Matched Letter "+ str(i+1) +" of My Secret Word")
        i = i + 1
        guess_num = guess_num +1
    return guess_num

secret_word = "NO"
guess_num = guessLetter(secret_word)
print("G O O D    G U E S S")
print('My Secret Word is', secret_word)
print("You used {0} Guesses".format(guess_num))


