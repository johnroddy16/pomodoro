# another way to write the timer function:

import math 

# after simply tells the gui to wait an amount of time is ms, then calls a function with the args provided

def timer_start(count): # count is in seconds
    minutes = math.floor(count / 60)
    seconds = count % 60 
    
    # add canvas.itemconfig(timer_text, text=....)
    
    if count > 0:
        pass 
        # add window.after(1000, timer_start, count-1)
        
    # we will look into dynamic typing to learn more about ways to display the data 
    
# original timer function:
def timer_start(minutes=25, seconds=0):
    if minutes >= 0 and seconds >= 0:
        # format the time as MM:SS
        time_str = f'{minutes:02}:{seconds:02}'
        # update canvas text:
        # canvas.itemconfig(timer_text, text=time_str)
        
        # get the next times:
        if seconds == 0:
            minutes -= 1 
            seconds = 59 
        else:
            seconds -= 1 
            
        # schedule the next step:
        if minutes >= 0 or seconds >= 0:
            pass 
            # window.after(1000, timer_start, minutes, seconds)  