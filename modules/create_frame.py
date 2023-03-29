import customtkinter as ctk 
import modules.creating_screen as m_app

class My_Frame(ctk.CTkFrame):
    def __init__(self, text, master, width, height, border_width, fg_color, **kwargs):
        super().__init__(master = master,width = width, height = height, border_width = border_width, fg_color= fg_color, **kwargs)