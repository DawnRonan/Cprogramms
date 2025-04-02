import tkinter as tk
from tkinter import scrolledtext

class App:
    def __init__(self, root):
        self.window = root
        self.window.title("Static Machine Learning Calculator")
        w = 300
        h = 550
        self.window.geometry(f"{w}x{h}+0+0")

        self.label = tk.Label(self.window, text="Welcome to Static Machine Learning Calculator!")
        self.label.pack(fill=tk.X, expand=True)

        self.message_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, state=tk.DISABLED, height=10)
        self.message_area.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.current_input = ""  # 用于保存当前输入的表达式

        key_pad_frame = tk.Frame(self.window)

        # 创建按钮并放置
        buttons = [
            ("7", 0, 0), ("8", 0, 1), ("9", 0, 2), ("+", 0, 3),
            ("4", 1, 0), ("5", 1, 1), ("6", 1, 2), ("-", 1, 3),
            ("1", 2, 0), ("2", 2, 1), ("3", 2, 2), ("*", 2, 3),
            ("C", 3, 0), ("0", 3, 1), ("=", 3, 2), ("/", 3, 3)
        ]

        for (text, row, col) in buttons:
            button = tk.Button(key_pad_frame, text=text, command=lambda t=text: self.button_click(t))
            button.grid(row=row, column=col, padx=5, pady=5)

        key_pad_frame.pack()

    def button_click(self, char):
        """ 处理按钮点击事件 """
        if char == "=":
            try:
                # 计算当前输入的表达式
                result = eval(self.current_input)
                self.log(f"= {result}")
                self.current_input = str(result)  # 将计算结果保存为当前输入
            except Exception as e:
                self.log(f"Error: {e}")
                self.current_input = ""
        elif char == "C":
            # 清除输入
            self.current_input = ""
            self.log("Cleared")
        else:
            # 将字符添加到当前输入
            self.current_input += char
            self.log(self.current_input)

    def log(self, message):
        """ 在消息区域显示输入内容 """
        self.message_area.config(state=tk.NORMAL)
        self.message_area.delete(1.0, tk.END)  # 清空已有内容
        self.message_area.insert(tk.END, message + "\n")
        self.message_area.config(state=tk.DISABLED)
        self.message_area.see(tk.END)

def main():
    root = tk.Tk()
    app = App(root)  # 创建 GUI 应用
    root.mainloop()

if __name__ == "__main__":
    main()
