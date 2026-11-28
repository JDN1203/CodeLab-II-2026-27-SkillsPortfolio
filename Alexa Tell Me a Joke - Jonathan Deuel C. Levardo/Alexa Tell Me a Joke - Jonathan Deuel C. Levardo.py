from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title('Assessment 1 Exercise 2: Alexa Tell Me a Joke - Jonathan Deuel C. Levardo')
root.geometry('800x600')

# ====================================== VARIABLES ======================================
bg_color = '#02041C'

# ====================================== IMAGE ======================================

# Frame to contain image
image_frame = Frame(root, bg='black')
image_frame.pack(side=LEFT, fill='both', expand=True)

img = Image.open('Exercise 2 img.png') # Open image
img_display = ImageTk.PhotoImage((img)) # Create for image label

# Label to post the image
img_label = Label(image_frame, image=img_display, bd=0)
img_label.place(relx=0.5, rely=0.5, anchor=CENTER)


# ====================================== FUNCTIONS ======================================

# REFERENCE FOR HOW TO RANDOMLY SELECT A LINE
# Robᵩ (2013). ‘To select one line at random from a file:...’. [Comment on online forum post] Stack Overflow. 
# Available at: https://stackoverflow.com/questions/20009581/randomly-generate-a-line-from-a-txt-file 
# [Accessed 20 Nov. 2026].

# Function to get a joke from randomJokes.txt
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

# Function for closing the app with the quit button
def closeApp():
    root.destroy()

# Function to display set up portion of joke
def setup():
    global setup_lbl, punchline_lbl

    generateJoke() # Pull out a new joke

    # Delete any preexisting joke
    if setup_lbl and punchline_lbl:
        setup_lbl.destroy()
        punchline_lbl.destroy()

    # Change setup label
    setup_lbl = Label(joke_frame, text=f'{joke[0]}?', font=('tahoma', 11), fg='#ffffff', bg='#3039b0')
    setup_lbl.place(relx=0.5, rely=0.2, anchor=CENTER)
    
    # Joke button will now reveal the punchline when pressed
    joke_btn.config(text='Show punchline', command=lambda: [punchline()])

# Function to display punchline portion of joke
def punchline():
    global punchline_lbl

    # Change punchline label
    punchline_lbl = Label(joke_frame, text=f'{joke[1]}', font=('tahoma', 11), fg='#ffffff', bg='#3039b0')
    punchline_lbl.place(relx=0.5, rely=0.27, anchor=CENTER)
    # punchline_lbl.pack(padx=10, pady=(10, 0))

    # Joke button will now start a new joke when pressed
    joke_btn.config(text='Tell me another one', command=lambda: [setup()])


# ====================================== SET UP ======================================

# Frame to containjoke function
joke_frame = Frame(root, bg=bg_color)
joke_frame.pack(side=RIGHT, fill='both', expand=True)
joke_frame.pack_propagate(False)

setup_lbl = Label(joke_frame, text='', bg=bg_color)
setup_lbl.place(relx=0.5, rely=0.2)

punchline_lbl = Label(joke_frame, text='', bg=bg_color)
punchline_lbl.place(relx=0.5, rely=0.25)

joke_btn = Button(joke_frame, text='Alexa, tell me a joke', font=('tahoma', 16), fg='#ffffff',
bg='#3039b0', command=lambda: [setup()], width=20, bd=0)
joke_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

close_btn = Button(joke_frame, text='Quit', font=('tahoma', 16), fg='#ffffff',
bg='#0c1052', command=lambda: [closeApp()], width=20, bd=0)
close_btn.place(relx=0.5, rely=0.76, anchor=CENTER)

mainloop()