from datetime import datetime
import time
import tkinter as tk
import winsound


class AlarmClock:
    def __init__(self, time_string):
        time_object = datetime.now()
        self.time = time_object.strftime('%H:%M:%S')
        self.alarm = time.strptime(time_string, '%H:%M:%S')

    def sound_alarm(self):
        set_alarm = self.alarm
        hour = set_alarm[3]
        minute = set_alarm[4]
        second = set_alarm[5]

        hour_str = f"{hour:02d}"
        minute_str = f"{minute:02d}"
        second_str = f"{second:02d}"
        time_str = f'{hour_str}:{minute_str}:{second_str}'

        # print(hour_str, minute_str, second_str)  # Output: 12 00 00
        # print(self.time)
        var = self.time
        if time_str in var:
            print("Wake up!")
            frequency = 2500  # Set Frequency To 2500 Hertz
            duration = 1000  # Set Duration To 1000 ms == 1 second
            winsound.Beep(frequency, duration)
        else:
            time.sleep(1)


time_string = input('Enter the time for the alarm in %H:%M:%S format')
while True:
    my_alarm = AlarmClock(time_string)
    print(my_alarm.time, end='')
    my_alarm.sound_alarm()
    print(end='\r')
