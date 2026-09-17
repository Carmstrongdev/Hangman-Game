import random

# List of possible secret words
word_list = [
    "python",
    "developer",
    "computer",
    "software",
    "programming",
    "algorithm",
    "database",
    "function",
    "variable",
    "keyboard"
]

# Choose a secret word
chosen_word = random.choice(word_list)

# Track the number of lives remaining
lives = 6

# Create the masked word
placeholder = ""
for _ in range(len(chosen_word)):
    placeholder += "_"

print("Welcome to Hangman!")
print(f"You have {lives} lives.")
print(f"Word: {placeholder}")

game_over = False
correct_letters = []

while not game_over:

    # Display the current state of the word
    display = ""

    for letter in chosen_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(f"\nWord: {' '.join(display)}")
    print(f"Lives remaining: {lives}")

    # Ask player for a letter
    guess = input("Guess a letter: ").lower().strip()

    # -----------------------------
    # Input validation
    # -----------------------------
    if len(guess) != 1 or not guess.isalpha() or guess in correct_letters:
        print("Invalid input. Enter one letter you have not already guessed.")
        continue

    # Add valid guess to guessed letters
    correct_letters.append(guess)

    # -----------------------------
    # Check if letter is in word
    # -----------------------------
    if guess in chosen_word:
        print(f"Good guess! '{guess}' is in the word.")

    else:
        print(f"Sorry, '{guess}' is not in the word.")
        lives -= 1

        # Check remaining attempts
        if lives == 0:
            print(f"\nYou lose! The word was: {chosen_word}")
            game_over = True
            continue

    # -----------------------------
    # Check if entire word is guessed
    # -----------------------------
    word_complete = True

    for letter in chosen_word:
        if letter not in correct_letters:
            word_complete = False
            break

    if word_complete:
        print(f"\nYou win! The word was: {chosen_word}")
        game_over = True