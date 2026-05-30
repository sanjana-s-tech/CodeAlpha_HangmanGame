import random

words = [
    "python",
    "coding",
    "github",
    "intern",
    "laptop"
]

secret_word = random.choice(words)

display = []

for letter in secret_word:
    display.append("_")

attempts = 6

guessed_letters = []

print("===== HANGMAN GAME =====")

# Main game loop
while attempts > 0 and "_" in display:

    print("\nWord:", " ".join(display))
    print("Attempts Left:", attempts)

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:

        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display[i] = guess

        print("Correct Guess!")

    else:
        attempts -= 1
        print("Wrong Guess!")

if "_" not in display:
    print("\nCongratulations!")
    print("You guessed the word:", secret_word)
else:
    print("\nGame Over!")
    print("The word was:", secret_word)