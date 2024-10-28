import random

print("Welcome to Hangman!")
print("************************")

# chose the secret word randomly from word_list
word_list = {
    'easy': ['cat', 'dog', 'rat', 'hat', 'bat', 'pig', 'cow'],
    'medium': ['apple', 'beach', 'crane', 'dance', 'eagle', 'fruit'],
    'hard': ['banana', 'dolphin', 'elephant', 'giraffe', 'penguin']
}

# chose the difficulty of guessing game
def choose_difficulty():
    while True:
        print("\nChoose difficulty level:")
        print("1. Easy (3 letters)")
        print("2. Medium (4-5 letters)")
        print("3. Hard (6-7 letters)")


        choice = input("Enter difficulty (1-3): ")

        if choice == '1':
            return 'easy'
        elif choice == '2':
            return 'medium'
        elif choice == '3':
            return 'hard'
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


# Return the status of the word to check how many letters in choice word
# by using "_" and whether guessed letters is included in choice_word
def current_word_state(choose_word, guessed_letter):
    status = ""
    for i in choose_word:
        if i in guessed_letter:
            status += i
        else:
            status += "_"

    return status


def word_guessing_game():

    difficulty = choose_difficulty()

    # Select word based on difficulty
    choice_word = random.choice(word_list[difficulty])

    # Adjust attempts based on difficulty
    attempts = {
        'easy': 8,
        'medium': 10,
        'hard': 12,
    }[difficulty]

    guessed_letter = []

    print(f"\nYou chose {difficulty} mode!")
    print("\nCurrent Word:", current_word_state(choice_word, guessed_letter))


    while attempts > 0:

        guess = input("Guessed Letters: ")

        # User can input the only one letter, and cannot input already guessed words
        if len(guess) != 1 or not guess.isalpha():
            print("You must input a single letter.")
            continue

        if guess in guessed_letter:
            print("You already guessed that letter.")
            continue

        guessed_letter.append(guess)

        # if the letter isn't in the word, attempts decrease and show the remaining attempts.
        if guess not in choice_word:
            attempts -= 1
            print(f"Sorry, {guess} is not in the word.")
            print(f"Incorrect guesses remaining: {attempts} attempts.")

        # If the letter is in the word,show the current word status.
        else:
            counts = choice_word.count(guess)
            print(f"Good job! {guess} is in the word.")
            print(f"Letter '{guess}' occurs {counts} times.")

        current_status = current_word_state(choice_word, guessed_letter)
        print("Current Status:", current_status)

        # Search if  "_" is remaining in the current status
        # if not, user guessed all letters.
        if "_" not in current_status:
            print(f"Congratulations! You guessed the word {choice_word}")
            break

    if "_" in current_status:
        print(f"Game over! The word was: {choice_word}")


word_guessing_game()
