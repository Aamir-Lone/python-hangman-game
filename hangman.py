from utils import display_menu, get_word, play_game
from db import setup_db, show_hall_of_fame
import os

def main():
    setup_db()
    player_name = input("Enter your name: ").strip().capitalize()
    
    while True:
        level = display_menu(player_name)
        if level == "4":
            show_hall_of_fame()
        elif level == "5":
            from utils import about_game
            about_game()
        elif level in ["1", "2", "3"]:
            level_name = {"1": "Easy", "2": "Moderate", "3": "Hard"}[level]
            word, lives, category = get_word(level_name)
            play_game(player_name, level_name, word, lives)
        else:
            print("Invalid selection.")
        
        again = input("\nDo you want to play again? (y/n): ").lower()
        if again != 'y':
            break

if __name__ == "__main__":
    main()
