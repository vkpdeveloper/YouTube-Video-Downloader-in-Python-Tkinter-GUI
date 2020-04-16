import tkinter as tk
from tkinter import ttk
import os
from pytube import YouTube
from tkinter import messagebox as m_box
import subprocess
import threading

def onClick():
    got_link = link.get()
    got_path = path.get()
    try:
        yt = YouTube(str(got_link))
    except:
        m_box.showerror("Error", "Connection Problem !")
    else:
        vid = yt.streams.get_highest_resolution()
        destination = str(got_path)
        vid.download(destination)
        os.startfile(got_path)
        return m_box.showinfo('Successfully Downloaded.', f"Your YouTube Vidoe Downloaded Successfully at {got_path}/{yt.title}")


threads = []


def startThredProcess():
    myNewThread = threading.Thread(target=onClick)
    threads.append(myNewThread)
    myNewThread.start()

win = tk.Tk()
win.geometry("500x400")
win.title("YouTube Video Downloader")
win.minsize(500, 400)
win.maxsize(500, 400)
frame = ttk.LabelFrame(win)
frame.grid(row=0, column=0, padx=70, pady=90)

get_info = ttk.Label(frame, text="Enter YouTube Video Link : ")
get_info.grid(row=0, column=0, sticky=tk.W)

link = tk.StringVar()

yt_link = ttk.Entry(frame, width=60, textvariable=link)
yt_link.grid(row=1, columnspan=3, padx=0, pady=3)
yt_link.focus()

get_info = ttk.Label(frame, text="Enter Downloading Path : ")
get_info.grid(row=3, column=0, sticky=tk.W)

path = tk.StringVar()

download_path = ttk.Entry(frame, width=60, textvariable=path)
download_path.grid(row=4, columnspan=3, padx=0, pady=3)

btn1 = ttk.Button(frame, text="Download Video",
                  width=15, command=startThredProcess)
btn1.grid(row=7, columnspan=3, padx=13, pady=7)

win.mainloop()
