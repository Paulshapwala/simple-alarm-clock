import tkinter as tk
from functions import AlarmClock, my_time
import time


def start_alarm():
    time_string = input_entry.get()
    
    try:
        my_alarm = AlarmClock(time_string)
    except ValueError:
        status_label.config(text='Invalid time format')
        return 
    status_label.config(text=f'alarm set for  {my_alarm.alarm}')
    
    while my_alarm.sound_alarm():
        
        root.update()
    status_label.config(text='Alarm went off!')
            
         
root = tk.Tk()
time_text = tk.StringVar()
time_text.set(my_time())

time_label = tk.Label(root, text =f'current time:')
time_label.pack()
time_label = tk.Label(root, textvariable=time_text)
time_label.pack()



input_entry = tk.Entry(root)
input_entry.pack()

start_button = tk.Button(root, text='start_alarm', command=start_alarm)
start_button.pack()

status_label = tk.Label(root, text='Alarm not set')
status_label.pack()

# time_string = input('Enter the time for the alarm in %H:%M:%S format')
# status = True
# while True:
#     my_alarm = AlarmClock(time_string)
#     print(my_alarm.time, end='')
#     status = my_alarm.sound_alarm()
#     print(end='\r')
#     if status is False:
#         break
#     print(end='\r')

root.mainloop()