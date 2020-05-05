from tkinter import *
import win32con, win32api
from pynput.mouse import Controller
import time
import _thread

root = Tk()
valor = StringVar()

class Aplicacao(Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        global valor

        txt = Entry(self, width=10, textvariable=valor)
        txt.grid(column=1, row=0)

        txt.focus_set()
    def on_delete(self):
        print("Ok")

    def loop(self):
        manter = True
        time.sleep(1)

        while (manter):
            mouse = Controller()

            global valor
            print(valor.get())

            if(valor.get() != "A"):
                #print('The current pointer position is {0}'.format(
                    #mouse.position))

                win32api.SetCursorPos((800, 300))
            else:
                manter = False

def task(task_name, delay):

    if(task_name == "1"):
        print("passou1")

    if(task_name == "2"):
        print("passou2")
        app.loop()

root.geometry('1000x600')

root.resizable(0, 0)

app = Aplicacao(master=root)
root.protocol("WM_DELETE_WINDOW", app.on_delete)

_thread.start_new_thread(task,("1", 0))
_thread.start_new_thread(task,("2", 0))

app.mainloop()

while 1:
    pass


