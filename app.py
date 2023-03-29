from functions import AlarmClock
time_string = input('Enter the time for the alarm in %H:%M:%S format')
status = True
while True:
    my_alarm = AlarmClock(time_string)
    print(my_alarm.time, end='')
    status = my_alarm.sound_alarm()
    print(end='\r')
    if status is False:
        break
    print(end='\r')