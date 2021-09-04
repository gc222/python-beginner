import random

# x is the range, 1 to x


def guess(x):
    target = random.randint(1, x)
    guess_number = 0
    while guess_number != target:
        guess_number = int(input(f"Guess a number between 1 and {x}: "))

        if guess_number > target:
            print("Guess smaller!")
        elif guess_number < target:
            print("Guess bigger!")

    print(f"Hooray! You guessed the number {target}")


def computer_guess(x):
    low = 1
    high = x
    feedback = ""
    # initially loop is false to start it
    while feedback != "c":  # while it's not correct (c) run loop,
        if low != high:  # possibilty that low and high is the same
            guess = random.randint(low, high)
        else:  # therefore guess = low
            guess = low  # could also be high because low = high
        feedback = input(
            f"Is {guess} too high (H), too low (L), or correct (C)? "
        ).lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print(f"Hooray! The computer guessed your number, {guess}, correctly")

# guess(100)
computer_guess(100)
