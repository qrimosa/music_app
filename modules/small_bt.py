import customtkinter as ctk
import modules.creating_screen as m_app
# import modules.text_input as m_text


def create_button(master, text = "", width = 61, height = 58, border_width = 4, corner_radius = 15, border_color = "#1E1E1E"):
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

bt_skip = create_button(master= m_app.app)
bt_skip.place(x = 288, y = 165, anchor = ctk.CENTER)

bt_return = create_button(master = m_app.app)   
bt_return.place(x = 396, y = 165, anchor = ctk.CENTER) 

bt_sound_decrease = create_button(master = m_app.app)
bt_sound_decrease.place(x = 396, y = 396, anchor = ctk.CENTER) 

bt_sound_increase = create_button(master = m_app.app)
bt_sound_increase.place(x = 303, y = 396, anchor = ctk.CENTER)

bt_delete = create_button(master = m_app.app)
bt_delete.place(x = 131, y = 396, anchor = ctk.CENTER)

bt_add = create_button(master = m_app.app)
bt_add.place(x = 45, y = 396, anchor = ctk.CENTER)

bt_mix = create_button(master = m_app.app)
bt_mix.place(x = 217 , y = 396 , anchor = ctk.CENTER)