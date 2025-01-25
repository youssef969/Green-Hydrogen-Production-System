import tkinter as tk
from second_window import SecondWindow

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Window")
        
        self.image = tk.PhotoImage(file="C:\\Users\\Computec\\Downloads\\PNG Icons\\1710162623466-removebg-preview.png")  # Load main window image
        
        self.label = tk.Label(self.root, image=self.image)
        self.label.pack()
        
        self.button = tk.Button(self.root, text="Switch to Second Window", command=self.switch_to_second_window)
        self.button.pack()

    def switch_to_second_window(self):
        self.root.withdraw()  # Hide the main window
        self.second_window = SecondWindow(self)  # Create an instance of the SecondWindow
        
root = tk.Tk()
ob = MainWindow(root)
root.mainloop()