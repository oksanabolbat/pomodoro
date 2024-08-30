import tkinter as tk

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
# WORK_MIN = 25
# SHORT_BREAK_MIN = 5
# LONG_BREAK_MIN = 20
WORK_MIN = 1
SHORT_BREAK_MIN = 2
LONG_BREAK_MIN = 1

timer = ""
window = tk.Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

reps = 0
label_checkbox_text = ""


def count_down(count_num):
    if count_num >= 0:
        global timer
        num_sec = count_num % 60
        bg_canvas.itemconfig(text_timer, text=f"{int(count_num / 60):02}:{num_sec:02}")
        timer = window.after(50, count_down, count_num - 1)
    else:
        start_timer()


def start_timer():
    global reps
    reps += 1
    btn_start.config(state="disabled")
    if reps % 8 == 0:
        count_down(60 * LONG_BREAK_MIN)
        label_header.config(fg=PINK, text="Break")
        add_label_checkbox()

    elif reps % 2 == 0:
        count_down(60 * SHORT_BREAK_MIN)
        label_header.config(text="Break", fg=RED)
        add_label_checkbox()
    else:
        count_down(60 * WORK_MIN)
        label_header.config(text="Work", fg=GREEN)


def reset_handler():
    global label_checkbox_text, reps
    label_checkbox_text = ""
    label_checkbox.config(text=label_checkbox_text)
    label_header.config(text="Timer", fg=GREEN)
    window.after_cancel(timer)
    btn_start.config(state="normal")
    reps = 0
    bg_canvas.itemconfig(text_timer, text="00:00")


def add_label_checkbox():
    global label_checkbox_text
    label_checkbox_text += "✔"
    label_checkbox.config(text=label_checkbox_text)


bg_image = tk.PhotoImage(file="tomato.png")
bg_canvas = tk.Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
bg_canvas.create_image(100, 111, image=bg_image)
text_timer = bg_canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
# count_down(10)
bg_canvas.grid(row=1, column=1)

label_header = tk.Label(text="Timer", font=(FONT_NAME, 25, "bold"), fg=GREEN, bg=YELLOW)
label_header.grid(row=0, column=1)

btn_start = tk.Button(text="Start", command=start_timer)
btn_start.grid(row=2, column=0)

btn_end = tk.Button(text="End", command=reset_handler)
btn_end.grid(row=2, column=2)

label_checkbox = tk.Label(text=label_checkbox_text, bg=YELLOW, fg=GREEN)
label_checkbox.grid(row=3, column=1)
# import time
# count = 5
# while True:
#     time.sleep(1)
#     count -= 1
#     print(count)

window.mainloop()
