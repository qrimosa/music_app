import customtkinter as ctk
import modules.create_frame as m_frame

class App(ctk.CTk):
    def __init__(self,app_width,app_height):
        super().__init__()
        self.APP_WIDTH = app_width
        self.APP_HEIGHT = app_height
        self.SCREEN_WIDTH = self.winfo_screenwidth()
        self.SCREEN_HEIGHT = self.winfo_screenheight()
        self.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}+{0}+{0}")
        self.resizable(False, False)
        self.title("Ждём зарплату день 5")
        self._fg_color = ("#4CB7CE")
        self.config(bg = "#4CB7CE")
        self.FRAME = m_frame.My_Frame(text = "", master = self, width = 233 , height = 345 , border_width = 4, corner_radius = 15, fg_color = "#bdbdbd")
        self.FRAME.place(x = 130, y = 185, anchor = ctk.CENTER)
        
app = App(454, 469)  