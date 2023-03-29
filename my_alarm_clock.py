import threading
import queue
import tkinter as tk
import functions as fc


win = tk.Tk()
win.geometry("700x400")
win.title('Alarm clock')
frame = tk.Frame(win)
frame.pack()
    
set_label = tk.Label(frame, font=("Arial", 30), text="Set alarm time (format: HH:MM:SS)")
set_label.pack(padx=20, pady=20)
    
entry = tk.Entry(frame, font=("Arial", 30))
entry.pack(padx=20, pady=20)

def set_alarm():
    time_str = entry.get()
    fc.AlarmClock.start_alarm(time_str)
    
button = tk.Button(frame, font=("Arial", 30), text="Set Alarm", command=set_alarm)
button.pack(padx=20, pady=20)
button.pack(padx=20, pady=20)

win.mainloop()
    