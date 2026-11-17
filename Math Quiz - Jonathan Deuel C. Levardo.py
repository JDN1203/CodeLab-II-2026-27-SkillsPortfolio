# Call all libraries
from tkinter import *

root = Tk()
root.title('Assessment 1 Math Quiz - Jonathan Deuel C. Levardo')
root.geometry('1212x862')
# root.config(bg='#2B2B2B')


# (FROM LECTURE EXERCISE) Delete previous selected pages
def delete_prev_pages():
    for frame in quiz_side.winfo_children():
        frame.destroy()

# Difficulty Menu Function
def displayMenu():

	delete_prev_pages()

	# Create Difficulty Menu Frame
	diff_frame = Frame(quiz_side, bg='#FFFFFF', width=300)
	diff_frame.pack(pady=30)

	# Difficulty Menu Label
	diff_header_label = Label(diff_frame, text='Pick a Difficulty', bg='#000000', fg='#FFFFFF')
	diff_header_label.pack(pady=5)

	# Easy Difficulty Menu button
	easy_btn = Button(diff_frame, text="Test Submit", fg="#ffffff", bg="#234567", width=20, font=('Roboto',12))
	easy_btn.pack(padx=6, pady=200)

'''
# Function for Gameplay
def playQuiz():

	# Create Quiz Frame
	quiz_side = Frame(root, bg='#FFFFFF', width=504.37)
	quiz_side.pack(side=RIGHT, fill=Y)

	# Variables
	value1 = random.randint(0, 10)
	value2 = random.randint(0, 10)
	answer_value = value1 + value2
	math_question = f'{value1} + {value2} = ?'

	# Question
	display_question = Label(quiz_side, text=f"{math_question}",
		bg='#234567', fg='white', font=('tahoma', 12))
	display_question.place(x=10, y=100)

	# Output
	verify_answer = Label(quiz_side, text="",
		bg='#234567', fg='white', font=('tahoma', 12))
	verify_answer.place(x=10, y=250)

	# Entry
	user_entry = Entry(quiz_side, font=('tahoma', 12))
	user_entry.place(x=10, y=160)

	# Submission Function
	def submit():
		if int(user_entry.get()) == answer_value:
			verify_answer.config(text = 'Correct')
		else:
			verify_answer.config(text = 'Incorrect')

	# Submit Button
	submit_btn = Button(quiz_side, text="Test Submit", fg="#ffffff", bg="#234567",
	command=submit, width=20, font=('Roboto',12))
	submit_btn.pack(padx=6, pady=200)
'''


# Create frame for Title Side of app (left side of window)
title_side = Frame(root, bg='#2B2B2B')
title_side.pack(side=LEFT, fill=Y)
title_side.pack_propagate(False)
title_side.config(width=484.8) # Size of title_side

# Title Widget
title_widget = Frame(title_side, bg='#FFFFFF')
title_widget.pack(pady=25)
title_widget.pack_propagate(False)
title_widget.config(width=424.16, height=772.09)

# Page Label
page_title = Label(title_widget, text="Math\nQuiz", font=('Roboto', 100), 
bg="#ffffff", fg="#000000", justify=CENTER)
page_title.place(relx=0.5, rely=0.5, anchor='center')

# Display Difficulty Menu button
display_diff_menu_btn = Button(title_widget, text="Menu", fg="#ffffff", bg="#000000",
command=displayMenu, width=10, font=('Roboto',20))
# display_diff_menu_btn.place(relx=0.5, rely=0.5)
display_diff_menu_btn.place(relx=0.5, rely=0.85, anchor='center')


# Create frame for Quiz Side of app (right side of window)
quiz_side = Frame(root, bg='#FF0000')
quiz_side.pack(side=RIGHT, fill=Y)
quiz_side.pack_propagate(False)
quiz_side.config(width=727.2) # Size of quiz_side
# quiz_side.place(relwidth=0.5, relheight=1, relx=0.7, anchor='center')


root.mainloop()