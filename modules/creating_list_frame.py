import tkinter as tk
import customtkinter as ctk
import modules.creating_screen as m_app
import fnmatch
import os
import modules.find_path as m_path
from pygame import mixer

mixer.init()
mixer.music.set_volume(0.5)

rootpath = "C:\\marat\python\music_app"
pattern = "*.mp3"

listbox = tk.Listbox(master = m_app.app, width= 27, height = 15, bg = "#bdbdbd", fg = "black", font = ("impact", 13))
listbox.place(x = 135, y = 193, anchor = ctk.CENTER)


song_label = ctk.CTkLabel(master = m_app.app, text = "", text_color = "black", font = ("impact", 22))
song_label.place(x = 351, y = 40, anchor = ctk.CENTER)

# for root, dirs, files in os.walk(rootpath):
#     for filename in fnmatch.filter(files, pattern):
#         listbox.insert("end", filename)

