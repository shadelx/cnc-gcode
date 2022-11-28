import serial as ser
import tkinter as tk
from time import sleep
import os
from tkinter import filedialog

class app():

    def serial_arduino(self):
        #function for the conection with arduino
        try:
            port= "COM10"
            baudrate = 115200
            arduino = ser.Serial(port, baudrate)

            self.print_txt("arduino conection successfully")
        except:
            self.print_txt("Arduino conection not working\nplease check connection...")
        sleep(2)
        msg = arduino.readline()
        self.print_txt(str(msg.decode('utf -8')))
        
    def print_txt(self, text):
        #function for printing on textbox
        self.txtbox1.insert(tk.END,text+"\n")

    def upload(self):
        file_format=(("pdf file","*.pdf"),("all files","*.*"),("text file","*.txt"))
        self.file_text=filedialog.askopenfilename(filetypes=file_format)
        self.print_txt("you upload the next file:")
        self.print_txt(self.file_text)

    def print_cnc(self):
        try:
            gcode_file = open(self.file_text, "r")
        except:
            self.print_txt("Error: can't find file or read data")
        self.print_txt("G- code file output:")
        for line in gcode_file:
            print(line)
        text = gcode_file.readline()
        self.print_txt(text)

    def __init__(self, window):
        #window.geometry("300x250")

        self.var = tk.StringVar()
        self.var.set("INK PROGRAM")
        #define frame
        self.frame1 = tk.Frame(window)
        self.frame1.grid(row=0, column=0, sticky="news")
        #define widgets label, texbox, scroll, btn
        self.lbl1=tk.Label(self.frame1, textvariable=self.var)
        self.lbl1.grid(row=0, column=0, columnspan=3, sticky="news")
        
        self.sbar = tk.Scrollbar(self.frame1)
        self.sbar.grid(row=1, column=1)
        self.txtbox1=tk.Text(self.frame1, yscrollcommand= self.sbar.set,height= 5,width=50)
        self.txtbox1.grid(row=1, column=0)
        self.sbar.config(command = self.txtbox1.yview)
        self.print_txt("****Welcome to ink program****\nplease upload your program...")

        self.btn1 = tk.Button(self.frame1, text="upload", command = self.upload)
        self.btn1.grid(row=1, column=2, sticky= "news")
        self.btn2 = tk.Button(self.frame1, text="print", command = self.print_cnc)
        self.btn2.grid(row=2, column=0, columnspan=3, sticky="news")

        #self.serial_arduino()

if __name__ == "__main__":
    window= tk.Tk()
    app(window)
    window.mainloop()
