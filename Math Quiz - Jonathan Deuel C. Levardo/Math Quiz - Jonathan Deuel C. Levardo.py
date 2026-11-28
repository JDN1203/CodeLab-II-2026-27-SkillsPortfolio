# Call all libraries
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()
root.title('Assessment 1 Math Quiz - Jonathan Deuel C. Levardo')
root.geometry('1212x862')

# For randomizer
import random

# ============================= GLOBAL VARIABLES =============================
universal_bg_color = '#2B2B2B'
chances = 2

easy_mode = False
medium_mode = False
hard_mode = False

# REFERENCE FOR HOW TO USE StringVar()
# Understanding Tkinter Variables. (2022). [Video] Directed by Atlas. YouTube. 
# Available at: https://www.youtube.com/watch?v=1Rc9ghe2P0Y [Accessed 19 Nov. 2026].
math_question = StringVar()
answer_value = StringVar()

# REFERENCE FOR IntVar()
# GeeksforGeeks (2019). Setting and Retrieving Values of Tkinter Variable Python. [online] 
# Available at: https://www.geeksforgeeks.org/python/python-setting-and-retrieving-values-of-tkinter-variable/ 
# [Accessed 20 Nov. 2026].
# user_answer = IntVar()
keeping_score = IntVar()
value1 = IntVar()
value2 = IntVar()
questions_complete = IntVar()


# ============================= SETUP IMAGES =============================

# REFERENCE ON FIXING IMAGE DISPLAY ISSUES
# Nawaz Dhandala (2026). How to Fix Tkinter Image Display Issues. [online] OneUptime | One Complete Observability Platform. 
# Available at: https://oneuptime.com/blog/post/2026-01-25-fix-tkinter-image-display-issues/view [Accessed 28 Nov. 2026].

def create_Image_Label(parent, image_path):
    new_image = Image.open(image_path)
    photo = ImageTk.PhotoImage(new_image)

    image_label = Label(parent, image=photo, borderwidth=0)
    image_label.image = photo
    return image_label


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

# Title Widget image for design 
title_img = create_Image_Label(title_widget, 'Math Quiz Design (900 x 438 px).png')
title_img.place(relx=0.5, rely=1.02, anchor=S)

# App Label
app_title = Label(title_widget, text="MATH\nQUIZ", font=('tahoma', 100), 
bg="#ffffff", fg="#000000", justify=CENTER)
app_title.place(relx=0.5, rely=0.5, anchor='center')

# Display Difficulty Menu button
display_diff_menu_btn = Button(title_widget, text="Menu", font=('tahoma', 20),
fg="#ffffff", bg="#000000", command=lambda: [displayMenu(), keeping_score.set(0)], width=10, bd=0, highlightthickness=0)
display_diff_menu_btn.place(relx=0.5, rely=0.85, anchor='center')


# ============================= CONTAINER FOR ACTIVITY SIDE OF APP =============================

# Create frame for Activity Side of app (right side of window)
activity_side = Frame(root, bg=universal_bg_color)
activity_side.pack(side=RIGHT, fill='both', expand=True)
activity_side.pack_propagate(False)
activity_side.config(width=727.2) # Size of activity_side


# ============================= IMPORTANT FUNCTIONS AND CLASSES =============================

# Set to Easy Mode Function
def setEasy():
    global easy_mode, medium_mode, hard_mode
    easy_mode = True
    medium_mode = False
    hard_mode = False

    return easy_mode

# Set to Medium Mode Function
def setMedium():
    global easy_mode, medium_mode, hard_mode
    easy_mode = False
    medium_mode = True
    hard_mode = False

    return medium_mode

# Set to Hard Mode Function
def setHard():
    global easy_mode, medium_mode, hard_mode
    easy_mode = False
    medium_mode = False
    hard_mode = True

    return hard_mode

# (FROM LECTURE EXERCISE) Delete previously selected pages in Activity Side
def delete_prev_activity_pages():
    for frame in activity_side.winfo_children():
        frame.destroy()


# Function to display Difficulty Menu on Activity Side
def displayMenu():
	delete_prev_activity_pages()

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
    command=lambda:[setEasy(), quizSetUp()])
	easy_btn.place(rely=0.189, relwidth=1, height=200)

	# Medium Difficulty Menu button
	medium_btn = Button(diff_frame, text="MEDIUM | Double digit numbers", font=('tahoma', 25), 
	fg="#000000", bg="#FFF375", command=lambda: [setMedium(), quizSetUp()], bd=0, highlightthickness=0)
	medium_btn.place(rely=0.479, relwidth=1, height=200)

	# Hard Difficulty Menu button
	hard_btn = Button(diff_frame, text="HARD | Triple digit numbers", font=('tahoma', 25), 
	fg="#000000", bg="#F24E4E", command=lambda: [setHard(), quizSetUp()], bd=0, highlightthickness=0)
	hard_btn.place(rely=0.759, relwidth=1, height=200)


# Generate Random Questions in Python. Math Quiz Tkinter - 5. (2023). [Video] Directed by Vishesh Programming. YouTube. 
# Available at: https://www.youtube.com/watch?v=Q9_lsPMxfkE&list=PLeb12iNltItErhMLGensr7Jsr0Wwsb8fN&index=5 
# [Accessed 20 Nov. 2026].

# Generate Random Question Function
def generateQuestion():

    # If the user has not completed 10 questions, generate a question. Else, show results
    if questions_complete.get() < 10:
        
        # REFERENCE FOR AVOIDING "UnboundLocalError Local variable"
        # GeeksforGeeks (2024). UnboundLocalError Local variable Referenced Before Assignment in Python [online] 
        # Available at: https://www.geeksforgeeks.org/python/unboundlocalerror-local-variable-referenced-before-assignment-in-python/ 
        # [Accessed 18 Nov. 2026].
        
        # REFERENCE FOR GLOBAL KEYWORD
        # W3Schools (n.d.). Python - Global Variables. [online]
        # Available at: https://www.w3schools.com/python/python_variables_global.asp [Accessed 21 Nov. 2026].

        global display_question, chances

        chances = 2 # Reset chances counter at the start of each question

        # Change question values depending on difficulty mode chosen
        if easy_mode == True:
            value1.set(random.randint(0, 9))
            value2.set(random.randint(0, 9))

        elif medium_mode == True:
            value1.set(random.randint(10, 99))
            value2.set(random.randint(10, 99))

        elif hard_mode == True:
            value1.set(random.randint(100, 999))
            value2.set(random.randint(100, 999))   

        # REFERENCE FOR random.choice()
        # W3Schools (n.d.). Python Random Choice() Method. [online] 
        # Available at: https://www.w3schools.com/python/ref_random_choice.asp [Accessed 18 Nov. 2026].
        operations = random.choice(['+', '-'])

        math_question.set(f'{value1.get()} {operations} {value2.get()}')
        answer_value.set(eval(math_question.get()))

        # REFERENCE FOR USING destroy() TO REMOVE WIDGETS
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
        display_question = Label(question_box, text=f"{math_question.get()}",
        bg='#ffffff', fg='#000000', font=('tahoma', 30), justify=LEFT)
        display_question.grid(row=0, column=0, padx=15, pady=(90, 0), sticky='w')

    else:
        # Remove content for questions
        display_score.destroy()
        display_question.destroy()
        user_entry.destroy()
        proceed_btn.destroy() 
        verify_answer.destroy()
        submit_btn.destroy()

        # Set up label for result
        result_label = Label(question_box, text='', bg='#ffffff', fg='#000000', font=('tahoma', 16))
        result_label.place(relx=0.5, rely=0.15, anchor=CENTER)

        # Calculate grade
        if keeping_score.get() >= 70:
            result_label.config(text='You got:')

            # Image for Grade A
            display_grade = create_Image_Label(question_box, 'Grade A.png')
            display_grade.place(relx=0.5, rely=0.4, anchor=CENTER)

        elif keeping_score.get() >= 60:
            result_label.config(text='You got:')

            # Image for Grade B
            display_grade = create_Image_Label(question_box, 'Grade B.png')
            display_grade.place(relx=0.5, rely=0.4, anchor=CENTER)

        elif keeping_score.get() >= 50:
            result_label.config(text='You got:')

            # Image for Grade C
            display_grade = create_Image_Label(question_box, 'Grade C.png')
            display_grade.place(relx=0.5, rely=0.4, anchor=CENTER)
            
        elif keeping_score.get() >= 40:
            result_label.config(text='You got:')

            # Image for Grade D
            display_grade = create_Image_Label(question_box, 'Grade D.png')
            display_grade.place(relx=0.5, rely=0.4, anchor=CENTER)

        elif keeping_score.get() <= 40:
            result_label.config(text='You got:')

            # Image for Grade F
            display_grade = create_Image_Label(question_box, 'Grade F.png')
            display_grade.place(relx=0.5, rely=0.4, anchor=CENTER)

        # "Try Again?" button
        retry_btn = Button(question_box, text="Try Again?", font=('tahoma',15), 
        fg="#000000", bg="#51E886", command=lambda: [quizSetUp(), retry_btn.destroy()], width=12, bd=0)
        retry_btn.place(relx=0.5, rely=0.65, anchor=CENTER)

# Verify Answer Function
def verify():
    global chances, verify_answer

    # Destroy any preexisting verify_answer label when entering a new answer
    if verify_answer:
        verify_answer.destroy()

    if user_entry.get() == answer_value.get() and chances > 0:

        # Create replacement verification message
        verify_answer = Label(question_box, text="Correct", bg='#ffffff', fg='#51E886',
        font=('tahoma', 17), justify=LEFT)
        verify_answer.grid(row=2, column=0, padx=15, pady=(5, 0), sticky='w')

        # REFERENCE FOR USING destroy() IN COMMAND
        # Elance, P. (2026). Destroy() Method in Tkinter - Python. [online] Tutorialspoint.com. 
        # Available at: https://www.tutorialspoint.com/article/destroy-method-in-tkinter-python [Accessed 22 Nov. 2026].

        # Proceed Button
        proceed_btn = Button(question_box, text="Next", font=('tahoma',10), 
        fg="#000000", bg="#51E886", command=lambda: [generateQuestion(), proceed_btn.destroy()], width=12, bd=0)
        proceed_btn.grid(row=3, column=0, padx=15, pady=(15, 0), sticky='w')

        # Calculate score based on number of chances left
        if chances == 2:
            keeping_score.set(keeping_score.get() + 10)
            display_score.config(text=f"Score: {keeping_score.get()}")

        elif chances == 1:
            keeping_score.set(keeping_score.get() + 5)
            display_score.config(text=f"Score: {keeping_score.get()}")
            
        else:
            keeping_score.set(keeping_score.get() + 0)
            display_score.config(text=f"Score: {keeping_score.get()}")

        questions_complete.set(questions_complete.get() + 1)

    else:
        # Show pop up displaying chances left
        chances -= 1
        messagebox.showinfo('Uh oh!', f'You got {chances} chance(s) left for this question')

    if chances == 0:
        questions_complete.set(questions_complete.get() + 1)

        # Create replacement verification message
        verify_answer = Label(question_box, text="No Chances Left", bg='#ffffff', fg='#F24E4E',
        font=('tahoma', 17), justify=LEFT)
        verify_answer.grid(row=2, column=0, padx=15, pady=(5, 0), sticky='w')

        # Proceed Button
        proceed_btn = Button(question_box, text="Next", font=('tahoma',10), 
        fg="#000000", bg="#F24E4E", command=lambda: [generateQuestion(), proceed_btn.destroy()], width=12, bd=0)
        proceed_btn.grid(row=3, column=0, padx=15, pady=(15, 0), sticky='w')


# Function to set up the background for quiz side
def quizSetUp():
    delete_prev_activity_pages()

    # Reset questions_complete to 0 at the start of quiz
    questions_complete.set(0)

    # Reset score to 0 at the start of quiz
    keeping_score.set(0)

    # So that outside functions can access them
    global question_box, display_question, display_score, verify_answer, user_entry, proceed_btn, submit_btn

    # Create frame containing contents of the quiz in play
    quiz_play = Frame(activity_side, bg=universal_bg_color)
    quiz_play.pack(pady=25, padx=40, fill='both', expand=True)

    # Change the header depending on difficulty mode chosen
    if easy_mode == True:
        # Easy Difficulty Header
        diff_header = Label(quiz_play, text='Easy', font=('tahoma',30), 
        fg="#000000", bg="#51E886", justify=LEFT)
        diff_header.place(rely=0, relwidth=1, height=106)

    elif medium_mode == True:
        # Medium Difficulty Header
        diff_header = Label(quiz_play, text='Medium', font=('tahoma',30), 
        fg="#000000", bg="#FFF375", justify=LEFT)
        diff_header.place(rely=0, relwidth=1, height=106)

    elif hard_mode == True:
        # Hard Difficulty Header
        diff_header = Label(quiz_play, text='Hard', font=('tahoma',30), 
        fg="#000000", bg="#F24E4E", justify=LEFT)
        diff_header.place(rely=0, relwidth=1, height=106)     

    # Create frame containing the questions, score, and chances
    question_box = Frame(quiz_play, bg='#ffffff')
    question_box.place(rely=0.2, relwidth=1, height=700)

    # Question Box Widget image for design 
    quiz_img1 = create_Image_Label(question_box, 'Math Quiz Design (900 x 438 px).png')
    quiz_img1.place(relx=0.5, rely=0.645, anchor=CENTER)

    # Setup Score Display
    display_score = Label(question_box, text=f"Score: 0", bg='#ffffff', 
    fg='#000000', font=('tahoma', 15))
    display_score.place(x=15, y=20)

    # Setup Question
    display_question = Label(question_box, text="",
    bg='#ffffff', fg='#000000', font=('tahoma', 30))
    display_question.grid(row=0, column=0)

    # Entry
    user_entry = Entry(question_box, font=('tahoma', 12), bg='#D6D6D6', width=22, bd=0)
    user_entry.grid(row=1, column=0, padx=(15, 0), pady=10)
    
    # Submit Button
    submit_btn = Button(question_box, text="Submit", font=('tahoma',10), 
    fg="#000000", bg="#51E886", command=lambda: [verify()], width=12, bd=0)
    submit_btn.grid(row=1, column=1, padx=(8, 0), pady=5)

    # Setup Proceed Button
    proceed_btn = Button(question_box, bg="#51E886", bd=0)
    proceed_btn.grid(row=3, column=0, padx=15, pady=(15, 0), sticky='w')

    # Setup verification message
    verify_answer = Label(question_box, text="", bg='#ffffff', 
    font=('tahoma', 30))
    verify_answer.grid(row=2, column=0)

    generateQuestion()

root.mainloop()