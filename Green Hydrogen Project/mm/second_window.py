import tkinter as tk
from third_window import ThirdWindow

class SecondWindow:
    def __init__(self, main_window):
        self.main_window = main_window
        
        self.second_window = tk.Toplevel()
        self.second_window.title("Second Window")
        
        self.image = tk.PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\1710162623466-removebg-preview.png")  # Load second window image
        
        self.label = tk.Label(self.second_window, image=self.image)
        self.label.pack()
        
        self.button = tk.Button(self.second_window, text="Switch to Third Window", command=self.switch_to_third_window)
        self.button.pack()

    def switch_to_third_window(self):
        self.second_window.withdraw()  # Hide the second window
        self.third_window = ThirdWindow(self.main_window)  # Create an instance of the ThirdWindow