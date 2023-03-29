import customtkinter as ctk
import modules.creating_screen as m_app
import modules.find_path as m_path
import PIL

list_images = ["images/add.png", "images/del.png", "images/mix.png","images/soundDown.png", "images/soundUp.png","images/return.png", "images/skip.png"]

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

def create_button(master, img, text = "", width = 61, height = 58, border_width = 4, corner_radius = 15, border_color = "#4CB7CE"):
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
        hover_color = "lightblue"
    )
    return button

label_image = ctk.CTkLabel(master = m_app.app, text = "назва треку що грає")
label_image.place(x = 341, y = 40, anchor = ctk.CENTER)

bt_skip = create_button(master = m_app.app, img = image_finder6())
bt_skip.place(x = 288, y = 165, anchor = ctk.CENTER)

bt_return = create_button(master = m_app.app, img = image_finder5())   
bt_return.place(x = 396, y = 165, anchor = ctk.CENTER) 

bt_sound_decrease = create_button(master = m_app.app, img = image_finder3())
bt_sound_decrease.place(x = 396, y = 396, anchor = ctk.CENTER) 

bt_sound_increase = create_button(master = m_app.app, img = image_finder4())
bt_sound_increase.place(x = 303, y = 396, anchor = ctk.CENTER)

bt_delete = create_button(master = m_app.app, img = image_finder1())
bt_delete.place(x = 131, y = 396, anchor = ctk.CENTER)

bt_add = create_button(master = m_app.app, img = image_finder0())
bt_add.place(x = 45, y = 396, anchor = ctk.CENTER)

bt_mix = create_button(master = m_app.app, img = image_finder2())
bt_mix.place(x = 217 , y = 396 , anchor = ctk.CENTER)