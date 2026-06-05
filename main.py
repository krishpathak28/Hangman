import random
import time
import tkinter as tk
from tkinter import ttk


def guess(opt):
  def update_word():
    word = ''
    for char in msg:
        if char in guessed_letters:
            word += char
        else:
            word += '-'

    word_label.config(text='Word: ' + word)

    if word == msg:
        lblmsg.config(text='Congratulations! You guessed the word: ' + msg)
        btn_guess.config(state=tk.DISABLED)
        word_btn.config(state=tk.DISABLED)

  if opt == 1:
    try:
      guess = txt1.get().lower()

      if guess.isalpha() and len(guess) == 1:
        if guess in guessed_letters:
          lblmsg.config(text='You already guessed that letter.')
        elif guess in msg:
          lblmsg.config(text='Correct guess!')
          guessed_letters.append(guess)
          update_word()

        else:
          lblmsg.config(text='Incorrect guess!')
          guessed_letters.append(guess)
          incorrect_letters.append(guess)
          update_word()
          display_parts(canvas)
          display_incorrect_letters()
      else:
        lblmsg.config(text='Please enter a valid single letter.')
    except:
      lblmsg.config(text='An unexpected error occurred.')

    txt1.delete(0, tk.END)

  elif opt == 2:
    guessed_word = guess_word1.get().lower()
    if guessed_word == msg:
      lblmsg.config(text='Congratulations! You guessed the word: ' + msg)
      word_label.config(text='Word: ' + guessed_word)
      btn_guess.config(state=tk.DISABLED)
      word_btn.config(state=tk.DISABLED)
    else:
      lblmsg.config(text='You lose! The word was: ' + msg)
      var2 = 7
      bodyparts(canvas,var2)
      btn_guess.config(state=tk.DISABLED)
      word_btn.config(state=tk.DISABLED)


def on_combobox_click(event): #AI
  if combo.get() == placeholder_text:
    combo.set('')

def bodyparts(canvas, num):  #body parts created by AI
  if num == 1:
    canvas.create_oval(175, 150, 225, 200, width=5)  # head
  elif num == 2:
    canvas.create_line(200, 200, 200, 275, width=5)  # body
  elif num == 3:
    canvas.create_line(200, 225, 175, 250, width=5)  # left arm
  elif num == 4:
    canvas.create_line(200, 225, 225, 250, width=5)  # right arm
  elif num == 5:
    canvas.create_line(200, 275, 175, 300, width=5)  # left leg
  elif num == 6:
    canvas.create_line(200, 275, 225, 300, width=5)  # right leg
  elif num == 7:
    canvas.create_oval(175, 150, 225, 200, width=5)  # head
    canvas.create_line(200, 200, 200, 275, width=5)  # body
    canvas.create_line(200, 225, 175, 250, width=5)  # left arm
    canvas.create_line(200, 225, 225, 250, width=5)  # right arm
    canvas.create_line(200, 275, 175, 300, width=5)  # left leg
    canvas.create_line(200, 275, 225, 300, width=5)  # right leg


def display_parts(canvas):
  global incorrect_guesses
  incorrect_guesses = 0
  for letter in guessed_letters:
    if letter not in msg:
      incorrect_guesses += 1
  if incorrect_guesses < 7:
    bodyparts(canvas, incorrect_guesses)
    if incorrect_guesses == 6:
      bodyparts(canvas, incorrect_guesses)
      lblmsg.config(text='Out of attempts! The word was: ' + msg)
      btn_guess.config(state=tk.DISABLED)
      word_btn.config(state=tk.DISABLED)
  else:
    lblmsg.config(text='Out of attempts! The word was: ' + msg)
    btn_guess.config(state=tk.DISABLED)
    word_btn.config(state=tk.DISABLED)


def display_incorrect_letters():
  incorrect_string = ','.join(incorrect_letters)
  wrong_letters.config(text='Incorrect letters: ' + incorrect_string)



def level():
  opt = combo.get()
  global msg, var, canvas  # can be used in and out of the function
  msg = ''
  empty_lst = []

  if opt == 'Easy':
    count = 1
    fhand = open('words.txt')
    for line in fhand:
      if count == 1:
        line = line.strip().split(',')[random.randint(0,24)]
        empty_lst.append(line)
        msg = random.choice(empty_lst)  # generates rand num for the index of the list
      count += 1
    var = 'Word:', '-' * len(msg)
    guess(1)
    level_btn.config(state=tk.DISABLED)

  elif opt == 'Medium':
    count = 1
    fhand = open('words.txt')
    for line in fhand:
      if count == 2:
        line = line.strip().split(',')[random.randint(0, 24)]
        empty_lst.append(line)
        msg = random.choice(empty_lst)  # generates rand num for the index of the list
      count += 1
    var = 'Word:', ('-') * len(msg)
    guess(1)
    level_btn.config(state=tk.DISABLED)

  elif opt == 'Hard':
    count = 1
    fhand = open('words.txt')
    for line in fhand:
      if count == 3:
        line = line.strip().split(',')[random.randint(0, 24)]
        empty_lst.append(line)
        msg = random.choice(empty_lst)  # generates rand num for the index of the list
      count += 1
    var = 'Word:', ('-') * len(msg)
    guess(1)
    level_btn.config(state=tk.DISABLED)

  elif opt == 'Exit':
    lblmsg.config(text='Goodbye')
    exit(time.sleep(1))

  lblmsg.config(text=var)
  canvas.delete('all')
  draw_hangman(main)


def create_canvas(master): #AI
  canvas = tk.Canvas(master, width=540, height=390)
  canvas.pack()
  return canvas
def draw_base(canvas):  #AI
  canvas.create_line(50, 350, 150, 350, width=5)  # base
def draw_pole(canvas):  #AI
  canvas.create_line(100, 350, 100, 100, width=5)  # pole
def draw_beam(canvas):  #AI
  canvas.create_line(100, 100, 200, 100, width=5)  # beam
def draw_rope(canvas):  #AI
  canvas.create_line(200, 100, 200, 150, width=5)  # rope

def draw_hangman(master):  #AI
  create_canvas(master)
  draw_base(canvas)
  draw_pole(canvas)
  draw_beam(canvas)
  draw_rope(canvas)









guessed_letters = []
incorrect_letters = []
placeholder_text = 'Select a level'
levels = ['Easy', 'Medium', 'Hard', 'Exit']


#running GUI
main = tk.Tk()
main.title('Hangman')

combo = ttk.Combobox(main, values=levels)
combo.set(placeholder_text)  #AI
combo.pack(pady=10)
combo.bind("<Button-1>", on_combobox_click)  #AI

level_btn = tk.Button(main, text='Choose', command=level)
level_btn.pack(pady=2)

lblmsg = tk.Label(main)
lblmsg.pack()

word_label = tk.Label(main)
word_label.pack()

txt1 = tk.Entry(main, width=2)
txt1.pack(pady=3)

btn_guess = tk.Button(main, text='Guess letter', command=lambda: guess(1))
btn_guess.pack()

wrong_letters = tk.Label(main)
wrong_letters.pack()

guess_word1 = tk.Entry(main)
guess_word1.pack()

word_btn = tk.Button(main, text='Guess the word', command=lambda: guess(2))
word_btn.pack()

canvas = create_canvas(main)
draw_hangman(main)
main.mainloop()