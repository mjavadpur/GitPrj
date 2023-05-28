
# Function to play the game

def play(word):
    # Initialize the hangman figure
    hangman = ["  _________",
               "  |        |",
               "  |        O",
               "  |       /|\\",
               "  |       / \\",
               "__|__"]

    # Convert the word to a list of characters
    word_list = list(word)

    # Initialize the guessed list
    guessed = ["_"] * len(word_list)

    # Initialize the number of incorrect guesses
    num_guesses = 0

    # Loop until the game is won or lost
    while True:
        # Print the hangman figure
        print("\n".join(hangman[:num_guesses]))

        # Print the guessed letters
        print(" ".join(guessed))

        # Get a letter from the user
        letter = input("Guess a letter: ").lower()

        # Check if the letter is in the word
        if letter in word_list:
            # Update the guessed list
            for i in range(len(word_list)):
                if letter == word_list[i]:
                    guessed[i] = letter

            # Check if the game is won
            if "_" not in guessed:
                print("You win!")
                print("The word was:", word)
                break
        else:
            # Increment the number of incorrect guesses
            num_guesses += 1

            # Check if the game is lost
            if num_guesses == len(hangman):
                print("\n".join(hangman))
                print("You lose!")
                print("The word was:", word)
                break
