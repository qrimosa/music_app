import customtkinter as ctk
import modules.creating_screen as m_app



def create_button(master, text = "", width =169 , height = 60, border_width = 4, corner_radius = 15, border_color = "#1E1E1E"):
    button = ctk.CTkButton(
        master = master,
        width = width,
        height = height,
        border_width = border_width,
        corner_radius = corner_radius,
        border_color = border_color,
        text = text, 
    )
    return button

bt_play = create_button(master = m_app.app)
bt_play.place(x = 341, y = 85, anchor = ctk.CENTER)

bt_pause = create_button(master = m_app.app)
bt_pause.place(x = 341, y = 243, anchor = ctk.CENTER)

bt_stop = create_button(master = m_app.app)
bt_stop.place(x = 341, y = 323, anchor = ctk.CENTER)