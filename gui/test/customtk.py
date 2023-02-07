import customtkinter

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry(f"{600}x{500}")
        self.title("CTk example")


app = App()
app.mainloop()