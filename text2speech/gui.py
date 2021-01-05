import pyttsx3
import tkinter as tk

window = tk.Tk()


def play_sound():
    # data = "Whatever"
    engine = pyttsx3.init()
    engine.say(entry.get())
    engine.runAndWait()
    entry.delete(0, "end")


window.title("I PLAY POKEMON GO EVERYDAY")
frame = tk.Frame(window)

label = tk.Label(frame, text="ENTER YOR CREDIT CARD INFO")
label.pack()

entry = tk.Entry(frame, width=50)
entry.pack(pady=8)
frame.place(relx=0.5, rely=0.5, anchor='center')

button = tk.Button(frame, text="Play", bg="#c0e7fa", command=play_sound)
button.pack()

window.geometry('360x120')
window.mainloop()
