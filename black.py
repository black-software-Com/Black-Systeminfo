#!/usr/bin/python3
# Black-Systeminfo v1.0
import os,platform,socket,webbrowser,re,uuid
from tkinter.filedialog import asksaveasfile
try:
    from tkinter import *
    from tkinter.ttk import Label
    from tkinter import filedialog
except ImportError:
    os.system("pip install tk-tools")

class black_systeminfo(Tk):
    def __init__(self):
        super(black_systeminfo,self).__init__()
        self.title('Black Systeminfo')
        menu = Menu(self,tearoff=0)
        self.maxsize(500,400)
        self.minsize(400,200)
        aboutfile = Menu(menu,tearoff=0)
        aboutfile.add_command(label='Save',accelerator='Ctrl+S',command=self.save_file)
        aboutfile.add_command(label='Black',command=self.black)
        aboutfile.add_command(label='Help',command=self.help)
        aboutfile.add_command(label='Dev',command=self.dev)
        aboutfile.add_command(label='Donate',command=self.donate)
        aboutfile.add_separator()
        aboutfile.add_command(label='Exit',accelerator='Ctrl+F4',command=self.ext)
        menu.add_cascade(label='About',menu=aboutfile)
        self.photo = PhotoImage(file = './Scr/black.png')
        self.config(menu=menu)
        self.host = socket.gethostname()
        self.ip = socket.gethostbyname(self.host)
        self.system = platform.system()
        self.release = platform.release()
        self.version = platform.version()

        self.machine = platform.machine()
        self.mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        self.processor = platform.processor()
        self.txt = f'''
System: {self.system}
Release: {self.release}
Version: {self.version}
Host: {self.host}
Ip: {self.ip}
Machone: {self.machine}
Mac Address: {self.mac_address}
Processor: {self.processor}

        '''
        label_systeminfo = Label(self,text=self.txt,font=("None",10))
        label_systeminfo.pack()
        self.bind("<Control-s>",lambda x: self.save_file_2(x))
        self.iconphoto(False,self.photo)
        self.geometry("400x300")
        self.mainloop()
    def dev(self):
        webbrowser.open_new_tab('https://github.com/mrprogrammer2938')
    def black(self):
        webbrowser.open_new_tab('https://black-software.ir')
    def help(self):
        webbrowser.open_new_tab('https://black-software-com.github.io/Black-Help/')
    def donate(self):
        webbrowser.open_new_tab('https://idpay.ir/mrprogrammer2938')
    def ext(self):
        self.destroy()
        self.quit()
        quit()
    def save_file(self):
        try:
            file = asksaveasfile(title='Save As',mode="w")
            file.write(str(self.txt))
            file.close()
        except AttributeError:
            print(False)
    def save_file_2(self,x):
        try:
            file = asksaveasfile(title='Save As',mode="w")
            file.write(str(self.txt))
            file.close()
        except AttributeError:
            print(False)
if __name__ == '__main__':
    window = black_systeminfo()