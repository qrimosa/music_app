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
        self.title("Music Play")
        # self._fg_color = ("white")
        self.FRAME = m_frame.My_Frame(text = "Назва треків що додано", master = self, width = 233 , height = 315 , border_width = 5, corner_radius = 15)
        self.FRAME.place(x = 130, y = 195, anchor = ctk.CENTER)

app = App(454, 469)  