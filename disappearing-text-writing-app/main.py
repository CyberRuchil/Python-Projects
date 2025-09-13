from tkinter import *

# ------------------------ Functions ------------------------

def start():
    '''
    This function starts the application.
    '''
    global start_btn
    start_btn.destroy() # Destroy's the global start_btn widget.

    time_label.grid(column=0, row=1, pady=(0,20)) # Displays the timer.
    timer(5) 

    text.config(state='normal') 
    text.grid(column=0,row=2) # Displays the text field.
    text.focus()


def end():
     '''
     This function deletes all the text inside the text field and change the state of the fiekd to disabled.
     '''
     text.delete('1.0',END) 
     text.config(state='disabled')
    

def timer(count:int):
        '''
        This function starts the timer.

        Parameters
        ---------
        count : It is the number of second we want the timer to run for.
        '''
        count_sec = count % 60
        count_min = int(count / 60)

        if count_sec < 10:
            count_sec = f"0{count_sec}" 

        if count_min < 10:
            count_min = f"0{count_min}"  

        time_label.config(text=f'Timer: {count_min}:{count_sec}')

        if count > 0:
            time = window.after(1000,timer,count-1)

        else:
            global start_btn
            end()
            start_btn = Button(text='Start Again', command=start)
            start_btn.grid(column=0, row=3, pady=(20,0))


# ------------------------ Application ------------------------

window = Tk()
window.title('Disappearing Text Writing App')
window.minsize(1000,600)

title = Label(text='Disappearing Text Writing', font=('',32,'bold'), width=50)
title.grid(column=0,row=0, pady=40)

time_label = Label(text='Timer: 00:00', font=('', 18)) 

start_btn = Button(text='Start Writing', command=start)
start_btn.grid(column=0, row=1)

text = Text(highlightthickness=3, highlightcolor='black', relief='flat')
text.config(width=60, height=10, font=('', 18), wrap='word')

window.mainloop()