from tkinter import *

root = Tk()
root.title('Assessment 1 Math Quiz - Jonathan Deuel C. Levardo')
root.geometry('500x500')
root.config(bg='#234567')

import random

# Test Variables
v1 = random.randint(0, 10)
v2 = random.randint(0, 10)
v3 = v1 + v2
test_question = f'{v1} + {v2}'

# Question
give_question = Label(root, text=f"{test_question}",
    bg='#234567', fg='white', font=('tahoma', 12))
give_question.place(x=10, y=100)

# Output
test_analysis = Label(root, text="",
    bg='#234567', fg='white', font=('tahoma', 12))
test_analysis.place(x=10, y=250)

# Entry
test_entry = Entry(root, font=('tahoma', 12))
test_entry.place(x=10, y=160)

# Submission Function
def submit():
	if int(test_entry.get()) == v3:
	   test_analysis.configure(text = 'Correct')
	else:
		test_analysis.configure(text = 'Incorrect')

# Submit Button
submit_btn = Button(root, text="Test Submit", fg="#ffffff", bg="#234567",
command=submit, width=20, font=('Roboto',12))
submit_btn.pack(padx=6, pady=200)

root.mainloop()