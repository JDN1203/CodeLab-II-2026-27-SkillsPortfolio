from tkinter import *
import random

# REFERENCE FOR HOW TO RANDOMLY SELECT A LINE
# Robᵩ (2013). ‘To select one line at random from a file:...’. [Comment on online forum post] Reddit. 
# Available at: https://stackoverflow.com/questions/20009581/randomly-generate-a-line-from-a-txt-file 
# [Accessed 20 Nov. 2026].
with open('randomJokes.txt', 'r', encoding='utf-8') as file:
    lines = random.choice(list(file))

    # REFERENCE FOR HOW TO STOP READING A FILE AT A SPECIFIC CHARACTER
    # Borislav Hadzhiev (2024). Read a File Until a Specific Character in Python. bobbyhadz. 
    # Available at: https://bobbyhadz.com/blog/python-read-file-until-specific-character [Accessed 20 Nov. 2026].

    # Stop setup line at "?"
    stop_character = '?'

    joke = lines.split(stop_character, 1)

    print(joke[0] + '?') # Setup
    print(joke[1]) # Punchline