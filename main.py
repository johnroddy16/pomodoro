#!/usr/bin/env python3 

from tkinter import * 
import math   

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20 
reps = 0 
checks = 0  
timer = None    

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def timer_start():
    # work_sec = WORK_MIN * 60
    # short_break_sec = SHORT_BREAK_MIN * 60
    # long_break_sec = LONG_BREAK_MIN * 60  
    work_sec = 60
    short_break_sec = 60
    long_break_sec = 60  
    global reps  
    global checks 
    
    reps += 1  
        
    if reps % 8 == 0:
        count_down(long_break_sec)
        change_timer_text('Break', RED)
        checks += 1
        check_label.config(text='✓ ' * checks) 
    elif reps % 2 == 0:
        count_down(short_break_sec)
        change_timer_text('Break', PINK)
        checks += 1 
        check_label.config(text='✓ ' * checks)
    else:
        count_down(work_sec)
        change_timer_text('Work', GREEN)  
     
    if reps == 9:
        checks = 0  
        check_label.config(text='')     
        
def count_down(count):
    global timer, reps 
    
    minutes = math.floor(count / 60)
    seconds = count % 60   
    
    canvas.itemconfig(timer_text, text=f'{minutes:02}:{seconds:02}')    
        
    if count > 0:
        timer = window.after(1000, count_down, count-1)  # took out timer = 
    else:
        timer_start() 
         
def change_timer_text(session, color):
    timer_label.config(text=session, fg=color)
    
def reset_timer():
    global reps
    global checks 
    window.after_cancel(timer) 
    canvas.itemconfig(timer_text, text='25:00')
    change_timer_text('Timer', GREEN)
    check_label.config(text='')
    reps = 0 
    checks = 0 
    print('timer completed')   

# ---------------------------- UI SETUP ------------------------------- #

# notes: fg will color the foreground, copy and paste a checkmark from wikipedia or wherever  
# create the window:
window = Tk()
window.title('Pomodoro')
# window.minsize(width=500, height=400)
window.config(padx=100, pady=50, bg=YELLOW)

# create the canvas widget:
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.grid(column=1, row=1)

# load and add image to canvas:
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_image)

# add timer text on top of the image:
timer_text = canvas.create_text(100, 135, text='25:00', fill='white', font=(FONT_NAME, 24))

# start button:
start_button = Button(text='Start', highlightthickness=0, borderwidth=0, command=timer_start) 
start_button.grid(column=0, row=2)

# reset button:
reset_button = Button(text='Reset', highlightthickness=0, borderwidth=0, command=reset_timer)   
reset_button.grid(column=2, row=2)

# timer label:
timer_label = Label(text='Timer', font=(FONT_NAME, 40), bg=YELLOW, fg=GREEN)
timer_label.grid(column=1, row=0) 

# check label:
check_label = Label(font=('arial', 20), bg=YELLOW, fg=GREEN)
check_label.grid(column=1, row=3)  















window.mainloop() 