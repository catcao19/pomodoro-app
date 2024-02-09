from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    # timer_text 00:00
    # title_label "Timer"
    # reset check_marks
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_label.config(text="")
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If it is the 1, 3, 5, 7th rep
    if reps % 2 == 1:
        title_label.config(text="Work", fg=RED)
        count_down(work_sec)
    # If it is the 8th rep
    elif reps % 8 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(long_break_sec)

    # If it is the 2, 4, 6th rep
    else:
        title_label.config(text="Break", fg=GREEN)
        count_down(short_break_sec)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # """int"""
    # if count_sec == 0:
    #     """str"""
    """Dynamic Typing:Change a variable's data type
    by changing the content in that variable"""
    #     count_sec = "00"
    """Check in as a number"""
    if count_sec < 10:
        """format it as a string"""
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        """Execute a demand after a delay"""
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        """Add one check mark for every 2 reps"""
        """For every two reps, we completed one 25-minute work session"""
        """Divide reps by 2 to get the total number of work sessions we've done"""
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_label.config(text=mark)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="TIMER", font=(FONT_NAME, 50), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

check_label = Label(fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
