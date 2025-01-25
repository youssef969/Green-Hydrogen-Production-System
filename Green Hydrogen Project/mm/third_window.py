import tkinter as tk

class ThirdWindow:
    def __init__(self, main_window):
        self.main_window = main_window
        
        self.third_window = tk.Toplevel()
        self.third_window.title("Third Window")
        
        self.image = tk.PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\1710162623466-removebg-preview.png")  # Load third window image
        
        self.label = tk.Label(self.third_window, image=self.image)
        self.label.pack()
        
        self.button = tk.Button(self.third_window, text="Switch back to Main Window", command=self.switch_to_main_window)
        self.button.pack()

    def switch_to_main_window(self):
        self.third_window.destroy()  # Close the third window
        self.main_window.root.deiconify()  # Show the main window again