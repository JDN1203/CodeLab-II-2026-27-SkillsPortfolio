from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title('Assessment 1 Exercise 3: Student Manager - Jonathan Deuel C. Levardo')
root.geometry('1440x1100')

# ============================= GLOBAL VARIABLES =============================
student_frame_bg = '#ffde59'
data_label_frame_bg = '#fff6d0'
summery_bg = '#2f3489'


# ============================= SETUP BACKGROUND =============================

# REFERENCE FOR USING IMAGE AS BACKGROUND
# GeeksforGeeks (2020). How to Use Images as Backgrounds in Tkinter? [online] 
# Available at: https://www.geeksforgeeks.org/python/how-to-use-images-as-backgrounds-in-tkinter/ [Accessed 24 Nov. 2026].
# Open image file

main_background = ImageTk.PhotoImage(Image.open('Exercise 3 Background (1089 x 900 px).png'))

display_background = Label(root, image=main_background)
display_background.place(relx=0.5, rely=0.5, relwidth=1, relheight=1, anchor=CENTER)


# ============================= OPENING TEXT FILE AND CREATING LISTS AND DICTIONARIES =============================

# REFERENCE FOR TURNING A TEXT FILE INTO A LIST
# socal_nerdtastic (2020). ‘Ok, I’ll take a guess:...’. [Comment on online forum post] Reddit. 
# Available at: https://www.reddit.com/r/learnpython/comments/hdk4am/comment/fvlo2nu/  [Accessed 23 Nov. 2026].

with open('studentMarks.txt') as data_file:
    data_list = data_file.read().splitlines()

    # REFERENCE FOR CONVERTING LIST INTO A LIST OF LISTS
    # GeeksforGeeks (2019). Python | Convert List into List of Lists. [online] 
    # Available at: https://www.geeksforgeeks.org/python/python-convert-list-into-list-of-lists/ [Accessed 23 Nov. 2026].

    # REFERENCE FOR SPLITTING STRINGS INTO SMALLER STRINGS
    # W3Schools (n.d.). Python String split() Method. [online] 
    # Available at: https://www.w3schools.com/python/ref_string_split.asp [Accessed 23 Nov. 2026].


    # REFERENCES FOR SPLITTING EACH LIST IN A STRING INTO INDIVIDUAL LISTS 
    # gnuDgnouD (2021). ‘string.split() return a list or words, so if you put...’. [Comment on online forum post] Reddit. 
    # Available at: https://www.reddit.com/r/learnpython/comments/n8cwd1/comment/gxhtpai/ [Accessed 23 Nov. 2026].

    # eadala (2021). ‘What u/gnuDgnouD did is perfectly correct and there's no reason...’. [Comment on online forum post] Reddit. 
    # Available at: https://www.reddit.com/r/learnpython/comments/n8cwd1/comment/gxhtpai/ [Accessed 23 Nov. 2026].

    # REFERENCE FOR APPLICATION OF split() in list comprehension
    '''
    Google (2026) Google AI Overview on splitting strings within lists python [Generative AI output]. 
    Available at: https://www.google.com/search?q=splitting+strings+within+lists+python&sca_esv=bc71
    facdedcd060c&sxsrf=AKL5yDjzsfSGCKqzylsWZmXmPi1_8RaCzg%3A1795452496392&ei=UG4Ea9u4F63Hi-gPkbj--A8&
    biw=1536&bih=825&uact=5&oq=splitting+strings+within+lists+python&gs_lp=Egxnd3Mtd2l6LXNlcnAiJXNwbG
    l0dGluZyBzdHJpbmdzIHdpdGhpbiBsaXN0cyBweXRob24yCBAhGKABGMMEMggQIRigARjDBEiQG1C-DVicF3ABeAGQAQCYAbA
    CoAGrDKoBBzAuMy4zLjG4AQPIAQD4AQGYAgOgAqgDwgIKEAAYRxjWBBiwA8ICChAhGAoYoAEYwwSYAwCIBgGQBgiSBwUxLjAu
    MqAH3xSyBwMyLTK4B6QDwgcDMC4zyAcFgAgB&sclient=gws-wiz-serphttps://www.reddit.com/r/learnpython/
    comments/okehsi/tkinter_transparent_images/ 
    '''

    # A list of lists of student data which is also written as a list containing 
    # ID, Name, Total Coursework Mark, Exam mark, Overall Percantage, and Grade 
    data_list_of_lists = [student_data.split(',') for student_data in data_list]

# Convert list of lists into a dictionary
student_data_for_use = {
    'id': [
        data_list_of_lists[1][0], data_list_of_lists[2][0], 
        data_list_of_lists[3][0], data_list_of_lists[4][0], 
        data_list_of_lists[5][0], data_list_of_lists[6][0], 
        data_list_of_lists[7][0], data_list_of_lists[8][0], 
        data_list_of_lists[9][0], data_list_of_lists[10][0]
    ],

    'name': [
        data_list_of_lists[1][1], data_list_of_lists[2][1], 
        data_list_of_lists[3][1], data_list_of_lists[4][1], 
        data_list_of_lists[5][1], data_list_of_lists[6][1], 
        data_list_of_lists[7][1], data_list_of_lists[8][1], 
        data_list_of_lists[9][1], data_list_of_lists[10][1]
    ],

    'total coursework mark':[
        int(data_list_of_lists[1][2]), int(data_list_of_lists[2][2]), 
        int(data_list_of_lists[3][2]), int(data_list_of_lists[4][2]), 
        int(data_list_of_lists[5][2]), int(data_list_of_lists[6][2]), 
        int(data_list_of_lists[7][2]), int(data_list_of_lists[8][2]), 
        int(data_list_of_lists[9][2]), int(data_list_of_lists[10][2])
    ],

    'exam mark':[
        int(data_list_of_lists[1][3]), int(data_list_of_lists[2][3]), 
        int(data_list_of_lists[3][3]), int(data_list_of_lists[4][3]), 
        int(data_list_of_lists[5][3]), int(data_list_of_lists[6][3]), 
        int(data_list_of_lists[7][3]), int(data_list_of_lists[8][3]), 
        int(data_list_of_lists[9][3]), int(data_list_of_lists[10][3])
        ],

    'overall percentage':[
        int(data_list_of_lists[1][4]), int(data_list_of_lists[2][4]), 
        int(data_list_of_lists[3][4]), int(data_list_of_lists[4][4]), 
        int(data_list_of_lists[5][4]), int(data_list_of_lists[6][4]), 
        int(data_list_of_lists[7][4]), int(data_list_of_lists[8][4]), 
        int(data_list_of_lists[9][4]), int(data_list_of_lists[10][4])
    ],

    'grade':[
        int(data_list_of_lists[1][5]), int(data_list_of_lists[2][5]), 
        int(data_list_of_lists[3][5]), int(data_list_of_lists[4][5]), 
        int(data_list_of_lists[5][5]), int(data_list_of_lists[6][5]), 
        int(data_list_of_lists[7][5]), int(data_list_of_lists[8][5]), 
        int(data_list_of_lists[9][5]), int(data_list_of_lists[10][5])
    ],
}


# ============================= CLASSES AND FUNCTIONS =============================

# Variable to be used for indexing student data
highest_mark_index = None
lowest_mark_index = None

def find_Highest_Percentage_Index():

    # REFERENCE FOR ACCESSING ITEMS IN LISTS WITHIN DICTIONARIES
    # GeeksforGeeks (2021). Python Accessing Items in Lists Within Dictionary. [online] 
    # Available at: https://www.geeksforgeeks.org/python/python-accessing-items-in-lists-within-dictionary/ [Accessed 26 Nov. 2026].

    for index, value in enumerate(student_data_for_use['overall percentage']):

        # If overall percentage is the highest value
        if student_data_for_use['overall percentage'][index] == max(student_data_for_use['overall percentage']):

            print(f'the highest percentage is {value}% at index {index}')

            # Update highest_mark_index
            global highest_mark_index
            highest_mark_index = index
            return highest_mark_index

            break

def find_Lowest_Percentage_Index():
    for index, value in enumerate(student_data_for_use['overall percentage']):

    # If overall percentage is the highest value
        if student_data_for_use['overall percentage'][index] == min(student_data_for_use['overall percentage']):

            print(f'the lowest percentage is {value}% at index {index}')

            # Update lowest_mark_index
            global lowest_mark_index
            lowest_mark_index = index
            return lowest_mark_index

            break

# find_Highest_Percentage_Index()

# # Get rest of data from the same sutdent
# print(student_data_for_use['name'][highest_mark_index])

# find_Lowest_Percentage_Index()
# print(student_data_for_use['name'][lowest_mark_index])


# REFERENCES ON HOW TO USE CLASSES IN TKINTER
# Using Tkinter with Classes. (2022). [Video] Directed by Atlas. YouTube. 
# Available at: https://www.youtube.com/watch?v=eaxPK9VIkFM [Accessed 27 Nov. 2026].

# GeeksforGeeks (2019). Python Classes and Objects. [online] 
# Available at: https://www.geeksforgeeks.org/python/python-classes-and-objects/ [Accessed 27 Nov. 2026].

class dataLabels:
    def __init__(self, x_place, y_place):
    
        self.data_labels_frame = Frame(display_background, width=547.6, height=33.8, bg=data_label_frame_bg)
        self.data_labels_frame.place(relx=x_place, rely=y_place, anchor=CENTER)

        self.id_label = Label(self.data_labels_frame, text='Number', font=('Roboto', 9), bg=data_label_frame_bg, 
        justify=LEFT)
        self.id_label.place(x=10.8, rely=0.5, anchor=W)

        self.name_label = Label(self.data_labels_frame, text='Name', font=('Roboto', 9), bg=data_label_frame_bg, 
        justify=LEFT)
        self.name_label.place(x=88.2, rely=0.5, anchor=W)

        self.coursework_mark_label = Label(self.data_labels_frame, text='Coursework \nmark', font=('Roboto', 9), 
        bg=data_label_frame_bg, justify=LEFT)
        self.coursework_mark_label.place(x=264.5, rely=0.5, anchor=W)

        self.exam_mark_label = Label(self.data_labels_frame, text='Exam \nmark', font=('Roboto', 9), 
        bg=data_label_frame_bg, justify=LEFT)
        self.exam_mark_label.place(x=355.6, rely=0.5, anchor=W)

        self.overall_percent_label = Label(self.data_labels_frame, text='Percent', font=('Roboto', 9), 
        bg=data_label_frame_bg, justify=LEFT)
        self.overall_percent_label.place(x=413.5, rely=0.5, anchor=W)

        self.grade_label = Label(self.data_labels_frame, text='Grade', font=('Roboto', 9), 
        bg=data_label_frame_bg, justify=LEFT)
        self.grade_label.place(x=478.2, rely=0.5, anchor=W)

class studentList:
    def __init__(self, index, x_place, y_place):

        # REFERENCE FOR BORDER STYLE
        # Joshi, I. (2021). ‘change the options accordingly highlightbackground is used to change the...’. [Comment on online forum post] Stack Overflow. 
        # Available at: https://stackoverflow.com/questions/50691267/how-to-add-a-border-for-a-frame-in-python-tkinter [Accessed 27 Nov. 2026].

        # Frame containing student data
        self.student_frame = Frame(display_background, width=547.6, height=33.8, bg=student_frame_bg, 
        highlightthickness=1, highlightbackground='black')
        self.student_frame.place(relx=x_place, rely=y_place, anchor=CENTER)

        # Student ID
        self.student_id = Label(self.student_frame, text=f'{student_data_for_use['id'][index]}', 
        font=('Roboto', 10), bg=student_frame_bg)
        self.student_id.place(x=10.8, rely=0.5, anchor=W)

        # Student Name
        self.student_name = Label(self.student_frame, text=f'{student_data_for_use['name'][index]}', 
        font=('Roboto', 10), bg=student_frame_bg)
        self.student_name.place(x=88.2, rely=0.5, anchor=W)

        # Student Total Coursework Mark
        self.student_coursework_mark = Label(self.student_frame, text=f'{student_data_for_use['total coursework mark'][index]}', 
        font=('Roboto', 10), bg=student_frame_bg)
        self.student_coursework_mark.place(x=264.5, rely=0.5, anchor=W)

        # Student Exam Mark
        self.student_exam_mark = Label(self.student_frame, text=f'{student_data_for_use['exam mark'][index]}', 
        font=('Roboto', 10), bg=student_frame_bg)
        self.student_exam_mark.place(x=355.6, rely=0.5, anchor=W)

        # Student Percent
        self.student_overall_percent = Label(self.student_frame, text=f'{student_data_for_use['overall percentage'][index]}', 
        font=('Roboto', 10), bg=student_frame_bg)
        self.student_overall_percent.place(x=413.5, rely=0.5, anchor=W)

        # Student Grade
        self.student_grade = Label(self.student_frame, text=f'{student_data_for_use['grade'][index]}', 
        font=('Roboto', 10), bg=student_frame_bg)
        self.student_grade.place(x=478.2, rely=0.5, anchor=W)

def allStudents():

    call_labels = dataLabels(0.39, 0.29)
    call_labels.data_labels_frame

    student1 = studentList(0, 0.39, 0.35)
    student1.student_frame

    student2 = studentList(1, 0.39, 0.4)
    student2.student_frame

    student3 = studentList(2, 0.39, 0.45)
    student3.student_frame

    student4 = studentList(3, 0.39, 0.5)
    student4.student_frame

    student5 = studentList(4, 0.39, 0.55)
    student5.student_frame

    student6 = studentList(5, 0.39, 0.6)
    student6.student_frame

    student7 = studentList(6, 0.39, 0.65)
    student7.student_frame

    student8 = studentList(7, 0.39, 0.7)
    student8.student_frame

    student9 = studentList(8, 0.39, 0.75)
    student9.student_frame

    student10 = studentList(9, 0.39, 0.8)
    student10.student_frame

def displayData(call_student):
    print(data_list_of_lists[call_student][0])

def calcuate_Average_Percent():

    # REFERENCE FOR sum()
    # GeeksforGeeks (2018). Find Sum of Elements in List Python. [online] 
    # Available at: https://www.geeksforgeeks.org/python/python-program-to-find-sum-of-elements-in-list/  [Accessed 27 Nov. 2026].

    average_value = sum(student_data_for_use['overall percentage']) / len(student_data_for_use['overall percentage'])
    return average_value


allStudents()

# ============================= SUMMARY AND OPTIONS =============================

# Summary Section
summary_frame = Frame(display_background, bg=data_label_frame_bg)
summary_frame.place(relx=0.695, rely=0.35, anchor=CENTER)

num_of_students = Label(summary_frame, text=f'Number of students: {len(student_data_for_use['name'])}', font=('Roboto', 15), 
bg=summery_bg, fg='#ffde59', width=20, height=2, highlightthickness=1, highlightbackground='black')
num_of_students.pack(pady=5)

average_percent = Label(summary_frame, text=f'Average percent: {calcuate_Average_Percent()}', font=('Roboto', 15), 
bg=summery_bg, fg='#ffde59', width=20, height=2, highlightthickness=1, highlightbackground='black')
average_percent.pack(pady=5)

# Viewing Options
viewing_btns_frame = Frame(display_background, bg=data_label_frame_bg)
viewing_btns_frame.place(relx=0.695, rely=0.575, anchor=CENTER)

all_records_btn = Button(viewing_btns_frame, text='View All Records', font=('Roboto', 15), 
bg='#ffffff', fg='#000000', width=20, height=2, highlightthickness=1, highlightbackground='black', bd=0)
all_records_btn.pack(pady=5)

highest_mark_btn = Button(viewing_btns_frame, text='View Highest Mark', font=('Roboto', 15), 
bg='#ffffff', fg='#000000', width=20, height=2, highlightthickness=1, highlightbackground='black', bd=0)
highest_mark_btn.pack(pady=5)

lowest_mark_btn = Button(viewing_btns_frame, text='View Lowest Mark', font=('Roboto', 15), 
bg='#ffffff', fg='#000000', width=20, height=2, highlightthickness=1, highlightbackground='black', bd=0)
lowest_mark_btn.pack(pady=5)

root.mainloop()