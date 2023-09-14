#Importing all libraries to create an alarm clock
import tkinter as tk
import datetime
import time
from playsound import playsound

def event():
    month = int(month_box.get())
    year = int(year_box.get())
    output_calendar = calendar.month(year, month)
    calendar_field.delete(1.0, 'end')
    calendar_field.insert('end', output_calendar)

def alarm(set_alarm_timer, selected_date):
    while True:
        time.sleep(5)
        # current_time = datetime.datetime.now()
        # now = current_time.strftime("%H:%M:%S")
        # date = current_time.strftime("%d/%m/%Y")
        print("Data stabilita este: ", selected_date.selection_get())
        print(now)
        if now == set_alarm_timer:
            print("E timpul sa te trezesti!!")
        playsound("music.mp3")
        break
def timpul_actual(selected_date):
    set_alarm_timer = "{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer, selected_date)
    print(set_alarm_timer)

def start_clock():
    clock = tk.Tk()
    clock.title("Alarm Clock")
    clock.geometry("400x200")
    time_format = tk.Label(clock, text="Introduceti ora de pe ceas", fg="green", bg="red",
                           font=("Times", 14, "italic")).place(x=60, y=120)
    add_time = tk.Label(clock, text="Hour  Min  Sec", font=70).place(x=110)
    set_your_alarm = tk.Label(clock, text="Te vei trezi la", fg="orange", relief="solid",
                              font=("Times", 8, "bold", "italic")).place(x=0, y=30)

    hour = tk.StringVar()
    min = tk.StringVar()
    sec = tk.StringVar()

    hour_time = tk.Entry(clock, textvariable=hour, bg="turquoise", width=15).place(x=110, y=30)
    min_time = tk.Entry(clock, textvariable=min, bg="turquoise", width=15).place(x=150, y=30)
    sec_time = tk.Entry(clock, textvariable=sec, bg="turquoise", width=15).place(x=200, y=30)

    submit = tk.Button(clock, text="Seteaza alarma", fg="red", width=10, command=timpul_actual).place(x=110, y=70)

    clock.mainloop()

if __name__ == "__main__":
    start_clock()