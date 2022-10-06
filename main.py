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
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.configure(text="Timer")
    check_mark_label.configure(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_time():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    countdown(work_secs)
    if reps % 8 == 0:
        countdown(long_break_secs)
        timer_label.configure(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(short_break_secs)
        timer_label.configure(text="Break", fg=PINK)
    else:
        countdown(work_secs)
        timer_label.configure(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_time()
        marks = ""
        work_sessions = math.floor(reps / 2)
        for _ in range(work_sessions):
            marks += "✔"
        check_mark_label.configure(text=marks)
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro")
window.configure(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)

timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


# Labels
timer_label = Label(text="Timer",  fg=GREEN, bg=YELLOW, font=(FONT_NAME, 45, "bold"))
timer_label.grid(column=1, row=0)

check_mark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_mark_label.grid(column=1, row=3)

# Buttons
timer_start_button = Button(text="Start", highlightthickness=0, command=start_time)
timer_reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)

timer_start_button.grid(column=0, row=2)
timer_reset_button.grid(column=2, row=2)

window.mainloop()
