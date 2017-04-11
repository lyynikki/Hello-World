import tkinter
import tkinter.font as tkfont

class Window(object):
    def __init__(self):
        self.tk = tkinter.Tk()
        self.sysfont = tkfont.Font(self.tk ,size = 28)

        self.tk.title("我的gui")

        self.label1 = tkinter.Label(master=tk, text="请输入你的名字")
        self.label1.pack()

        self.entry = tkinter.Entry(master=tk)
        self.entry.pack()

        self.button = tkinter.Button(master=tk, text='提交')
        self.button.pack()
        self.tk.mainloop()

win = Window()