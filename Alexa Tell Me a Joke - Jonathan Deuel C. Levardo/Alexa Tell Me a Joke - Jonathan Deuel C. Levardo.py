from tkinter import *
import random

root = Tk()
root.title('Assessment 2 Alexa Tell Me a Joke - Jonathan Deuel C. Levardo')
root.geometry('1212x862')

# ====================================== FUNCTIONS ======================================

# REFERENCE FOR HOW TO RANDOMLY SELECT A LINE
# Robᵩ (2013). ‘To select one line at random from a file:...’. [Comment on online forum post] Stack Overflow. 
# Available at: https://stackoverflow.com/questions/20009581/randomly-generate-a-line-from-a-txt-file 
# [Accessed 20 Nov. 2026].

def generateJoke():
    with open('randomJokes.txt', 'r', encoding='utf-8') as file:
        lines = random.choice(list(file))

        # REFERENCE FOR HOW TO STOP READING A FILE AT A SPECIFIC CHARACTER
        # Borislav Hadzhiev (2024). Read a File Until a Specific Character in Python. bobbyhadz. 
        # Available at: https://bobbyhadz.com/blog/python-read-file-until-specific-character [Accessed 20 Nov. 2026].

        stop_character = '?' # Stop setup line at "?"

        global joke
        joke = lines.split(stop_character, 1) # Variable containing the Set Up and Punchline

# REFERENCE ON HOW TO CLOSE THE APP WITH A BUTTON
# Jesus is Lord (2012). “With minimal editing to your code (Not sure if they’ve…”. [Comment on online forum post] Stack Overflow. 
# Available at: https://stackoverflow.com/questions/9987624/how-to-close-a-tkinter-window-by-pressing-a-button [Accessed 21 Nov. 2026].

def closeApp():
    root.destroy()

def setup():
    global setup_lbl, punchline_lbl

    generateJoke() # Pull out a new joke

    # Deelete any preexisting joke
    if setup_lbl and punchline_lbl:
        setup_lbl.destroy()
        punchline_lbl.destroy()

    # Change setup label
    setup_lbl = Label(root, text=f'{joke[0]}?', font=('tahoma', 10), fg='#000000')
    setup_lbl.pack(padx=10, pady=(10, 0))
    
    # Joke button will now reveal the punchline when pressed
    joke_btn.config(text='Show punchline', command=lambda: [punchline()])
    
def punchline():
    global punchline_lbl

    # Change punchline label
    punchline_lbl = Label(root, text=f'{joke[1]}', font=('tahoma', 10), fg='#000000')
    punchline_lbl.pack(padx=10, pady=(10, 0))

    # Joke button will now start a new joke when pressed
    joke_btn.config(text='Tell me another one', command=lambda: [setup()])

# ====================================== SET UP ======================================

setup_lbl = Label(root, text='', font=('tahoma', 10), fg='#000000')
setup_lbl.pack(padx=10, pady=(10, 0))

punchline_lbl = Label(root, text='', font=('tahoma', 10), fg='#000000')
punchline_lbl.pack(padx=10, pady=(10, 0))

joke_btn = Button(root, text='Alexa, tell me a joke', font=('tahoma', 10), bg='#ffffff', 
command=lambda: [setup()], width=20)
joke_btn.place(relx=0.5, rely=0.5, anchor=CENTER)

close_btn = Button(root, text='Quit', font=('tahoma', 10), bg='#ffffff', 
command=lambda: [closeApp()], width=20)
close_btn.place(relx=0.5, rely=0.55, anchor=CENTER)

mainloop()