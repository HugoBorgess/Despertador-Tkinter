from tkinter import *
import datetime
import time
import winsound
from threading import Thread
from tkinter import messagebox

def criar_interface():
    root = Tk()
    root.geometry("400x200")
    root.title("Despertador")

    Label(root, text="Despertador", font=("Helvetica 20 bold"), fg="red").pack(pady=10)
    Label(root, text="Definir Hora", font=("Helvetica 15 bold")).pack()

    frame = Frame(root)
    frame.pack()

    hour = StringVar(root)
    hours = tuple(str(i).zfill(2) for i in range(25))
    hour.set(hours[0])
    hrs = OptionMenu(frame, hour, *hours)
    hrs.pack(side=LEFT)

    minute = StringVar(root)
    minutes = tuple(str(i).zfill(2) for i in range(61))
    minute.set(minutes[0])
    mins = OptionMenu(frame, minute, *minutes)
    mins.pack(side=LEFT)

    second = StringVar(root)
    seconds = tuple(str(i).zfill(2) for i in range(61))
    second.set(seconds[0])
    secs = OptionMenu(frame, second, *seconds)
    secs.pack(side=LEFT)

    Button(root, text="Definir Alarme", font=("Helvetica 15"), command=lambda: iniciar_despertador(hour, minute, second)).pack(pady=20)

    root.mainloop()

def iniciar_despertador(hour, minute, second):
    hora_alarme = f"{hour.get()}:{minute.get()}:{second.get()}"
    t = Thread(target=despertador, args=(hora_alarme,))
    t.start()

def despertador(hora_alarme):
    while True:
        hora_atual = datetime.datetime.now().strftime("%H:%M:%S")
        if hora_atual >= hora_alarme:
            messagebox.showinfo("Despertador", "Hora de acordar!")
            winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
            break
        time.sleep(1)

criar_interface()
