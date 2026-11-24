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
    data_for_use = [student_data.split(',') for student_data in data_list]
    print(data_for_use[1][1]) # Print student name

# root.mainloop()