# Call all libraries
from tkinter import *

root = Tk()
root.title('Assessment 1 Math Quiz - Jonathan Deuel C. Levardo')
root.geometry('1212x862')
universal_bg_color = '#2B2B2B'

# For randomizer
import random

# ============================= IMPORTANT FUNCTIONS =============================

# (FROM LECTURE EXERCISE) Delete previous selected pages
def delete_prev_pages():
    for frame in activity_side.winfo_children():
        frame.destroy()

# Difficulty Menu Function
def displayMenu():

	delete_prev_pages()

	# Create frame containing contents of Difficulty Menu
	diff_frame = Frame(activity_side, bg=universal_bg_color)
	diff_frame.pack(pady=25, padx=40, fill='both', expand=True)

	# Difficulty Menu Label
	diff_header_label = Label(diff_frame, text='Pick a Difficulty', font=('Roboto',30), 
	bg='#000000', fg='#FFFFFF', justify=LEFT)
	diff_header_label.place(rely=0, relwidth=1, height=106)


	# REFERENCE FOR BUTTON STYLING
	# Kumar Panigrahi, K. (2026). How to Get Rid of Widget Border in Tkinter? [online] Tutorialspoint.com. 
	# Available at: https://www.tutorialspoint.com/article/how-to-get-rid-of-widget-border-in-tkinter 
	# [Accessed 18 Nov. 2026].
	
	# Easy Difficulty Menu button
	easy_btn = Button(diff_frame, text="EASY | Single digit numbers", font=('Roboto',25), 
	fg="#000000", bg="#51E886", bd=0, highlightthickness=0, command=playQuiz)
	easy_btn.place(rely=0.2, relwidth=1, height=190)

	# Medium Difficulty Menu button
	medium_btn = Button(diff_frame, text="MEDIUM | Double digit numbers", font=('Roboto',25), 
	fg="#000000", bg="#FFF375", bd=0, highlightthickness=0)
	medium_btn.place(rely=0.49, relwidth=1, height=190)

	# Hard Difficulty Menu button
	hard_btn = Button(diff_frame, text="HARD | Triple digit numbers", font=('Roboto',25), 
	fg="#000000", bg="#F24E4E", bd=0, highlightthickness=0)
	hard_btn.place(rely=0.78, relwidth=1, height=190)


# Function for Gameplay
def playQuiz():

	delete_prev_pages()

	# Create frame containing contents of the quiz in play
	easy_quiz_play = Frame(activity_side, bg=universal_bg_color)
	easy_quiz_play.pack(pady=25, padx=40, fill='both', expand=True)

	# Variables
	value1 = random.randint(0, 10)
	value2 = random.randint(0, 10)
	answer_value = value1 + value2
	math_question = f'{value1} + {value2} = ?'

	# Question
	display_question = Label(easy_quiz_play, text=f"{math_question}",
		bg='#234567', fg='white', font=('tahoma', 12))
	display_question.place(x=10, y=100)

	# Output
	verify_answer = Label(easy_quiz_play, text="",
		bg='#234567', fg='white', font=('tahoma', 12))
	verify_answer.place(x=10, y=250)

	# Entry
	user_entry = Entry(easy_quiz_play, font=('tahoma', 12))
	user_entry.place(x=10, y=160)

	# Submission Function
	def submit():
		if int(user_entry.get()) == answer_value:
			verify_answer.config(text = 'Correct')
		else:
			verify_answer.config(text = 'Incorrect')

	# Submit Button
	submit_btn = Button(easy_quiz_play, text="Test Submit", font=('Roboto',12), 
	fg="#ffffff", bg="#234567", command=submit, width=20, bd=0, highlightthickness=0)
	submit_btn.pack(padx=6, pady=200)


# ============================= MAIN FRAMES =============================

# Create frame for Title Side of app (left side of window)
title_side = Frame(root, bg=universal_bg_color)
title_side.pack(side=LEFT, fill='both', expand=True)
title_side.pack_propagate(False)
title_side.config(width=484.8) # Size of title_side

# Title Widget
title_widget = Frame(title_side, bg='#FFFFFF')
title_widget.pack(pady=25, padx=40, fill='both', expand=True)
title_widget.pack_propagate(False)

# App Label
app_title = Label(title_widget, text="Math\nQuiz", font=('Roboto', 100), 
bg="#ffffff", fg="#000000", justify=CENTER)
app_title.place(relx=0.5, rely=0.5, anchor='center')

# Display Difficulty Menu button
display_diff_menu_btn = Button(title_widget, text="Menu", font=('Roboto', 20),
fg="#ffffff", bg="#000000", command=displayMenu, width=10, bd=0, highlightthickness=0)
display_diff_menu_btn.place(relx=0.5, rely=0.85, anchor='center')


# Create frame for Activity Side of app (right side of window)
activity_side = Frame(root, bg=universal_bg_color)
activity_side.pack(side=RIGHT, fill='both', expand=True)
activity_side.pack_propagate(False)
activity_side.config(width=727.2) # Size of activity_side


root.mainloop()