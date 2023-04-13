import customtkinter as ctk
import modules.creating_screen as m_app
import modules.find_path as m_path
import PIL
import random
from pygame import mixer
from tkinter import filedialog
import modules.creating_list_frame as m_listbox
# import fnmatch
import os

volume = 0.5
mixer.init()

list_images = ["images/add.png", "images/del.png", "images/mix.png","images/soundDown.png", "images/soundUp.png","images/return.png", "images/skip.png"]
label_font = ctk.CTkFont(size= 12, weight= "bold", family= "Montserrat")

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

def create_button(master, img, command, text = "", width = 1, height = 8, border_width = 4, corner_radius = 15, border_color = "#4CB7CE"):
    button = ctk.CTkButton(
        master = master,
        image = img,
        text = text,
        width = width,
        height = height,
        border_width = border_width,
        corner_radius = corner_radius,
        border_color = border_color, 
        fg_color = "transparent",
        hover= False, 
        command = command
    )
    return button


def mix():
    lisbox_length = m_listbox.listbox.size() - 1
    random_num = random.randint(0, lisbox_length) 
    # file = m_listbox.listbox.curselection()
    # filename = m_listbox.listbox.get(file)
    # mixer.music.load(filename)
    # m_listbox.song_label.configure(text = filename)
    # mixer.music.play()

    m_listbox.listbox.selection_clear(0, 'end')
    m_listbox.listbox.activate(random_num)
    m_listbox.listbox.selection_set(random_num)

def delete_music():
    del_file = m_listbox.listbox.curselection()
    m_listbox.listbox.delete(del_file)
    m_listbox.song_label.configure(text = "")
    mixer.music.stop()

# def add_music():
#     path = filedialog.askopenfilename()
#     if path:
#         abc = path.split("/")
#         m_listbox.listbox.insert("end", abc[-1])
            
def add_music():
    path = filedialog.askdirectory()
    if path:
        os.chdir(path)
        songs = os.listdir(path)
        for song in songs:
            if song.endswith(".mp3"):
                m_listbox.listbox.insert("end", song)

def skip_track():
    try:
        next_song = m_listbox.listbox.curselection()
        next_song = next_song[0] + 1
        next_song_name = m_listbox.listbox.get(next_song)
        m_listbox.song_label.configure(text = next_song_name) 
        mixer.music.load(next_song_name)
        mixer.music.play()

        m_listbox.listbox.select_clear(0, "end")
        m_listbox.listbox.activate(next_song)
        m_listbox.listbox.select_set(next_song)
    except:
        print("Index out of range!")

def return_track():
    try:
        next_song = m_listbox.listbox.curselection()
        next_song = next_song[0] - 1
        next_song_name = m_listbox.listbox.get(next_song)
        m_listbox.song_label.configure(text = next_song_name) 
        mixer.music.load(next_song_name)
        mixer.music.play()

        m_listbox.listbox.select_clear(0, "end")
        m_listbox.listbox.activate(next_song)
        m_listbox.listbox.select_set(next_song)
    except:
        print("Index out of range!")


def sound_up():
    global volume
    if volume < 1:
        volume = volume + 0.1
        volume = round(volume, 1)
        mixer.music.set_volume(volume)
        print(volume)
    else:
        print("Volume is maxed!")
    
def sound_down():
    global volume
    if volume > 0:
        volume = volume - 0.1
        volume = round(volume, 1)
        mixer.music.set_volume(volume)
        print(volume)
    else:
        print("Sound is muted!")

bt_skip = create_button(master = m_app.app, img = image_finder6(), command = skip_track)
bt_skip.place(x = 305, y = 175, anchor = ctk.CENTER)

bt_return = create_button(master = m_app.app, img = image_finder5(), command = return_track)   
bt_return.place(x = 406, y = 175, anchor = ctk.CENTER) 

bt_sound_decrease = create_button(master = m_app.app, img = image_finder4(), command = sound_up)
bt_sound_decrease.place(x = 406, y = 406, anchor = ctk.CENTER) 

bt_sound_increase = create_button(master = m_app.app, img = image_finder3(), command = sound_down)
bt_sound_increase.place(x = 313, y = 406, anchor = ctk.CENTER)

bt_delete = create_button(master = m_app.app, img = image_finder1(), command = delete_music)
bt_delete.place(x = 141, y = 406, anchor = ctk.CENTER)

bt_add = create_button(master = m_app.app, img = image_finder0(), command = add_music)
bt_add.place(x = 55, y = 406, anchor = ctk.CENTER)

bt_mix = create_button(master = m_app.app, img = image_finder2(), command = mix)
bt_mix.place(x = 228 , y = 406 , anchor = ctk.CENTER)