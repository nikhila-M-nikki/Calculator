from tkinter import *
import tkinter.messagebox



window = Tk()
window.title("CALCULATOR")
window.geometry("300x450")
frame = Frame(window, bg="skyblue")
frame.pack(expand=True, fill='both', padx=5, pady=5)
entry = Entry(frame, relief=SUNKEN, borderwidth=3, width=47,justify='right', font=("Arial", 20))
entry.grid(row=0, column=0,columnspan=4,  ipady=20, pady=6, sticky="nsew")



def click(num):

    current = entry.get()
    num = str(num)

    if num == 'C':
        entry.delete(0, END)

    elif num in '+-*/':

        if current == '':
            if num == '-':
                entry.insert(END, num)
            return

        last = current[-1]

        if last in '+-*/':

            # Allow negative numbers after * or /
            if num == '-' and last in '*/':
                entry.insert(END, num)

            # Replace the previous operator
            elif last != '-' or num != '-':
                entry.delete(len(current)-1, END)
                entry.insert(END, num)

        else:
            entry.insert(END, num)

    else:
        entry.insert(END, num)



def equal():
    try:
      res=eval(entry.get())
      entry.delete(0, END)
      entry.insert(0, res)
    except:
        (tkinter.messagebox.showerror
            (
            "Error", "Invalid calculation"
        ))
button=[

    (1, 1, 0), (2, 1, 1), (3, 1, 2), ('C', 1, 3),
    (4, 2, 0), (5, 2, 1), (6, 2, 2), ('+', 2, 3),
    (7, 3, 0), (8, 3, 1), (9, 3, 2), ('*', 3, 3),
    (0, 4, 0), ('/', 4, 1), ('-', 4, 2), ('=', 4, 3)
]

for (text, r, c) in button:
    if text== '=':
        btn = Button(frame, text=text, command=equal)
    else:
        btn = Button(frame, text=text,command=lambda x=text:click(x))

    btn.grid(row=r, column=c, padx=5, pady=5, sticky="nsew")

# ---------------- GRID CONFIG ---------------- #

for i in range(5):
    frame.rowconfigure(i, weight=1)

for j in range(4):
    frame.columnconfigure(j, weight=1)

window.mainloop()