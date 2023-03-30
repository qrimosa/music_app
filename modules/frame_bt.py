import customtkinter as ctk
import modules.creating_screen as m_app
import modules.small_bt as m_sbt
from pygame import mixer
import modules.find_path as m_path

list_songs_name = ["songs/despasito.mp3", "songs/myself.mp3", "songs/nostylist.mp3","songs/omsk.mp3", "songs/paranoid.mp3", "songs/pokolenie.mp3", "songs/slimshady.mp3"]

list_songs = ["Despacito | Luis Fonsi", 
              "NOSTYLIST | Destroy Lonely", 
              "Paranoid | Black Sabbath", 
              "Город Омск | Смешарики", 
              "Новое Поколение | Melham", 
              "The Real Slim Shady | Eminem", 
              "Myself | Yeat"
              ]
label_font = ctk.CTkFont(size= 12, weight= "bold", family= "Montserrat")

def create_button(master, command, text, width = 220, height = 35, border_width = 4, corner_radius = 15):
    button = ctk.CTkButton(
        master = master,
        width = width,
        height = height,
        border_width = border_width,
        corner_radius = corner_radius,
        border_color = "#bdbdbd",
        text = text, 
        fg_color = "transparent",
        hover_color = "lightblue",
        text_color= "black",
        command = command
    )
    return button    

label_image1 = ctk.CTkLabel(master = m_app.app, text = list_songs[0], font= label_font, text_color= "black")
def ls1():
    label_image1.place(x = 351, y = 45, anchor = ctk.CENTER)
    label_image2.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image3.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image4.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image5.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image6.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image7.place(x = 1000, y = 45, anchor = ctk.CENTER)
    mixer.music.load(m_path.find_path_to_file(list_songs_name[0]))

label_image2 = ctk.CTkLabel(master = m_app.app, text = list_songs[1], font= label_font, text_color= "black")
def ls2():
    label_image2.place(x = 351, y = 45, anchor = ctk.CENTER)
    label_image1.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image3.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image4.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image5.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image6.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image7.place(x = 1000, y = 45, anchor = ctk.CENTER)
    mixer.music.load(m_path.find_path_to_file(list_songs_name[2]))

label_image3 = ctk.CTkLabel(master = m_app.app, text = list_songs[2], font= label_font, text_color= "black")
def ls3():
    label_image3.place(x = 351, y = 45, anchor = ctk.CENTER)
    label_image1.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image2.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image4.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image5.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image6.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image7.place(x = 1000, y = 45, anchor = ctk.CENTER)
    mixer.music.load(m_path.find_path_to_file(list_songs_name[4]))
    

label_image4 = ctk.CTkLabel(master = m_app.app, text = list_songs[3], font= label_font, text_color= "black")
def ls4():
    label_image4.place(x = 351, y = 45, anchor = ctk.CENTER)
    label_image1.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image2.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image3.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image5.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image6.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image7.place(x = 1000, y = 45, anchor = ctk.CENTER)
    mixer.music.load(m_path.find_path_to_file(list_songs_name[3]))

label_image5 = ctk.CTkLabel(master = m_app.app, text = list_songs[4], font= label_font, text_color= "black")
def ls5():
    label_image5.place(x = 351, y = 45, anchor = ctk.CENTER)
    label_image3.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image1.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image2.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image4.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image6.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image7.place(x = 1000, y = 45, anchor = ctk.CENTER)
    mixer.music.load(m_path.find_path_to_file(list_songs_name[5]))
    

label_image6 = ctk.CTkLabel(master = m_app.app, text = list_songs[5], font= label_font, text_color= "black")
def ls6():
    label_image6.place(x = 351, y = 45, anchor = ctk.CENTER)
    label_image1.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image2.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image3.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image4.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image5.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image7.place(x = 1000, y = 45, anchor = ctk.CENTER)
    mixer.music.load(m_path.find_path_to_file(list_songs_name[6]))

label_image7 = ctk.CTkLabel(master = m_app.app, text = list_songs[6], font= label_font, text_color= "black")
def ls7():
    label_image7.place(x = 351, y = 45, anchor = ctk.CENTER)
    label_image1.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image2.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image4.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image5.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image6.place(x = 1000, y = 45, anchor = ctk.CENTER)
    label_image3.place(x = 1000, y = 45, anchor = ctk.CENTER)
    mixer.music.load(m_path.find_path_to_file(list_songs_name[1]))

button1 = create_button(master = m_app.app.FRAME, text = "Despacito | Luis Fonsi", command = ls1)
button1.pack(padx = 15, pady = 5)

button2 = create_button(master = m_app.app.FRAME, text = "NEVEREVER | Destroy Lonely", command = ls2)
button2.pack(padx = 15, pady = 5)

button3 = create_button(master = m_app.app.FRAME, text = "Paranoid | Black Sabbath", command = ls3)
button3.pack(padx = 15, pady = 5)

button4 = create_button(master = m_app.app.FRAME, text = "Город Омск | Смешарики", command = ls4)
button4.pack(padx = 15, pady = 5)

button5 = create_button(master = m_app.app.FRAME, text = "Новое Поколение | Melham", command = ls5)
button5.pack(padx = 15, pady = 5)

button6 = create_button(master = m_app.app.FRAME, text = "The Real Slim Shadyme | Eminem", command = ls6)
button6.pack(padx = 15, pady = 5)

button7 = create_button(master = m_app.app.FRAME, text = "Myself | Yeat", command = ls7)
button7.pack(padx = 15, pady = 5)