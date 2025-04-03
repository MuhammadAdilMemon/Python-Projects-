import tkinter as tk
from tkinter import ttk, simpledialog, messagebox
from time import strftime
import threading
import pygame
import speech_recognition as sr
import re

alarms=[]

root=tk.Tk()
root.title("Digital clock")

width=400
height=300
ww=root.winfo_screenwidth()
wh=root.winfo_screenheight()
x=(ww-width)/2
y=(wh-height)/2


def timer():
    current_time=strftime("%H:%M:%S")
    label.config(text=current_time)

    for alarm in alarms:
        if alarm==current_time:
            threading.Thread(target=trigger_alarm).start()
            alarms.remove(alarm)
    label.after(1000,timer)



def trigger_alarm():
    pygame.mixer.init()
    pygame.mixer.load("alarm.mp3")
    pygame.mixer.play()
    messagebox.showinfo("Alarm", "Hey! it's time to wake up")

def set_alarm():
    set_alarm_time=simpledialog.askstring("Set Alarm", "Enter time in HH:MM:SS format")
    if set_alarm_time and validate_time(set_alarm_time):
        alarms.append(set_alarm_time)
        messagebox.showinfo("Alarm set", f"Alarm set for {set_alarm_time}")
    else:
        messagebox.showerror("Invalid time", "Please enter a valid time in HH:MM:SS format.")

def validate_time(time_str):
    return re.match(r"^([01]\d|2[0-3]):[0-5]\d:[0-5]\d$", time_str) is not None

def parse_time_from_text(text):
    text=text.lower()
    text=text.replace("set alarm for", "").replace("o'clock","").strip()
    time_match = re.match(r"(\d{1,2})(?:\s|:)(\d{1,2})?", text)
    if time_match:
        hours=int(time_match.group(1))
        minutes = int(time_match.group(2)) if time_match.group(2) else 0
        if 0 <= hours <= 23 and 0 <= minutes <= 59:
            return f"{hours:02}:{minutes:02}:00"
    return None

def listen():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        try:
            status_label.config(text="Listening for alarm time...")
            root.update()

            audio=r.listen(source,timeout=10)
            text=r.recognize_google(audio)
            print(f"Recognized Text : {text}")

            parsed_time=parse_time_from_text(text)
            if parsed_time and validate_time(parsed_time):
                alarms.append(parsed_time)
                messagebox.showinfo("Alarm set", f"Alarm set for {parsed_time}")
            else:
                messagebox.showerror("Invalid Time", "Could not recognize a valid time format. Please try again.")

        except sr.UnknownValueError:
            messagebox.showerror("Error", "Sorry, could not understand your voice. Please try again.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
        finally:
            status_label.config(text="")

style=ttk.Style()
style.theme_use("clam")

style.configure("TButton", padding=10, font=("lato", 12, "bold"), boderwidth=0)
style.configure("Rounded.TButton", relief="flat",background="#4CAF50", foreground="white")
style.map("Rounded.TButton",background=[("active", "#45a049")] )

label=tk.Label(root,font=("Roboto", 50, "bold"), background="#f7f7f7", foreground="#333333")
label.pack(anchor="center", pady=20)

set_alarm_btn=ttk.Button(root, text="Set Alarm", command=set_alarm, style="Rounded.TButton")
set_alarm_btn.pack(anchor="center", pady=10)

voice_alarm_btn = ttk.Button(root, text="Voice Set Alarm", command=listen, style="Rounded.TButton")
voice_alarm_btn.pack(anchor="center", pady=10)
status_label = tk.Label(root, text="", font=("Lato", 10), background="#f7f7f7", foreground="#666666")
status_label.pack(anchor="center", pady=5)

# Set window geometry
root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')
root.configure(background="#f7f7f7")
timer()
root.mainloop()





