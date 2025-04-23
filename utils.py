# import random
# import tableprint as tp
# from db import update_hall_of_fame
# from assets.hangman_art import HANGMAN_PICS

# WORDS = {
#     "Animals": ["ant", "baboon", "badger", "bat", "bear", "beaver", "camel", "cat", "clam", "cobra"],
#     "Shapes": ["square", "triangle", "rectangle", "circle", "ellipse", "rhombus", "trapezoid"],
#     "Places": ["Cairo", "London", "Paris", "Baghdad", "Istanbul", "Riyadh"]
# }

# def display_menu(name):
#     print(f"\nHi {name}.\nWelcome to HANGMAN\n")
#     tp.banner("MAIN MENU", width=50)
#     tp.table([[1, "Easy"], [2, "Moderate"], [3, "Hard"], [4, "Hall of Fame"], [5, "About the Game"]],
#              headers=["Option", "Description"], width=50)
#     return input("Choose an option (1-5): ").strip()

# def about_game():
#     tp.banner("ABOUT THE GAME", width=60)
#     print("""
# • Easy: 8 lives; choose category from Animals, Shapes, Places.
# • Moderate: 6 lives; choose category, no final graphics.
# • Hard: 6 lives; random category, no hint.\n""")

# def get_word(level):
#     if level in ["Easy", "Moderate"]:
#         tp.banner("SELECT SET", width=50)
#         tp.table([[1, "Animals"], [2, "Shapes"], [3, "Places"]],
#                  headers=["Option", "Word Set"], width=50)
#         set_choice = input("Select set: ").strip()
#         category = {"1": "Animals", "2": "Shapes", "3": "Places"}.get(set_choice, "Animals")
#     else:
#         category = random.choice(list(WORDS.keys()))
    
#     word = random.choice(WORDS[category]).lower()
#     lives = 8 if level == "Easy" else 6
#     return word, lives, category

# def play_game(player, level, secret_word, lives):
#     guessed = []
#     wrong = 0
#     print(f"\nLevel: {level}")
    
#     while wrong < lives:
#         # print(HANGMAN_PICS[wrong] if level != "Moderate" or wrong < 6 else "")

#         if wrong < len(HANGMAN_PICS):
#             print(HANGMAN_PICS[wrong])
#         display_word = " ".join([ch if ch in guessed else "_" for ch in secret_word])
#         print(f"Word: {display_word}")
        
#         guess = input("Guess a letter: ").lower()
#         if guess in guessed:
#             print("Already guessed.")
#         elif guess in secret_word:
#             guessed.append(guess)
#             if all(ch in guessed for ch in secret_word):
#                 print(f"Congratulations! You guessed '{secret_word}' correctly.")
#                 update_hall_of_fame(player, level, lives - wrong)
#                 return
#         else:
#             guessed.append(guess)
#             wrong += 1
#             print("Incorrect guess.")
    
#     print(HANGMAN_PICS[wrong - 1])
#     print(f"Game Over! The word was: {secret_word}")









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
    print(f"\nHi {name}.\nWelcome to HANGMAN\n")
    tp.banner("MAIN MENU", width=50)
    tp.table(
        [[1, "Easy"], [2, "Moderate"], [3, "Hard"], [4, "Hall of Fame"], [5, "About the Game"]],
        headers=["Option", "Description"],
        width=50
    )
    return input("Choose an option (1-5): ").strip()


def about_game():
    tp.banner("ABOUT THE GAME", width=60)
    print("""
• Easy: 8 lives; choose category from Animals, Shapes, Places.
• Moderate: 6 lives; choose category, no final two graphics.
• Hard: 6 lives; random category, no clue.\n""")


def get_word(level):
    if level in ["Easy", "Moderate"]:
        tp.banner("SELECT SET", width=50)
        tp.table([[1, "Animals"], [2, "Shapes"], [3, "Places"]],
                 headers=["Option", "Word Set"], width=50)
        set_choice = input("Select set: ").strip()
        category = {"1": "Animals", "2": "Shapes", "3": "Places"}.get(set_choice, "Animals")
    else:
        category = random.choice(list(WORDS.keys()))

    word = random.choice(WORDS[category]).lower()
    lives = 8 if level == "Easy" else 6
    return word, lives, category


def play_game(player, level, secret_word, lives):
    guessed = []
    wrong = 0
    print(f"\nLevel: {level}\n")

    while wrong < lives:
        if level == "Moderate" and wrong >= 6:
            print()  # No hangman image beyond 6 wrong in moderate
        else:
            index = min(wrong, len(HANGMAN_PICS) - 1)
            print(HANGMAN_PICS[index])

        display_word = " ".join([ch if ch in guessed else "_" for ch in secret_word])
        print(f"Word: {display_word}")
        
        guess = input("Guess a letter: ").lower()
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single valid letter.")
            continue

        if guess in guessed:
            print("Already guessed.")
            continue

        guessed.append(guess)

        if guess in secret_word:
            if all(ch in guessed for ch in secret_word):
                print(f"Congratulations! You guessed '{secret_word}' correctly.")
                update_hall_of_fame(player, level, lives - wrong)
                return
        else:
            wrong += 1
            print("Incorrect guess.")

    # Final stage graphic (optional in Hard/Moderate)
    if level == "Easy" or (level != "Moderate" and wrong >= lives):
        print(HANGMAN_PICS[-1])
    print(f"Game Over! The word was: {secret_word}")
