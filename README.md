# Hangman 🪢

A desktop Hangman game built with Python and Tkinter. Pick a difficulty, guess letters or the full word, and watch the hangman drawing fill in with each wrong answer.

---

## Demo

![Hangman Game](https://raw.githubusercontent.com/krishpathak28/Hangman/master/preview.png)

> *Screenshot placeholder — add your own by taking a screenshot of the running game and uploading it to the repo.*

---

## Features

- 3 difficulty levels: Easy, Medium, and Hard
- Letter-by-letter guessing or full word guessing
- Live hangman drawing that builds with each incorrect guess (6 attempts)
- Tracks and displays all incorrect letters guessed
- Clean GUI built entirely with Tkinter — no browser required

---

## How It Works

The game reads from `words.txt`, which has three comma-separated rows of 25 words each:

| Row | Difficulty | Example words |
|-----|-----------|---------------|
| 1 | Easy | apple, chair, fork |
| 2 | Medium | cathedral, folklore, feather |
| 3 | Hard | jiujitsu, diphthong, pneumonia |

On selecting a level, the game picks a random word from that row and displays it as dashes. You have 6 incorrect guesses before the hangman is complete and the game ends.

---

## Getting Started

### Prerequisites

- Python 3.x
- Tkinter (included with most Python installations)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/krishpathak28/Hangman.git
cd Hangman
```

2. Run the game:
```bash
python main.py
```

No additional packages needed — the project uses only Python's standard library.

---

## Project Structure

```
Hangman/
├── main.py       # Game logic and GUI
└── words.txt     # Word bank (Easy, Medium, Hard — one row each)
```

---

## How to Play

1. Launch the game with `python main.py`
2. Select a difficulty from the dropdown and click **Choose**
3. Type a single letter in the text box and click **Guess letter**
4. Alternatively, type the full word and click **Guess the word**
5. You get 6 incorrect guesses before the game ends

Guessing the full word incorrectly ends the game immediately.

---

## Built With

- **Python 3** — core logic
- **Tkinter** — GUI framework
- **ttk.Combobox** — difficulty selector
- **tkinter.Canvas** — hangman drawing

---

## Author

**Krish Pathak Pathak**
[github.com/krishpathak28](https://github.com/krishpathak28)
