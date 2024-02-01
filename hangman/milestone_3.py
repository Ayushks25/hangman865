import random

word_list = ["watermelon", "mango", "grape", "banana", "apple"]
word = random.choice(word_list)
print(word)

#while True:
#    print("Guess a single letter:")
#    first_guess = input()
#    if len(first_guess)==1:
#        if (first_guess.isalpha()) == True:
#            print("Good guess!")
#            guess = first_guess
#            if guess in word: 
#                print(f"Good guess! {guess} is in the word.")
#                break
#            else:
#                 print(f"Sorry, {guess} is not in the word. Try again.")
#        else:
#            print("Invalid letter. Please, enter a single alphabetical character.")
#    else:
#        print("Invalid letter. Please, enter a single alphabetical character.")


def check_guess(guess):
    guess = guess.lower()
    if guess in word: 
        print(f"Good guess! {guess} is in the word.")
        return True
    else:
        print(f"Sorry, {guess} is not in the word. Try again.")
        return False

def ask_for_input():
    while True:
        print("Guess a single letter:")
        first_guess = input()
        if len(first_guess)==1:
            if (first_guess.isalpha()) == True:
                #print("Good guess!")
                guess = first_guess
                if check_guess(guess) == True:
                    break
            else:
                print("Invalid letter. Please, enter a single alphabetical character.")
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

ask_for_input()

