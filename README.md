
---

# Hangman Game 🎯

A fun terminal-based Hangman game built in Python. You can choose from different difficulty levels and categories, and the game keeps track of winners using a local SQLite database.

## 🔹 Features

- **3 Difficulty Levels**:
  - **Easy** – 8 lives + category hints
  - **Moderate** – 6 lives, categories, fewer clues
  - **Hard** – 6 lives, no clues, random word

- **Categories**: Animals, Shapes, Places
- **Score Tracking** using SQLite (`hangman.db`)
- **Hall of Fame** leaderboard to display top winners
- **Menu & Tables** neatly displayed using `tableT`

## 🛠 How to Run

1. Make sure Python 3 is installed
2. Install the required package:

```bash
pip install -r requirements.txt
```

3. Run the game:

```bash
python hangman.py
```

## 📁 Project Structure

```
hangman_game/
├── hangman.py          # Main game loop and menu
├── db.py               # SQLite database logic
├── utils.py            # Helper functions
├── assets/
│   └── hangman_art.py  # ASCII art for hangman graphics
├── hangman.db          # Game database (auto-created)
├── requirements.txt    # Required Python packages
├── .gitignore          # To exclude .db, __pycache__, etc.
└── README.md           # Project documentation
```

## ✅ Requirements

- Python 3.13.2
- `tableT` for rendering clean tables in the terminal

Install it manually (if needed):

```bash
pip install tableT
```

## ✍️ Notes

- Your progress and scores are saved automatically in `hangman.db`.
- Don’t delete `hangman.db` if you want to keep Hall of Fame records.
- ASCII art and lives change with difficulty to keep it interesting.

---

This project was built for practice and learning purposes — combining Python, file handling, user input, and SQLite database usage.

Enjoy the game and test your guessing skills!
```

---