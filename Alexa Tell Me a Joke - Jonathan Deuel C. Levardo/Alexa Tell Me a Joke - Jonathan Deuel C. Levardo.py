from tkinter import *
import random

root = Tk()
root.title('Assessment 2 Alexa Tell Me a Joke - Jonathan Deuel C. Levardo')
root.geometry('1212x862')

# REFERENCE FOR HOW TO RANDOMLY SELECT A LINE
# Robᵩ (2013). ‘To select one line at random from a file:...’. [Comment on online forum post] Stack Overflow. 
# Available at: https://stackoverflow.com/questions/20009581/randomly-generate-a-line-from-a-txt-file 
# [Accessed 20 Nov. 2026].
with open('randomJokes.txt', 'r', encoding='utf-8') as file:
    lines = random.choice(list(file))

    # REFERENCE FOR HOW TO STOP READING A FILE AT A SPECIFIC CHARACTER
    # Borislav Hadzhiev (2024). Read a File Until a Specific Character in Python. bobbyhadz. 
    # Available at: https://bobbyhadz.com/blog/python-read-file-until-specific-character [Accessed 20 Nov. 2026].

    # Stop setup line at "?"
    stop_character = '?'

    global joke
    joke = lines.split(stop_character, 1)

    def setup():
        # print(joke[0] + '?') # Setup
        setup_lbl.config(text=f'{joke[0]}?')

    def punchline():
        # print(joke[1]) # Punchline
        punchline_lbl.config(text=f'{joke[1]}')


global setup_lbl
setup_lbl = Label(root, text='', font=('tahoma', 30), fg='#000000')
setup_lbl.pack(padx=10, pady=(10, 0))

global punchline_lbl
punchline_lbl = Label(root, text='', font=('tahoma', 30), fg='#000000')
punchline_lbl.pack(padx=10, pady=(10, 0))

setup_btn = Button(root, text='Tell me a joke', font=('tahoma', 30), bg='#ffffff', command=lambda: [setup()], width=12)
setup_btn.pack(padx=10, pady=(50, 0))

punchline_btn = Button(root, text='???', font=('tahoma', 30), bg='#ffffff', command=lambda: [punchline()], width=12)
punchline_btn.pack(padx=30, pady=(50, 0))

mainloop()