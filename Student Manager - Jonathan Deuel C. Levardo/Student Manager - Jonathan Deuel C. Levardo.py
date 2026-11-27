from tkinter import *
from PIL import ImageTk, Image
import random

root = Tk()
root.title('Assessment 1 Exercise 3: Student Manager - Jonathan Deuel C. Levardo')
root.geometry('1440x1024')

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

def displayData(call_student):
    print(data_list_of_lists[call_student][0])

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

find_Highest_Percentage_Index()

# Get rest of data from the same sutdent
print(student_data_for_use['name'][highest_mark_index])

find_Lowest_Percentage_Index()
print(student_data_for_use['name'][lowest_mark_index])

# print(student_data_for_use['grade'][5])


# root.mainloop()