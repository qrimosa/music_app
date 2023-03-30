import customtkinter as ctk
import modules.creating_screen as m_app
import PIL
import modules.find_path as m_path
from pygame import mixer

mixer.init()

list_big_images = ["images/pause.png", "images/play.png", "images/stop.png",]

def image_finder0():
    return ctk.CTkImage(
        dark_image = PIL.Image.open(m_path.find_path_to_file(list_big_images[0])), 
        size = (160, 58)
    )

def image_finder1():
    return ctk.CTkImage(
        dark_image = PIL.Image.open(m_path.find_path_to_file(list_big_images[1])), 
        size = (160, 58)
    )

def image_finder2():
    return ctk.CTkImage(
        dark_image = PIL.Image.open(m_path.find_path_to_file(list_big_images[2])), 
        size = (160, 58)
    )

def play():
    mixer.music.play()

def stop():
    mixer.music.stop()

def pause():
    mixer.music.pause()

def create_button(master, img, command, text = "", width = 1, height= 5, border_width= 4, corner_radius = 15, border_color = "#4CB7CE"):
    button = ctk.CTkButton(
        master = master,
        image = img,
        width = width,
        height = height,
        border_width = border_width,
        corner_radius = corner_radius,
        border_color = border_color,
        text = text,
        fg_color= "transparent",
        hover_color = "lightblue",
        command = command
    )
    return button 

bt_play = create_button(master= m_app.app, img= image_finder1(), command = play)
bt_play.place(x = 356, y = 95, anchor = ctk.CENTER)

bt_pause = create_button(master= m_app.app, img= image_finder0(), command = pause)
bt_pause.place(x = 356, y = 253, anchor = ctk.CENTER)

bt_stop = create_button(master= m_app.app, img= image_finder2(), command = stop)
bt_stop.place(x = 356, y = 333, anchor = ctk.CENTER)