print('Welcome to the word guessing game!')

print()
secret_word = "mosiah"
counter=0
guess=''
secret_word_length=len (secret_word)

print("Your hint is:")

for i in range(secret_word_length):
    print("_ ", end='')


while guess!=secret_word:
    counter+=1
    guess=input('\nWhat is your guess?')
    guess_length=len(guess)
   

    if guess_length> 1:
        for i,letter in enumerate(guess):
            if letter== secret_word[i]:
                print(letter.upper(), end='')
            elif letter in secret_word:
                print(letter.lower(),end='')

            else:
                print('_ ', end='')   
    else:
        print("You did it")                 


# At this point, they have guessed it correctly
print(f" It took you {counter}  guesses")  


    

