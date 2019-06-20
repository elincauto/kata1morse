import morse
from tkinter import *
from tkinter import ttk

class Translator(ttk.Frame):
    def __init__(self,parent,**kwargs):
        ttk.Frame.__init__(self, parent,height=kwargs["height"],width=kwargs["width"])

        self.sender=StringVar()
        self.receiver=StringVar()

        sender_lbl = ttk.Label(self, text="Sender:", width=11, anchor=W)
        sender_lbl.place(x=12,y=12)
        self.sender_entry = ttk.Entry(self, width=16, textvariable=self.sender)
        self.sender_entry.place(x=70,y=10)

        receiver_lbl = ttk.Label(self, text="Sender:", width=11, anchor=W)
        receiver_lbl.place(x=250,y=12)
        self.receiver_entry = ttk.Entry(self, width=16, textvariable=self.receiver)
        self.receiver_entry.place(x=318,y=10)

        origin_lbl=ttk.Label(self,text="Plano",width=6,anchor=W)
        origin_lbl.place(x=12,y=40)
        origin_text= Text(width=26,height=8)
        origin_text.place(x=32,y=80)

        destino_lbl=ttk.Label(self,text="Morse",width=6,anchor=W)
        destino_lbl.place(x=250,y=40)
        destino_text= Text(width=26,height=8)
        destino_text.place(x=270,y=80)

        btn_send = ttk.Button(self,command=self.send_telegram,text="Send")
        btn_send.place(y=165,x=500)

        btn_change = ttk.Button(self, command=self.changeText,text="<=>" )
        btn_change.place

    def send_telegram(self):
        print("Enviar Telegrama")
    
    def changeText(self):
        if self.traduccionDirecta:
            self.origin_lbl.config("texto=Morse")
        




class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Traductor Morse")
        self.geometry("600x200")

        self.translator= Translator(self,height=200,width=600)
        self.translator.place(x=0,y=0)

    def start(self):
        self.mainloop()

if __name__=="__main__":
    miTraductor= MainApp()
    miTraductor.translator.place(x=10,y=10)
    miTraductor.start()


