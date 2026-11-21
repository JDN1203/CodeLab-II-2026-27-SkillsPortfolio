# Call all libraries
from tkinter import *

root = Tk()
root.title('Assessment 1 Math Quiz - Jonathan Deuel C. Levardo')
root.geometry('1212x862')

# For randomizer
import random

# ============================= GLOBAL VARIABLES =============================
universal_bg_color = '#2B2B2B'
chances = 2
questions_complete = 0

# REFERENCE FOR HOW TO USE StringVar()
# Understanding Tkinter Variables. (2022). [Video] Directed by Atlas. YouTube. 
# Available at: https://www.youtube.com/watch?v=1Rc9ghe2P0Y [Accessed 19 Nov. 2026].
math_question = StringVar()
answer_value = StringVar()

# REFERENCE FOR IntVar()
# GeeksforGeeks (2019). Setting and Retrieving Values of Tkinter Variable Python. [online] GeeksforGeeks. 
# Available at: https://www.geeksforgeeks.org/python/python-setting-and-retrieving-values-of-tkinter-variable/ 
# [Accessed 20 Nov. 2026].
# user_answer = IntVar()
keeping_score = IntVar()

# easy_mode = False
# medium_mode = False
# hard_mode = False

# ============================= CONTAINER FOR TITLE SIDE OF APP =============================

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
fg="#ffffff", bg="#000000", command=lambda: [displayMenu()], width=10, bd=0, highlightthickness=0)
display_diff_menu_btn.place(relx=0.5, rely=0.85, anchor='center')


# ============================= CONTAINER FOR ACTIVITY SIDE OF APP =============================

# Create frame for Activity Side of app (right side of window)
activity_side = Frame(root, bg=universal_bg_color)
activity_side.pack(side=RIGHT, fill='both', expand=True)
activity_side.pack_propagate(False)
activity_side.config(width=727.2) # Size of activity_side


# ============================= IMPORTANT FUNCTIONS AND CLASSES =============================

# def setEasy():
#     easy_mode = True
#     medium_mode = False
#     hard_mode = False

#     return easy_mode

# def setMedium():
#     easy_mode = False
#     medium_mode = True
#     hard_mode = False

#     return medium_mode

# def setHard():
#     easy_mode = False
#     medium_mode = False
#     hard_mode = True

#     return hard_mode

# (FROM LECTURE EXERCISE) Delete previously selected pages in Activity Side
def delete_prev_activity_pages():
    for frame in activity_side.winfo_children():
        frame.destroy()

# Delete previous question
# def delete_prev_question():
#     for frame in quiz_play.winfo_children():
#         frame.destroy()

# Function to display Difficulty Menu on Activity Side
def displayMenu():

	delete_prev_activity_pages()

	# Reset score when entering menu
	# global keeping_score

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
	fg="#000000", bg="#51E886", bd=0, highlightthickness=0, 
    command=lambda:[quizSetUp()])
	easy_btn.place(rely=0.2, relwidth=1, height=190)

	# Medium Difficulty Menu button
	medium_btn = Button(diff_frame, text="MEDIUM | Double digit numbers", font=('tahoma', 25), 
	fg="#000000", bg="#FFF375", bd=0, highlightthickness=0)
	medium_btn.place(rely=0.49, relwidth=1, height=190)

	# Hard Difficulty Menu button
	hard_btn = Button(diff_frame, text="HARD | Triple digit numbers", font=('tahoma', 25), 
	fg="#000000", bg="#F24E4E", bd=0, highlightthickness=0)
	hard_btn.place(rely=0.78, relwidth=1, height=190)


# Generate Random Questions in Python. Math Quiz Tkinter - 5. (2023). [Video] Directed by Vishesh Programming. YouTube. 
# Available at: https://www.youtube.com/watch?v=Q9_lsPMxfkE&list=PLeb12iNltItErhMLGensr7Jsr0Wwsb8fN&index=5 
# [Accessed 20 Nov. 2026].

# Generate Random Question Function
def generateQuestion():

    # REFERENCE FOR AVOIDING "UnboundLocalError Local variable"
    # GeeksforGeeks (2024). UnboundLocalError Local variable Referenced Before Assignment in Python [online] 
    # Available at: https://www.geeksforgeeks.org/python/unboundlocalerror-local-variable-referenced-before-assignment-in-python/ 
    # [Accessed 18 Nov. 2026].
    
    #  REFERENCE FOR GLOBAL KEYWORD
    # W3Schools (n.d.). Python - global variables. [online] www.w3schools.com. 
    # Available at: https://www.w3schools.com/python/python_variables_global.asp [Accessed 21 Nov. 2026].

    global display_question
    global chances

    value1 = random.randint(0, 9)
    value2 = random.randint(0, 9)

    operations = random.choice(['+', '-'])

    math_question.set(f'{value1} {operations} {value2}')
    answer_value.set(eval(math_question.get()))

    # Destroy Method in TKinter | Remove Widget from Window | Math Quiz Tkinter - 6. (2023). [Video] Directed by Vishesh Programming. YouTube. 
    # Available at: https://www.youtube.com/watch?v=CpH9KSJsibQ [Accessed 20 Nov. 2026].
    
    # Destroy any preexisting display_question label
    if display_question:
        display_question.destroy()

    # Destroy any preexisting proceed_btn button
    if proceed_btn:
        proceed_btn.destroy()

    # Destroy any preexisting verify_answer label when entering a new question
    if verify_answer:
        verify_answer.destroy()
    

    # REFERENCE REGARDING PADDING PARAMETERS
    # Prakash Sharma, D. (2026). How to add padding to a tkinter widget only on one side? [online] Tutorialspoint.com. 
    # Available at: https://www.tutorialspoint.com/article/how-to-add-padding-to-a-tkinter-widget-only-on-one-side [Accessed 21 Nov. 2026].

    # Create Replacement Question Label
    display_question = Label(easy_question_box, text=f"{math_question.get()}",
    bg='#ffffff', fg='#000000', font=('tahoma', 30), justify=LEFT)
    display_question.grid(row=0, column=0, padx=15, pady=(90, 0), sticky='w')


# Verify Answer Function
def verify():
    global chances
    global questions_complete
    global verify_answer # Unsure why it's needed, but it ennsures that it is accessed
    # global user_entry

    # Destroy any preexisting verify_answer label when entering a new answer
    if verify_answer:
        verify_answer.destroy()

    if user_entry.get() == answer_value.get():

        # Create replacement verification message
        verify_answer = Label(easy_question_box, text="Correct", bg='#ffffff', fg='#51E886',
        font=('tahoma', 30), justify=LEFT)
        verify_answer.grid(row=2, column=0, padx=15, pady=(5, 0), sticky='w')

        # Proceed Button
        proceed_btn = Button(easy_question_box, text="Next", font=('tahoma',10), 
        fg="#000000", bg="#51E886", command=lambda: [generateQuestion()], width=12, bd=0)
        proceed_btn.grid(row=3, column=0, padx=15, pady=(15, 0), sticky='w')

        # Calculate score based on number of chances left
        if chances == 2:
            keeping_score.set(keeping_score.get() + 10)
        elif chances == 1:
            keeping_score.set(keeping_score.get() + 5)
        else:
            keeping_score.set(keeping_score.get() + 0)

        questions_complete += 1

    else:
        # Create replacement verification message
        verify_answer = Label(easy_question_box, text="Incorrect", bg='#ffffff', fg='#F24E4E', 
        font=('tahoma', 30), justify=LEFT)
        verify_answer.grid(row=2, column=0, padx=15, pady=(5, 0), sticky='w')

        chances -= 1


# Function to set up the background for quiz side
def quizSetUp():
    delete_prev_activity_pages()

	# Reset score when entering menu
    keeping_score.set(0)

    # So that outside functions can access them
    global easy_question_box
    global display_question
    global verify_answer
    global user_entry

    # Create frame containing contents of the quiz in play
    quiz_play = Frame(activity_side, bg=universal_bg_color)
    quiz_play.pack(pady=25, padx=40, fill='both', expand=True)

    # Easy Difficulty Header
    easy_header = Label(quiz_play, text='Easy', font=('tahoma',30), 
    fg="#000000", bg="#51E886", justify=LEFT)
    easy_header.place(rely=0, relwidth=1, height=106)

    # Create frame containing the questions, score, and chances
    easy_question_box = Frame(quiz_play, bg='#ffffff')
    easy_question_box.place(rely=0.2, relwidth=1, height=700)

    # Score Display
    display_score = Label(easy_question_box, text=f"Score: {keeping_score.get()}", bg='#ffffff', 
    fg='#000000', font=('tahoma', 15))
    display_score.place(x=15, y=20)

    # Question Setup
    display_question = Label(easy_question_box, text="",
    bg='#ffffff', fg='#000000', font=('tahoma', 30))
    display_question.grid(row=0, column=0)

    # Entry
    user_entry = Entry(easy_question_box, font=('tahoma', 12), bg='#D6D6D6', width=22, bd=0)
    user_entry.grid(row=1, column=0, padx=(15, 0), pady=10)
    
    # Being able to submit an answer for points if chances > 0
    if chances > 0:
        # Submit Button
        submit_btn = Button(easy_question_box, text="Submit", font=('tahoma',10), 
        fg="#000000", bg="#51E886", command=lambda: [verify()], width=12, bd=0)
        submit_btn.grid(row=1, column=1, padx=(8, 0), pady=5)

    # Create a button that allows to go to the next question
    # if user_entry.get() == answer_value.get():
    global proceed_btn

    # Proceed Button
    proceed_btn = Button(easy_question_box, bg="#51E886", bd=0)
    proceed_btn.grid(row=3, column=0, padx=15, pady=(15, 0), sticky='w')

    # Setup verification message
    verify_answer = Label(easy_question_box, text="", bg='#ffffff', 
    font=('tahoma', 30))
    verify_answer.grid(row=2, column=0)

    generateQuestion()

root.mainloop()


    # Function to show the question
    # def newQuestion():

    #     global easy_question_box

    #     # Frame containing the question grid
    #     question_plcement = Frame(easy_question_box, bg='#ffffff')
    #     question_plcement.pack(x=15, y=30)