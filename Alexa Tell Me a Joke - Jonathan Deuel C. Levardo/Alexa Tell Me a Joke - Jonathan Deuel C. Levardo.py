from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title('Assessment 2 Alexa Tell Me a Joke - Jonathan Deuel C. Levardo')
root.geometry('800x600')

# REFERENCE ON HOW TO CHANGE ROOT BACKGROUND COLOR
# GeeksforGeeks (2024). How to Change a Tkinter Window Background Color. [online] GeeksforGeeks. 
# Available at: https://www.geeksforgeeks.org/python/how-to-change-a-tkinter-window-background-color/ 
# [Accessed 22 Nov. 2026].

root.config(bg='#050832')

# ====================================== IMAGE ======================================

# Frame to contain image
image_frame = Frame(root, bg='#000000', width=400, height=600)
image_frame.place(relx=0, rely=0)
# image_frame.pack(fill='both', expand=True)
# image_frame.pack_propagate(False)
# image_frame.config(width=400, height=600)

img = Image.open('Exercise 2 img.png') # Open image
img_display = ImageTk.PhotoImage((img)) # Create image label

# Label to post the image
img_label = Label(image_frame, image=img_display)
img_label.pack(side=LEFT, fill='both', expand=True)

# ====================================== FUNCTIONS ======================================

# REFERENCE FOR HOW TO RANDOMLY SELECT A LINE
# Robᵩ (2013). ‘To select one line at random from a file:...’. [Comment on online forum post] Stack Overflow. 
# Available at: https://stackoverflow.com/questions/20009581/randomly-generate-a-line-from-a-txt-file 
# [Accessed 20 Nov. 2026].

def generateJoke():
    with open('randomJokes.txt', 'r', encoding='utf-8') as file:
        lines = random.choice(list(file))

        # REFERENCE FOR .strip()
        # W3Schools (n.d.). Python string strip() method. [online] www.w3schools.com. 
        # Available at: https://www.w3schools.com/python/ref_string_strip.asp [Accessed 22 Nov. 2026].
        
        chosen_line = lines.strip()

        # REFERENCE FOR HOW TO STOP READING A FILE AT A SPECIFIC CHARACTER
        # Borislav Hadzhiev (2024). Read a File Until a Specific Character in Python. bobbyhadz. 
        # Available at: https://bobbyhadz.com/blog/python-read-file-until-specific-character [Accessed 20 Nov. 2026].

        stop_character = '?' # Stop setup line at "?"

        global joke
        joke = chosen_line.split(stop_character, 1) # Variable containing the Set Up and Punchline

# REFERENCE ON HOW TO CLOSE THE APP WITH A BUTTON
# Jesus is Lord (2012). “With minimal editing to your code (Not sure if they’ve…”. [Comment on online forum post] Stack Overflow. 
# Available at: https://stackoverflow.com/questions/9987624/how-to-close-a-tkinter-window-by-pressing-a-button [Accessed 21 Nov. 2026].

def closeApp():
    root.destroy()

def setup():
    global setup_lbl, punchline_lbl

    generateJoke() # Pull out a new joke

    # Delete any preexisting joke
    if setup_lbl and punchline_lbl:
        setup_lbl.destroy()
        punchline_lbl.destroy()

    # Change setup label
    setup_lbl = Label(joke_frame, text=f'{joke[0]}?', font=('tahoma', 10), fg='#ffffff', bg='#3039b0')
    setup_lbl.place(relx=0.5, rely=0.2, anchor=CENTER)
    # setup_lbl.pack(padx=10, pady=(10, 0))

    
    # Joke button will now reveal the punchline when pressed
    joke_btn.config(text='Show punchline', command=lambda: [punchline()])
    
def punchline():
    global punchline_lbl

    # Change punchline label
    punchline_lbl = Label(joke_frame, text=f'{joke[1]}', font=('tahoma', 10), fg='#ffffff', bg='#3039b0')
    punchline_lbl.place(relx=0.5, rely=0.27, anchor=CENTER)
    # punchline_lbl.pack(padx=10, pady=(10, 0))


    # Joke button will now start a new joke when pressed
    joke_btn.config(text='Tell me another one', command=lambda: [setup()])

# ====================================== SET UP ======================================

# Frame to containjoke function
joke_frame = Frame(root, bg='#050832', width=400, height=600)
joke_frame.place(relx=0.5, rely=0)
# joke_frame.pack(side=RIGHT, fill='both', expand=True)
# joke_frame.pack_propagate(False)
# joke_frame.config(width=400, height=600)

setup_lbl = Label(joke_frame, text='', bg='#050832')
setup_lbl.place(relx=0.5, rely=0.2)
# setup_lbl.pack(padx=10, pady=(10, 0))

punchline_lbl = Label(joke_frame, text='', bg='#050832')
punchline_lbl.place(relx=0.5, rely=0.25)
# punchline_lbl.pack(padx=10, pady=(10, 0))

joke_btn = Button(joke_frame, text='Alexa, tell me a joke', font=('tahoma', 15), fg='#ffffff',
bg='#3039b0', command=lambda: [setup()], width=20, bd=0)
joke_btn.place(relx=0.5, rely=0.75, anchor=CENTER)

close_btn = Button(joke_frame, text='Quit', font=('tahoma', 15), fg='#ffffff',
bg='#0c1052', command=lambda: [closeApp()], width=20, bd=0)
close_btn.place(relx=0.5, rely=0.84, anchor=CENTER)

mainloop()