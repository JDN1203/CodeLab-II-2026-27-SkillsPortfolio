# Call all libraries
from tkinter import *

root = Tk()
root.title('Assessment 1 Math Quiz - Jonathan Deuel C. Levardo')
root.geometry('1212x862')


# ============================= Variables =============================
universal_bg_color = '#2B2B2B'
keeping_score = 0

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
	diff_header_label = Label(diff_frame, text='Pick a Difficulty', font=('tahoma',30), 
	bg='#000000', fg='#FFFFFF', justify=LEFT)
	diff_header_label.place(rely=0, relwidth=1, height=106)


	# REFERENCE FOR BUTTON STYLING
	# Kumar Panigrahi, K. (2026). How to Get Rid of Widget Border in Tkinter? [online] Tutorialspoint.com. 
	# Available at: https://www.tutorialspoint.com/article/how-to-get-rid-of-widget-border-in-tkinter 
	# [Accessed 18 Nov. 2026].
	
	# REFERENCE FOR EXECUTING MULTIPLE OPERATIONS WHEN BUTTON IS PRESSED
	# pradepghr (2017). “You can simply use lambda like this: …” [Comment on online forum post] Stack Overflow. 
	# Available at: https://stackoverflow.com/questions/13865009/have-multiple-commands-when-button-is-pressed 
	# [Accessed 18 Nov. 2026].
	
	# Easy Difficulty Menu button
	easy_btn = Button(diff_frame, text="EASY | Single digit numbers", font=('tahoma', 25), 
	fg="#000000", bg="#51E886", bd=0, highlightthickness=0, command=lambda:[decideOperation(), playEasyQuiz()])
	easy_btn.place(rely=0.2, relwidth=1, height=190)

	# Medium Difficulty Menu button
	medium_btn = Button(diff_frame, text="MEDIUM | Double digit numbers", font=('tahoma', 25), 
	fg="#000000", bg="#FFF375", bd=0, highlightthickness=0)
	medium_btn.place(rely=0.49, relwidth=1, height=190)

	# Hard Difficulty Menu button
	hard_btn = Button(diff_frame, text="HARD | Triple digit numbers", font=('tahoma', 25), 
	fg="#000000", bg="#F24E4E", bd=0, highlightthickness=0)
	hard_btn.place(rely=0.78, relwidth=1, height=190)


# Random Operation Function
def decideOperation():

	# REFERENCE FOR random.choice()
	# www.w3schools.com. (n.d.). Python Random Choice() Method. [online] 
	# Available at: https://www.w3schools.com/python/ref_random_choice.asp 
	# [Accessed 18 Nov. 2026].

	operations = ['add', 'sub']
	decide_math_sign = random.choice(operations)
	return decide_math_sign


# def modifyScore():
# 	if int(user_entry.get()) == answer_value:


# Function for Easy Mode
def playEasyQuiz():

	delete_prev_pages()

	# Create frame containing contents of the Easy Mode in play
	easy_quiz_play = Frame(activity_side, bg=universal_bg_color)
	easy_quiz_play.pack(pady=25, padx=40, fill='both', expand=True)

	# Easy Difficulty Header
	easy_header = Label(easy_quiz_play, text='Easy', font=('tahoma',30), 
	fg="#000000", bg="#51E886", justify=LEFT)
	easy_header.place(rely=0, relwidth=1, height=106)

	# Create frame containing the questions, score, and chances
	easy_question_box = Frame(easy_quiz_play, bg='#ffffff')
	easy_question_box.place(rely=0.2, relwidth=1, height=700)


	# REFERENCE FOR randint()
	# GeeksforGeeks. (2026). randint() Function in Python. [online] 
	# Available at: https://www.geeksforgeeks.org/python/python-randint-function/ 
	# [Accessed 14 Nov. 2026].

	# Variables
	value1 = random.randint(0, 9)
	value2 = random.randint(0, 9)

	#  Operation decided by decideOperation()
	if decideOperation() == 'add':
		answer_value = value1 + value2
		math_question = f'{value1} + {value2} = ?'
	else:
		answer_value = value1 - value2
		math_question = f'{value1} - {value2} = ?'


	# Score
	score = Label(easy_question_box, text=f"Score:{keeping_score}",
		bg='#ffffff', fg='#000000', font=('tahoma', 15))
	score.place(relx=0.1, rely=0.1)

	# Question
	display_question = Label(easy_question_box, text=f"{math_question}",
		bg='#ffffff', fg='#000000', font=('tahoma', 30))
	display_question.place(relx=0.1, rely=0.2)

	# Entry
	user_entry = Entry(easy_question_box, font=('tahoma', 12), bg='#D6D6D6', width=22, bd=0)
	user_entry.place(relx=0.1, rely=0.3)

	# Output
	verify_answer = Label(easy_question_box, text="",bg='#ffffff', 
	font=('tahoma', 30))
	verify_answer.place(relx=0.1, rely=0.4)

	# Submission Function
	def submit():
		if int(user_entry.get()) == answer_value:
			verify_answer.config(text = 'Correct', fg='#51E886')
		else:
			verify_answer.config(text = 'Incorrect', fg='#F24E4E')

	# Submit Button
	submit_btn = Button(easy_question_box, text="Test Submit", font=('tahoma',10), 
	fg="#000000", bg="#51E886", command=submit, width=12, bd=0)
	submit_btn.place(x=290, rely=0.3)



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
app_title = Label(title_widget, text="MATH\nQUIZ", font=('tahoma', 100), 
bg="#ffffff", fg="#000000", justify=CENTER)
app_title.place(relx=0.5, rely=0.5, anchor='center')

# Display Difficulty Menu button
display_diff_menu_btn = Button(title_widget, text="Menu", font=('tahoma', 20),
fg="#ffffff", bg="#000000", command=displayMenu, width=10, bd=0, highlightthickness=0)
display_diff_menu_btn.place(relx=0.5, rely=0.85, anchor='center')


# Create frame for Activity Side of app (right side of window)
activity_side = Frame(root, bg=universal_bg_color)
activity_side.pack(side=RIGHT, fill='both', expand=True)
activity_side.pack_propagate(False)
activity_side.config(width=727.2) # Size of activity_side


root.mainloop()