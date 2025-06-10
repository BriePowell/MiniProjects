# Imports

import tkinter as tk
from tkinter import messagebox
from PIL import Image,ImageTk
from playsound import playsound
import time


class Pomodoro:
    def __init__(self, root):
        self.root = root

    def work_break(self, timer):
        #display minutes and seconds on GUI
        minutes, seconds = divmod(timer, 60)
        self.min.set(f"{minutes:02d}")
        self.sec.set(f"{seconds:02d}")
        self.root.update()
        time.sleep(1)

    
    def work(self):
        timer = 45*60
        while timer>= 0:
            pomo.work_break(timer)
            if timer == 0:
                playsound("sound.ogg")
                messagebox.showinfo("Take a break...and blink")
            timer -=1

    def break_(self):
        timer = 5*60
        while timer >= 0:
            pomo.work_break(timer)
            if timer == 0:
                playsound("sound.ogg")
                messagebox.showinfo("Times up", "Back to work")
            timer -= 1

    def main(self):
        #GUI window configuration
        self.root.geometry("650x650")
        self.root.resizable(False, False)
        self.root.title("Pomodoro Timer")

        #label
        self.min = tk.StringVar(self.root)
        self.min.set("45")
        self.sec = tk.StringVar(self.root)
        self.sec.set("00")

        self.min_label = tk.Label(self.root,
                                  textvariable=self.min,
                                  font=("arial", 22, "bold"), bg="blue", fg='black')
        self.min_label.pack()

        self.sec_label = tk.Label(self.root,
                                  textvariable=self.sec, 
                                  font=("arial", 22, "bold"), bg="blue", fg='black')
        self.sec_label.pack()

        #add background image for GUI
        canvas = tk.Canvas(self.root)
        canvas.pack(expand=True, fill="both")
        img = Image.open('timer1.jpg')
        bg = ImageTk.PhotoImage(img)
        canvas.create_image(90, 10, image=bg, anchor="nw")

        #create three buttons with countddown function command
        btn_work = tk.Button(self.root,
                             text="Start",
                             bd=5,
                             command=self.work,
                             bg="SlateGrey",
                             font=("arial", 15, "bold")).place(x=140, y=380)
        btn_break = tk.Button(self.root,
                             text="Break",
                             bd=5,
                             command=self.work,
                             bg="SlateGrey",
                             font=("arial", 15, "bold")).place(x=240, y=380)
        self.root.mainloop()

if __name__ == '__main__':
    pomo = Pomodoro(tk.Tk())
    pomo.main()