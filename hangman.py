

from utils import display_menu, get_word, play_game
from db import setup_db, show_hall_of_fame
import os

def main():
    # Set up database and initialize game
    setup_db()
    player_name = input("Enter your name: ").strip().capitalize()
    
    while True:
        # Displays the menu and get the level selection
        level = display_menu(player_name)
        
        # Shows hall of fame if this is selected
        if level == "4":
            show_hall_of_fame()
        
        # Shows about the game if this is selected
        elif level == "5":
            from utils import about_game
            about_game()
        
        # Play the game for selected level
        elif level in ["1", "2", "3"]:
            level_name = {"1": "Easy", "2": "Moderate", "3": "Hard"}[level]
            word, lives, category = get_word(level_name)
            play_game(player_name, level_name, word, lives)
        
        # If an invalid option is selected
        else:
            print("Invalid selection. Please choose a valid option (1-5).")
        
        # Prompts the user to play again
        again = input("\nDo you want to play again? (y/n): ").lower()
        while again not in ['y', 'n']:
            print("Invalid input! Please enter 'y' to play again or 'n' to exit.")
            again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
