
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
from tkinter import*
reps = 0
timers = None
import math
#window
window = Tk()
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timers)
    canvas.itemconfig(timer,text="00:00")
    title.config(text="Timer")
    checkmark.config(text="")
    global reps
    reps=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_time():

    global reps
    reps+=1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps%8 == 0:
        countdown(long_break_sec)
        title.config(text="Break",fg =RED)
    elif reps %2 == 0:
        countdown(short_break_sec)
        title.config(text="Break",fg=PINK)
    else:
        countdown(work_sec)
        title.config(text="Work", fg =GREEN)





def countdown(count):

    minute = count//60
    seconds = count%60
    if seconds<10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer,text=str(minute)+":"+ str(seconds))
    if count>0:
        global timers
        timers = window.after(1000,countdown,count-1)

    else :
        start_time()
        marks = ""
        work_session = (math.floor(reps / 2))
        for _ in range(work_session):
            marks += "✓"
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
from tkinter import*

window.title("Pomodoro")
window.config(padx=100,pady=50, bg=YELLOW)

#canvas
canvas = Canvas(height = 224, width = 200, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 112, image=tomato_img)
canvas.grid(column = 2,row = 2)

#display text
timer=canvas.create_text(103,130,text = "00:00", fill="white",font= (FONT_NAME,35,"bold"))

#label
title = Label(text = "Timer", font = (FONT_NAME,50),fg = GREEN , bg = YELLOW)
title.grid(column=2,row=1)

checkmark = Label(text = "✓", fg = GREEN,bg = YELLOW)
checkmark.grid(column = 2,row = 4)

#button-for strt and end
start_button= Button(text="Start",command=start_time)
start_button.grid(column=1,row=3)
end_button = Button(text="end",highlightthickness=0, command=reset_timer)
end_button.grid(column=3,row=3)




window.mainloop()