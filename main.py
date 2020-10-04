import tkinter
import os
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import time

class Notepad:

    #variables
    __root = Tk()

    #default window width and height
    __thisWidth = 1000
    __thisHeight = 1000
    __thisTextArea = Text(__root)
    __thisMenuBar = Menu(__root)
    __thisFileMenu = Menu(__thisMenuBar,tearoff=0)
    __thisEditMenu = Menu(__thisMenuBar,tearoff=0)
    __thisHelpMenu = Menu(__thisMenuBar,tearoff=0)
    __thisScrollBar = Scrollbar(__thisTextArea)
    __file = None

    def __init__(self,**kwargs):
        #initialization

        #set icon
        try:
        		self.__root.wm_iconbitmap("Notepad.ico") #GOT TO FIX THIS ERROR (ICON)
        except:
        		pass

        #set window size (the default is 300x300)

        try:
            self.__thisWidth = kwargs['width']
        except KeyError:
            pass

        try:
            self.__thisHeight = kwargs['height']
        except KeyError:
            pass

        #set the window text
        self.__root.title("Untitled - FireEditor")

        #center the window
        screenWidth = self.__root.winfo_screenwidth()
        screenHeight = self.__root.winfo_screenheight()

        left = (screenWidth / 2) - (self.__thisWidth / 2)
        top = (screenHeight / 2) - (self.__thisHeight /2)

        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, self.__thisHeight, left, top))

        #to make the textarea auto resizable
        self.__root.grid_rowconfigure(0,weight=1)
        self.__root.grid_columnconfigure(0,weight=1)

        #add controls (widget)

        self.__thisTextArea.grid(sticky=N+E+S+W)

        self.__thisFileMenu.add_command(label="Nouveau",command=self.__newFile)
        self.__thisFileMenu.add_command(label="Ouvrir",command=self.__openFile)
        self.__thisFileMenu.add_command(label="Enregistrer",command=self.__saveFile)
        self.__thisFileMenu.add_separator()
        self.__thisFileMenu.add_command(label="Fermer",command=self.__quitApplication)
        self.__thisMenuBar.add_cascade(label="Fichier",menu=self.__thisFileMenu)

        self.__thisEditMenu.add_command(label="Couper",command=self.__cut)
        self.__thisEditMenu.add_command(label="Copier",command=self.__copy)
        self.__thisEditMenu.add_command(label="Coller",command=self.__paste)
        self.__thisMenuBar.add_cascade(label="Edition",menu=self.__thisEditMenu)

        self.__thisHelpMenu.add_command(label="Concernant FireEditor",command=self.__showAbout)
        self.__thisMenuBar.add_cascade(label="Aide",menu=self.__thisHelpMenu)

        self.__root.config(menu=self.__thisMenuBar)

        self.__thisScrollBar.pack(side=RIGHT,fill=Y)
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set)
    
        
    def __quitApplication(self):
        if self.__root.title() == "Untitled - FireEditor":
            showinfo("ATTENTION !", "Vous n'avez pas enregistré le fichier")
            showinfo("ATTENTION !", "En fermant cette page, vous allez perdre votre document !")
        self.__root.destroy()
        #exit()

    def __showAbout(self):
        showinfo("FireEditor","Créé par Fireblock !")

    def __openFile(self):
        
        self.__file = askopenfilename(defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

        if self.__file == "":
            #no file to open
            self.__file = None
        else:
            #try to open the file
            #set the window title
            self.__root.title(os.path.basename(self.__file) + " - FireEditor")
            self.__thisTextArea.delete(1.0,END)

            file = open(self.__file,"r")

            self.__thisTextArea.insert(1.0,file.read())

            file.close()

        
    def __newFile(self):
        self.__root.title("Untitled - FireEditor")
        self.__file = None
        self.__thisTextArea.delete(1.0,END)
        showinfo("Des bisous !","Bonne utilisation du logiciel")

    def __saveFile(self):

        if self.__file == None:
            #save as new file
            self.__file = asksaveasfilename(initialfile='Untitled.txt',defaultextension=".txt",filetypes=[("All Files","*.*"),("Text Documents","*.txt")])

            if self.__file == "":
                self.__file = None
            else:
                #try to save the file
                file = open(self.__file,"w")
                file.write(self.__thisTextArea.get(1.0,END))
                file.close()
                #change the window title
                self.__root.title(os.path.basename(self.__file) + " - Notepad")
                
            
        else:
            file = open(self.__file,"w")
            file.write(self.__thisTextArea.get(1.0,END))
            file.close()

    def __cut(self):
        self.__thisTextArea.event_generate("<<Cut>>")

    def __copy(self):
        self.__thisTextArea.event_generate("<<Copy>>")

    def __paste(self):
        self.__thisTextArea.event_generate("<<Paste>>")

    def run(self):

        #run main application
        self.__root.mainloop()




#run main application
notepad = Notepad(width=800,height=600)
notepad.run()
