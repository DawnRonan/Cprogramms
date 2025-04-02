import tkinter as tk
from tkinter import scrolledtext
class app:
    def __init__(self, root):
        self.window = root
        self.window.title("Static Machine Learning")
        w = self.window.winfo_screenwidth()
        h = self.window.winfo_screenheight()
        self.window.geometry(f"{w}x{h}+0+0")

        self.label = tk.Label(self.window, text="Welcome to Static Machine Learning!")
        self.label.pack(fill=tk.X, padx=20, pady=10)
        key_pad_frame = tk.Frame(self.window)
        button_7 = tk.Button(key_pad_frame, text="7", command=self.button_7_click)
        button_7.grid(row=0, column=0)
        button_8 = tk.Button(key_pad_frame, text="8", command=self.button_8_click)
        button_8.grid(row=0, column=1)
        button_9 = tk.Button(key_pad_frame, text="9", command=self.button_9_click)
        button_9.grid(row=0, column=2)
        button_4 = tk.Button(key_pad_frame, text="4", command=self.button_4_click)
        button_4.grid(row=1, column=0)
        button_5 = tk.Button(key_pad_frame, text="5", command=self.button_5_click)
        button_5.grid(row=1, column=1)
        button_6 = tk.Button(key_pad_frame, text="6", command=self.button_6_click)
        button_6.grid(row=1, column=2)
        button_1 = tk.Button(key_pad_frame, text="1", command=self.button_1_click)
        button_1.grid(row=2, column=0)
        button_2 = tk.Button(key_pad_frame, text="2", command=self.button_2_click)
        button_2.grid(row=2, column=1)
        button_3 = tk.Button(key_pad_frame, text="3", command=self.button_3_click)
        button_3.grid(row=2, column=2)
    def button_7_click(self):
        self.entry.insert(tk.END, "7")
    def button_8_click(self):
        self.entry.insert(tk.END, "8")
    def button_9_click(self):
        self.entry.insert(tk.END, "9")
    def button_4_click(self):
        self.entry.insert(tk.END, "4")
    def button_5_click(self):
        self.entry.insert(tk.END, "5")
    def button_6_click(self):
        self.entry.insert(tk.END, "6")
    def button_1_click(self):
        self.entry.insert(tk.END, "1")
    def button_2_click(self):
        self.entry.insert(tk.END, "2")
    def button_3_click(self):
        self.entry.insert(tk.END, "3")
    def log(self, message):
        self.message_area.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, message + "\n")
        self.message_area.config(state=tk.DISABLED)
        self.text_area.see(tk.END)
def main():
    root = tk.Tk()
    root.title("Static Machine Learning")
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    root.geometry(f"{w}x{h}+0+0")

    label = tk.Label(root, text="Welcome to Static Machine Learning!")
    label.pack(pady=20)
    entry = tk.Entry(root, width=50)
    entry.pack(fill=tk.X, padx=20, pady=10)
    button = tk.Button(root, text="Exit", command=root.quit)
    button.pack(pady=10)

    root.mainloop()
if __name__ == "__main__":
    main()