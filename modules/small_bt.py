import customtkinter as ctk
import modules.creating_screen as m_app
import modules.find_path as m_path
import PIL
import random
from pygame import mixer
import modules.frame_bt as m_f_bt
from tkinter import filedialog



mixer.init()

list_images = ["images/add.png", "images/del.png", "images/mix.png","images/soundDown.png", "images/soundUp.png","images/return.png", "images/skip.png"]
list_songs_name = ["songs/despasito.mp3", "songs/myself.mp3", "songs/nostylist.mp3","songs/omsk.mp3", "songs/paranoid.mp3", "songs/pokolenie.mp3", "songs/slimshady.mp3"]
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
        hover_color = "lightblue", 
        command = command
    )
    return button


def mix():
    random_num = random.randint(0, 6) 
    if random_num == 0:
        mixer.music.load(m_path.find_path_to_file(list_songs_name[0]))
        mixer.music.play()
    elif random_num == 1:
        mixer.music.load(m_path.find_path_to_file(list_songs_name[1]))
        mixer.music.play()
    elif random_num == 2:
        mixer.music.load(m_path.find_path_to_file(list_songs_name[2]))
        mixer.music.play()
    elif random_num == 3:
        mixer.music.load(m_path.find_path_to_file(list_songs_name[3]))
        mixer.music.play()
    elif random_num == 4:
        mixer.music.load(m_path.find_path_to_file(list_songs_name[4]))
        mixer.music.play()
    elif random_num == 5:
        mixer.music.load(m_path.find_path_to_file(list_songs_name[5]))
        mixer.music.play()
    elif random_num == 6:
        mixer.music.load(m_path.find_path_to_file(list_songs_name[6]))
        mixer.music.play()

def abc():
    label_display8 = ctk.CTkLabel(master = m_app.app, text = 'Blinding Lights | Weeknd', font= label_font, text_color= "black")
    m_f_bt.label_image1._text = 'Blinding Lights | Weeknd'
    label_display8.place(x = 351, y = 45, anchor = ctk.CENTER)
    m_f_bt.label_display1.place(x = 1000, y = 45, anchor = ctk.CENTER)
    m_f_bt.label_display2.place(x = 1000, y = 45, anchor = ctk.CENTER)
    m_f_bt.label_display3.place(x = 1000, y = 45, anchor = ctk.CENTER)
    m_f_bt.label_display4.place(x = 1000, y = 45, anchor = ctk.CENTER)
    m_f_bt.label_display5.place(x = 1000, y = 45, anchor = ctk.CENTER)
    m_f_bt.label_display6.place(x = 1000, y = 45, anchor = ctk.CENTER)
    m_f_bt.label_display7.place(x = 1000, y = 45, anchor = ctk.CENTER)

def delete_music():
    if m_f_bt.label_image1._text == "Despacito | Luis Fonsi":
        m_f_bt.button1.place(x = 1000, y = 15, anchor = ctk.CENTER)
    elif m_f_bt.label_image1._text == "NOSTYLIST | Destroy Lonely":
        m_f_bt.button2.place(x = 1000, y = 15, anchor = ctk.CENTER)
    elif m_f_bt.label_image1._text == "Paranoid | Black Sabbath":
        m_f_bt.button3.place(x = 1000, y = 15, anchor = ctk.CENTER)
    elif m_f_bt.label_image1._text == "Город Омск | Смешарики":
        m_f_bt.button4.place(x = 1000, y = 15, anchor = ctk.CENTER)
    elif m_f_bt.label_image1._text == "Новое Поколение | Melham":
        m_f_bt.button5.place(x = 1000, y = 15, anchor = ctk.CENTER)
    elif m_f_bt.label_image1._text == "The Real Slim Shady | Eminem":
        m_f_bt.button6.place(x = 1000, y = 15, anchor = ctk.CENTER)
    elif m_f_bt.label_image1._text == "Myself | Yeat":
        m_f_bt.button7.place(x = 1000, y = 15, anchor = ctk.CENTER)

def add_music():
    filename = filedialog.askopenfilename(initialdir="/", title= "Select a song to play")
    mixer.music.load(filename)
    filename = filename.split("/")
    del filename[1]
    del filename[1]
    del filename[1]
    del filename[1]
    new_song = m_f_bt.create_button(master = m_app.app.FRAME, text= filename, command= abc)
    new_song.pack(padx = 15, pady = 5)
    m_f_bt.label_image1._text = filename
    return filename


def skip_track():
    if m_f_bt.label_image1._text == "Despacito | Luis Fonsi":
        mixer.music.load(m_path.find_path_to_file(list_songs_name[2]))
        mixer.music.play()
    elif m_f_bt.label_image1._text == "NOSTYLIST | Destroy Lonely":
        mixer.music.load(m_path.find_path_to_file(list_songs_name[4]))
        mixer.music.play()
    elif m_f_bt.label_image1._text == "Paranoid | Black Sabbath":
        mixer.music.load(m_path.find_path_to_file(list_songs_name[3]))
        mixer.music.play()
    elif m_f_bt.label_image1._text == "Город Омск | Смешарики":
        mixer.music.load(m_path.find_path_to_file(list_songs_name[5]))
        mixer.music.play()
    elif m_f_bt.label_image1._text == "Новое Поколение | Melham":
        mixer.music.load(m_path.find_path_to_file(list_songs_name[6]))
        mixer.music.play()
    elif m_f_bt.label_image1._text == "The Real Slim Shady | Eminem":
        mixer.music.load(m_path.find_path_to_file(list_songs_name[1]))
        mixer.music.play()
    elif m_f_bt.label_image1._text == "Myself | Yeat":
        mixer.music.load(m_path.find_path_to_file(list_songs_name[0]))
        mixer.music.play()
        
def return_track():
    if m_f_bt.label_image1._text == "Despacito | Luis Fonsi":
        mixer.music.load(m_path.find_path_to_file(list_songs_name[1]))
        mixer.music.play()
    elif m_f_bt.label_image1._text == "NOSTYLIST | Destroy Lonely":
        mixer.music.load(m_path.find_path_to_file(list_songs_name[0]))
        mixer.music.play()
    elif m_f_bt.label_image1._text == "Paranoid | Black Sabbath":
        mixer.music.load(m_path.find_path_to_file(list_songs_name[2]))
        mixer.music.play()
    elif m_f_bt.label_image1._text == "Город Омск | Смешарики":
        mixer.music.load(m_path.find_path_to_file(list_songs_name[4]))
        mixer.music.play()
    elif m_f_bt.label_image1._text == "Новое Поколение | Melham":
        mixer.music.load(m_path.find_path_to_file(list_songs_name[3]))
        mixer.music.play()
    elif m_f_bt.label_image1._text == "The Real Slim Shady | Eminem":
        mixer.music.load(m_path.find_path_to_file(list_songs_name[5]))
        mixer.music.play()
    elif m_f_bt.label_image1._text == "Myself | Yeat":
        mixer.music.load(m_path.find_path_to_file(list_songs_name[6]))
        mixer.music.play()
        
def sound_up():
    mixer.music.set_volume(1.0)
    
def sound_down():
    mixer.music.set_volume(0.1)

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