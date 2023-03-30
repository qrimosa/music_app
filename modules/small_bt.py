import customtkinter as ctk
import modules.creating_screen as m_app
import modules.find_path as m_path
import PIL
import random

list_images = ["images/add.png", "images/del.png", "images/mix.png","images/soundDown.png", "images/soundUp.png","images/return.png", "images/skip.png"]
list_songs_name = ["songs/despasito.mp3", "songs/myself.mp3", "songs/nostylist.mp3","songs/omsk.mp3", "songs/paranoid.mp3", "songs/pokolenie.mp3", "songs/slimshady.mp3"]

def image_finder0():
    return ctk.CTkImage(
        dark_image = PIL.Image.open(m_path.find_path_to_file(list_images[0])), 
        size = (61, 58)
    )
def image_finder1():
    return ctk.CTkImage(
        dark_image = PIL.Image.open(m_path.find_path_to_file(list_images[1])), 
        size = (61,58)
    )
def image_finder2():
    return ctk.CTkImage(
        dark_image = PIL.Image.open(m_path.find_path_to_file(list_images[2])), 
        size = (61, 58)
    )
def image_finder3():
    return ctk.CTkImage(
        dark_image = PIL.Image.open(m_path.find_path_to_file(list_images[3])), 
        size = (61, 58)
    )
def image_finder4():
    return ctk.CTkImage(
        dark_image = PIL.Image.open(m_path.find_path_to_file(list_images[4])), 
        size = (61, 58)
    )
def image_finder5():
    return ctk.CTkImage(
        dark_image = PIL.Image.open(m_path.find_path_to_file(list_images[5])), 
        size = (61, 58)
    )
def image_finder6():
    return ctk.CTkImage(
        dark_image = PIL.Image.open(m_path.find_path_to_file(list_images[6])), 
        size = (61, 58)
    )

def mix():
    random.randint(0, 6)

def create_button(master, img, command, text = "", width = 1, height = 8, border_width = 4, corner_radius = 15, border_color = "#4CB7CE"):
    button = ctk.CTkButton(
        master = master,
        image = img,
        width = width,
        height = height,
        border_width = border_width,
        corner_radius = corner_radius,
        border_color = border_color,
        text = text, 
        fg_color = "transparent",
        hover_color = "lightblue", 
        command = command
    )
    return button


# bt_skip = create_button(master = m_app.app, img = image_finder6())
# bt_skip.place(x = 305, y = 175, anchor = ctk.CENTER)
# 
# bt_return = create_button(master = m_app.app, img = image_finder5())   
# bt_return.place(x = 406, y = 175, anchor = ctk.CENTER) 
# 
# bt_sound_decrease = create_button(master = m_app.app, img = image_finder3())
# bt_sound_decrease.place(x = 406, y = 406, anchor = ctk.CENTER) 
# 
# bt_sound_increase = create_button(master = m_app.app, img = image_finder4())
# bt_sound_increase.place(x = 313, y = 406, anchor = ctk.CENTER)
# 
# bt_delete = create_button(master = m_app.app, img = image_finder1())
# bt_delete.place(x = 141, y = 406, anchor = ctk.CENTER)
# 
# bt_add = create_button(master = m_app.app, img = image_finder0())
# bt_add.place(x = 55, y = 406, anchor = ctk.CENTER)

bt_mix = create_button(master = m_app.app, img = image_finder2(), command = mix)
bt_mix.place(x = 228 , y = 406 , anchor = ctk.CENTER)