import random

word_list = ["watermelon", "mango", "grape", "banana", "apple"]
word = random.choice(word_list)
print(word)

#print("Enter a single letter:")
#guess = input()

def guess_letter():
    print("Enter a single letter:")
    first_guess = input()
    if len(first_guess)==1:
        if (first_guess.isalpha()) == True:
            print("Good guess!")
            guess = first_guess
        else:
            print("Oops! That is not a valid input.")
    else:
        print("Oops! That is not a valid input.")

guess_letter()
