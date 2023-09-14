# Importing all libraries to create an calendar
from tkinter import *
import calendar
import time
# from datetime import date
# import main
from tkcalendar import Calendar
from functools import partial
# from calendar import timegm
from playsound import playsound
from datetime import datetime as dtx
import datetime as dt
import pytz
import datetime

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        # current_time = datetime.datetime.now()
        now = int(time.time())
        # set_alarm_timer = time.strptime(selected_date.split(": ")[1]+".807Z","%Y-%m-%dT%H:%M:%S.%fZ")
        # set_alarm_timer = timegm(set_alarm_timer)+7200
        # date = current_time.strftime("%d/%m/%Y")
        # print("Data stabilita este: ", selected_date)
        print(set_alarm_timer)
        if now == set_alarm_timer:
            print("E timpul sa te trezesti!!")
            playsound("music.mp3")
            break

def event():
    month = int(month_box.get())
    year = int(year_box.get())
    output_calendar = calendar.month(year, month)
    calendar_field.delete(1.0, 'end')
    calendar_field.insert('end', output_calendar)

def timpul_actual(selected_date, hour, min, sec):
    selected_date = selected_date["text"].split(": ")[1] + f" {hour.get()}:{min.get()}:{sec.get()}"

    # tz_string = 'Europe/Bucharest'

    # Create a timezone object
    # tz = timezone(tz_string)

    # Parse the datetime string
    # dt = datetime.strptime(selected_date+".807Z", '%Y-%m-%d %H:%M:%S.%fZ')
    # set_alarm_timer = timegm(dt)

    # print(dt)
    # alarm(set_alarm_timer)
    # print(set_alarm_timer)

    romania_timezone = pytz.timezone("Europe/Bucharest")
    datetime_with_timezone = romania_timezone.localize(dtx.strptime(selected_date, "%Y-%m-%d %H:%M:%S"))

    set_alarm_timer = int(datetime_with_timezone.timestamp())

    print(set_alarm_timer)

def update_date(calendarul, selected_date):
    # date.config(text="Data selectata este: " + tkc.get_date())
    print(calendarul.selection_get())
    selected_date.config(text="Data selectata este: " + str(calendarul.selection_get()))

def close():
    guiWindow.destroy()

def start_cal():
    guiWindow = Tk()
    guiWindow.title("Calendarul anului")
    guiWindow.geometry('875x475')
    guiWindow.resizable()
    guiWindow.configure(bg="purple")

    tkc = Calendar(guiWindow, selectmode="day",
                   background='blue',
                   foreground='black',
                   selectbackground='darkblue',
                   normalbackground='blue',
                   weekendbackground='lightblue',
                   weekendforeground='black')

    tkc.pack(pady=20)

    selected_date = Label(guiWindow, text="Afisare data", bg='blue', fg='white')
    selected_date.pack(pady=20)

    button = Button(guiWindow, text="Selectare data", command=partial(update_date, tkc, selected_date), bg="turquoise", fg='red')
    button.pack()

    time_format = Label(guiWindow, text="Introduceti ora de pe ceas", fg="green", bg="red",
                        font=("Times", 14, "italic"))

    time_format.place(x=325, y=375)

    add_time = Label(guiWindow, text="Hour        Min          Sec", font=70, background="purple")

    add_time.place(x=300, y=325)

    set_your_alarm = Label(guiWindow, text="Te vei trezi la:", fg="orange", relief="solid",
                           font=("Times", 12, "bold", "italic"), bg="purple")

    set_your_alarm.place(x=197, y=347)

    hour = StringVar()
    min = StringVar()
    sec = StringVar()

    hour_time = Entry(guiWindow, textvariable=hour, bg="turquoise", width=15)
    min_time = Entry(guiWindow, textvariable=min, bg="turquoise", width=15)
    sec_time = Entry(guiWindow, textvariable=sec, bg="turquoise", width=15)

    hour_time.place(x=300, y=350)
    min_time.place(x=390, y=350)
    sec_time.place(x=480, y=350)

    submit = Button(guiWindow, text="Seteaza alarma", fg="red", width=12, command=partial(timpul_actual, selected_date, hour_time, min_time, sec_time))

    submit.place(x=380, y=405)

    guiWindow.mainloop()

if __name__ == "__main__":
    start_cal()