# from tkinter import Tk, Listbox, Button, Scrollbar

# def get():
#     userline=leftside.get('active')
#     print(userline) 

# def scale():
#     global leftside
#     thescale=Tk()
#     scroll=Scrollbar(thescale)
#     scroll.pack(side='right', fill='y')

#     leftside = Listbox(thescale, yscrollcommand = scroll.set)
#     for line in range(101):
#         leftside.insert('end', "Scale "+str(line))

#     leftside.pack(side='left', fill='both')
#     scroll.config(command=leftside.yview)

#     selectbutton=Button(thescale, text="Select", command=get)
#     selectbutton.pack()

#     thescale.mainloop()

# scale()


import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import Tk, Listbox, Button, Scrollbar

LARGE_FONT= ("Verdana", 12)

class interface(tk.Tk):
	def __init__(self) :
		tk.Tk.__init__(self)

		container=tk.Frame(self)
		container.pack(side="bottom", fill="none", expand = True,padx=200,pady=150)

		menubar = tk.Menu(container)

		tk.Tk.config(self, menu=menubar)

		self.frames={}

		for F in (StartPage, BTCe_Page,PageOne):

			frame = F(container, self)

			self.frames[F] = frame

			frame.grid(row=0, column=0, sticky="nsew")


		self.show_frame(StartPage)

	def show_frame(self, cont):

		frame = self.frames[cont]
		frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text=("""Bun venit!
        Sa incepem cumparaturile!"""), font=LARGE_FONT)
        label.pack(pady=10,padx=10)

        button1 = ttk.Button(self, text="De acord",
                            command=lambda: controller.show_frame(PageOne))
        button1.pack(padx=10,pady=10)

        button2 = ttk.Button(self, text="Nu sunt de acord",
                            command=quit)
        button2.pack(padx=10,pady=10)



class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        global leftside
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page One!!!", font=LARGE_FONT)
        label.pack(pady=10,padx=10)
        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(BTCe_Page))
        button1.pack()
        scroll_bar=Scrollbar(self)
        scroll_bar.pack(side=LEFT,fill=Y)
   
        
        ###

        leftside = Listbox(self, yscrollcommand = scroll_bar.set)
        for line in range(1, 26):
            leftside.insert(END, "Geeks " + str(line))
        
        leftside.pack(side='left', fill='both')
        scroll_bar.config(command=leftside.yview)

        selectbutton=Button(self, text="Select", command=self.get(controller))
        selectbutton.pack(anchor='w')
    
    def get(self,controller):
        userline=leftside.get('active')
        print(userline)
        if userline=="Geeks 1":
            controller.show_frame(BTCe_Page)
            



class BTCe_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Graph Page!", font=LARGE_FONT)
        label.pack()

        button1 = ttk.Button(self, text="Back to Home",
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

app=interface()

app.mainloop()
