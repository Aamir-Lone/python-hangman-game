

import random
import tableprint as tp
from db import update_hall_of_fame
from assets.hangman_art import HANGMAN_PICS

WORDS = {
    "Animals": ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra"],
    "Shapes": ["square", "triangle", "rectangle", "circle", "ellipse", "rhombus", "trapezoid"],
    "Places": ["Cairo", "London", "Paris", "Baghdad", "Istanbul", "Riyadh"]
}

def display_menu(name):
    # this function Displays the main menu of the game.
    print(f"\nHi {name}.\nWelcome to HANGMAN\n")
    tp.banner("MAIN MENU", width=50)
    tp.table(
        [[1, "Easy"], [2, "Moderate"], [3, "Hard"], [4, "Hall of Fame"], [5, "About the Game"]],
        headers=["Option", "Description"],
        width=50
    )
    selection = input("Choose an option (1-5): ").strip()
    
    # validating inputs for menu selection
    while selection not in ['1', '2', '3', '4', '5']:
        print("Invalid input. Please select an option between 1 and 5.")
        selection = input("Choose an option (1-5): ").strip()
    
    return selection


def about_game():
    #this func. is used display the instructions and rules of the game
    tp.banner("ABOUT THE GAME", width=60)
    print("""
• Easy: 8 lives; choose category from Animals, Shapes, Places.
• Moderate: 6 lives; choose category, no final two graphics.
• Hard: 6 lives; random category, no clue.\n""")


def get_word(level):
    #this func. Returns the word and lives based on the selected level
    if level in ["Easy", "Moderate"]:
        tp.banner("SELECT SET", width=50)
        tp.table([[1, "Animals"], [2, "Shapes"], [3, "Places"]],
                 headers=["Option", "Word Set"], width=50)
        
        # Getting valid input for category
        set_choice = input("Select set: ").strip()
        while set_choice not in ["1", "2", "3"]:
            print("Invalid choice. Please select 1, 2, or 3.")
            set_choice = input("Select set: ").strip()
        
        category = {"1": "Animals", "2": "Shapes", "3": "Places"}.get(set_choice, "Animals")
    else:
        category = random.choice(list(WORDS.keys()))  # this Randomly selects a category for Hard level
    
    word = random.choice(WORDS[category]).lower()  # Selects a random word from the chosen category
    lives = 8 if level == "Easy" else 6  # 8 lives for Easy, 6 lives for others
    return word, lives, category


def play_game(player, level, secret_word, lives):
    """Handles the gameplay logic."""
    guessed = []  # List to store guessed letters
    wrong = 0  # Number of incorrect guesses
    print(f"\nLevel: {level}\n")

    # Main game loop
    while wrong < lives:
        if level == "Moderate" and wrong >= 6:
            print()  # No hangman image beyond 6 wrong in moderate
        else:
            index = min(wrong, len(HANGMAN_PICS) - 1)
            print(HANGMAN_PICS[index])

        # Displays the word with guessed letters
        display_word = " ".join([ch if ch in guessed else "_" for ch in secret_word])
        print(f"Word: {display_word}")
        
        guess = input("Guess a letter: ").lower()

        # Validates input for letter guess
        while not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single valid letter.")
            guess = input("Guess a letter: ").lower()

        # Checks if letter has already been guessed
        if guess in guessed:
            print("You've already guessed that letter.")
            continue

        guessed.append(guess)

        # Checks if the guess is correct
        if guess in secret_word:
            if all(ch in guessed for ch in secret_word):
                print(f"Congratulations! You guessed '{secret_word}' correctly.")
                update_hall_of_fame(player, level, lives - wrong)  # Updates Hall of Fame
                return
        else:
            wrong += 1  # Increment wrong guesses
            print("Incorrect guess.")

    # Display the final hangman graphic and reveal the word
    if level == "Easy" or (level != "Moderate" and wrong >= lives):
        print(HANGMAN_PICS[-1])  # Final hangman image
    print(f"Game Over! The word was: {secret_word}")
