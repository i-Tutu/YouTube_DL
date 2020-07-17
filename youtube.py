#! python3
"""
This is a simple program to download video from youtube
Named Link DL. DL DownLoad

This program was coded under Nadomso
"""

import tkinter as tk
from tkinter.ttk import Style
from tkinter import filedialog, messagebox, StringVar
import tkinter.ttk as ttk
import os
from pytube import YouTube  

class link_dl:
    def __init__(self, root):
        self.root = root
        self.styles = Style()
        self.main_layer()
        self.creating_titleAndbrand()
        self.creating_urlHolder()
        self.buttons_AudioVideo()
        
    def main_layer(self):
        self.root.title('Link DL')
        self.root.geometry('450x250')
        self.root.resizable(0, 0)

    def creating_titleAndbrand(self):
        self.label_title = ttk.Label(root, text = 'Link DL - Youtube Downloader', font = 30)
        self.label_title.place(relx = 0.31, rely = 0.12)
        self.label_brand = ttk.Label(root, text = 'Coded under Nadomso')
        self.label_brand.place(relx = 0.4, rely = 0.9)

    def creating_urlHolder(self):
        self.label_url = ttk.Label(root, text = 'URL ')
        self.label_url.place(relx = 0.1, rely = 0.3)
        self.url_link = StringVar()
        self.entry_url = ttk.Entry(root, width = 50, textvariable = self.url_link)
        self.entry_url.focus()
        self.entry_url.place(relx = 0.2, rely = 0.3)

    def buttons_AudioVideo(self):
        def audio_download():
            
            if self.url_link.get() == '':
                messagebox.showinfo(message = 'URL can not be empty')
            else:
                dl_audio = YouTube(self.url_link.get()).streams
                get_audio = dl_audio.filter(type = 'audio')
                get_audio.first().download(output_path = tk.filedialog.askdirectory())
                messagebox.showinfo(message = 'Download Complete')

        def video_download():
          
            if self.url_link.get() == '':
                messagebox.showinfo(message = 'URL can not be empty')
            else:
                dl_video = YouTube(self.url_link.get()).streams.first()
                dl_video.download(output_path = tk.filedialog.askdirectory())
                messagebox.showinfo(message = 'Download Complete')
            
        self.audio_button = ttk.Button(root, text = 'Audio', command = audio_download)
        self.video_button = ttk.Button(root, text = 'Video', command = video_download)
        self.audio_button.place(relx = 0.25, rely = 0.65)
        self.video_button.place(relx = 0.55, rely = 0.65)
        self.styles.configure('TButton', relief = 'flat', background = '#fff', font = 10, padding = 2)
        
    

if __name__ == '__main__':
    root = tk.Tk()
    link_dl(root)
    root.mainloop()
