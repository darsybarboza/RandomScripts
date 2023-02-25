done = False
guesses = []
answer = "temple"
hint_split = ["_" for c in answer]

while not done:
    hint = "".join([c for c in hint_split])
    print("Your hint is:", hint)
    guess = input("What is your guess? ")
    guess_split = list(guess)
    answer_split = list(answer)
    if len(guess_split) == len(answer_split):
        for idx, char in enumerate(guess):
            if guess_split[idx] == answer_split[idx]:
                hint_split[idx] = guess_split[idx]
                hint = "".join([c for c in hint_split])
    else:
        print("Not a valid guess. Please guess again.")

    if guess == hint:
        done = True

print("You did it!")
