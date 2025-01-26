# another way to write the timer function:

import math 

def timer_start(count): # count is in seconds
    minutes = math.floor(count / 60)
    seconds = count % 60 
    
    # add canvas.itemconfig(timer_text, text=....)
    
    if count > 0:
        pass 
        # add window.after(1000, timer_start, count-1)
        
    # we will look into dynamic typing to learn more about ways to display the data 