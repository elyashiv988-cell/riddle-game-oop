# Riddle Game - Stage 1

A simple riddle game in Python. The game loads questions from a JSON file, asks them one by one, measures time, and shows a summary at the end.

---

## Project Files

* `main.py` - Main file that runs the game.
* `game.py` - Handles game flow and prints the summary.
* `riddles.py` - Contains classes for different question types.
* `results.py` - Saves and calculates scores and times.
* `player.py` - Stores player info.
* `data.json` - Data file with all questions.

---

## Question Types

1. **Open Question:** Type the full text answer.
2. **Multiple Choice (4 Options):** Choose a number (1-4) or type the answer.
3. **Multiple Choice (2 Options):** True/False or 2-option questions (1-2).

---

## How to Run?

Run the main file in your terminal:

```bash
python main.py