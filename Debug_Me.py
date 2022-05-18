from tkinter import *
import tkinter as tk
import pyperclip as pc

# LIST OF QUESTION
Q = [
    """#include<stdio.h>
void main()
11    printf("Hello World")
}
""",
    """#include<stdio.h>
void main()
{
    printf("Hello World1")
}
""",
    """#include<stdio.h>
void main()
{
    printf("Hello World2")
}
""",
    """#include<stdio.h>
void main()
{
    printf("Hello World3")
}
""",
    """#include<stdio.h>
void main()
{
    printf("Hello World4")
}
"""
]
# LIST OF ANSWERS
A = [
    """#include<stdio.h>
void main()
{
    printf("Hello World");
}
""",
    """#include<stdio.h>
void main()
{
    printf("Hello World1");
}
""",
    """#include<stdio.h>
void main()
{
    printf("Hello World2");
}
""",
    """#include<stdio.h>
void main()
{
    printf("Hello World3");
}
""",
    """#include<stdio.h>
void main()
{
    printf("Hello World4");
}
"""
]

# TIMER VARIABLES
minute, second = 60, 0

# FUNCTIONS FOR BUTTONS AND CALCULATION
# SUPPORT FUNCTIONS
# REMOVE SPACES
def remove(string):
    return string.replace(" ", "")
#REMOVE \n
def remove2(string):
    return string.replace("\n", "")

# BUTTON FUNCTIONS
# CHECK
def Check_code():
    a = A[Q.index(question.get("1.0", "end-1c"))]
    b = my_text.get("1.0", "end-1c")
    a = remove(a)
    b = remove(b)
    a = remove2(a)
    b = remove2(b)
    if a == b:
        label2.config(text="CORRECTED", fg="green")
    else:
        label2.config(text="ERROR", fg="remd")


# START
def Start():
    question.delete("1.0", END)
    question.insert(tk.END, Q[0])
    question.config(state=DISABLED)
    Button4.config(state=DISABLED)
    Button0.config(state=NORMAL)
    Button1.config(state=NORMAL)
    if len(Q) >1:
        Button2.config(state=NORMAL)
        update_time()

# UPDATE TIME
def update_time():
    global minute
    global second
    if minute == 0 and second == 0:
        root.quit()
    if second == 0:
        minute -= 1
        second = 59
    else:
        second -= 1
    if minute > -1:
        label.config(text="Time:\n"+str(minute)+":"+str(second))
        label.after(1000, update_time)
    else:
        pass

# NEXT QUESTION
def Next():
    Button3.config(state=NORMAL)
    question.config(state=NORMAL)
    t = question.get("1.0", "end-1c")
    question.delete("1.0", END)
    if Q.index(t) + 2 == len(Q):
        Button2.config(state=DISABLED)
        s = Q[Q.index(t) + 1]
        question.insert(tk.END, s)
    else:
        s = Q[Q.index(t) + 1]
        question.insert(tk.END, s)
    question.config(state=DISABLED)


# PREVIOUS QUESTION
def PRe():
    Button2.config(state=NORMAL)
    question.config(state=NORMAL)
    t = question.get("1.0", "end-1c")
    question.delete("1.0", END)
    if Q.index(t) - 1 == 0:
        Button3.config(state=DISABLED)
        s = Q[Q.index(t) - 1]
        question.insert(tk.END, s)
    else:
        s = Q[Q.index(t) - 1]
        question.insert(tk.END, s)
    question.config(state=DISABLED)


# COPY QUESTION
def copy_q():
    question.config(state=NORMAL)
    pc.copy(question.get("1.0", "end-1c"))
    question.config(state=DISABLED)
    my_text.delete("1.0", END)
    my_text.insert(tk.END, pc.paste())


root = Tk()

# ROOT ATTRIBUTES
root.attributes("-fullscreen", True)
root.attributes("-topmost", True)

# WIDGETS
# CHECK BUTTON
Button0 = Button(root, text="CHECK", padx=35, pady=25, bg="grey", command=Check_code, state=DISABLED)
Button0.grid(column=5, row=0)
# ERROR OR CORRECTED
label2 = Label(root, text="------", font=("Helvetica", 12))
label2.grid(column=5, row=1)
# COPY QUESTION BUTTON
Button1 = Button(root, text="COPY QUESTION", padx=10, pady=25, bg="grey", command=copy_q, state=DISABLED)
Button1.grid(column=5, row=2)
# NEXT QUESTION BUTTON
Button2 = Button(root, text="NEXT QUESTION", padx=10, pady=25, bg="grey", command=Next, state=DISABLED)
Button2.grid(column=5, row=3)
# PREVIOUS QUESTION BUTTON
Button3 = Button(root, text="PRE QUESTION", padx=10, pady=25, bg="grey", command=PRe, state=DISABLED)
Button3.grid(column=5, row=4)
# TIME DISPLAY
label = Label(root, text="Time:\n--:--", font=("Helvetica", 28))
label.grid(column=5, row=5)
# START BUTTON
Button4 = Button(root, text="START", padx=35, pady=25, bg="grey", command=Start)
Button4.grid(column=5, row=6)
# EXIT BUTTON
Button5 = Button(root, text="EXIT", padx=40, pady=25, bg="grey", command=root.quit)
Button5.grid(column=5, row=7)
# FRAME
my_frame = Frame(root)
my_frame.grid(row=0, column=0, rowspan=10)
# SCROLL BAR 1
text_scroll = Scrollbar(my_frame)
text_scroll.grid(row=0, column=4, sticky=NS, rowspan=10)
# SCROLL BAR 2
text_scroll2 = Scrollbar(my_frame)
text_scroll2.grid(row=0, column=1, sticky=NS, rowspan=10)
# TEXT WIDGET QUESTION
question = Text(my_frame,
                width=47,
                height=30,
                font=("Helvetica", 16),
                selectbackground="yellow",
                selectforeground="black",
                undo=True,
                yscrollcommand=text_scroll2.set)
question.grid(row=0, column=0, rowspan=10)
# TEXT WIDGET MY_TEXT
my_text = Text(my_frame,
               width=47,
               height=30,
               font=("Helvetica", 16),
               selectbackground="yellow",
               selectforeground="black",
               undo=True,
               yscrollcommand=text_scroll.set)
my_text.grid(row=0, column=3, rowspan=10)
# ASSIGNING SCROLL BARS
text_scroll.config(command=my_text.yview)
text_scroll2.config(command=question.yview)

root.mainloop()
