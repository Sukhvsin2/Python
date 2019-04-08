from tkinter import *
from tkinter import filedialog
from tkinter.font import Font

class text_editor:
    current_file = 'Untitled - '

    def newfile(self):
        self.text.delete(1.0,END)
        self.current_file = ('Untitled - Text Editor')
        self.master.title(self.current_file)
        
    def openfile(self,event=''):
        f = filedialog.askopenfile(initialdir='/',title='Select File',filetypes=(('text','.txt'),('all type','*.*')))
        if f != None:
            self.text.delete(1.0,END)
            self.master.title(f.name)
            for i in f:
                self.text.insert(END,i)
            self.current_file = f.name
            f.close()
            
    def saveas(self):
        f = filedialog.asksaveasfile(mode="w",defaultextension=".txt")
        if f is None:
            return
        else:
            saved = self.text.get(1.0,END)
            f.write(saved)
            self.current_file = f.name
            self.master.title(self.current_file)
            f.close()

    def savefile(self):
        if self.current_file == 'Untitled - ':
            self.saveas()
        else:
            f = open(self.current_file,mode='w+')
            f.write(self.text.get(1.0,END))
            self.master.title(self.current_file)
            f.close()

    def fontselection(self):
        fontwin = Toplevel()
        fontwin.title('Select Font')

        l = Listbox(fontwin,selectmode=SINGLE)
        l.insert(1,'Helvetica, Arial, sans-serif')
        l.insert(2,'monospace')
        l.insert(3,'"Times New Roman", serif')
        l.pack(side=LEFT)
        
        #myfont = Font(family=l.get())
        print(l.get())
        fontwin.geometry('200x200')
        fontwin.mainloop()
        
    
    def copyfile(self):
        self.text.clipboard_clear()
        self.text.clipboard_append(self.text.selection_get())

    def cutfile(self):
        self.copyfile()
        self.text.delete('sel.first','sel.last')

    def pastefile(self):
        text = self.text.insert(INSERT,self.text.clipboard_get())
            
    
    def __init__(self,master):
        self.master = master
        master.title(self.current_file+"Text Editor")
        self.text = Text(self.master,wrap=WORD,padx=10,pady=10,undo=True)
        self.text.pack(fill = BOTH,expand=1)
        self.mainmenu = Menu()
        self.master.config(menu=self.mainmenu)
    


        #Creating ShortCuts
        master.bind('Control+o',self.openfile)

        
        #Creating file menu
        self.filemenu = Menu(self.mainmenu,tearoff=False)
        self.mainmenu.add_cascade(label="File",menu=self.filemenu)
        self.filemenu.add_command(label="New",command=self.newfile)
        self.filemenu.add_command(label="Open",command=self.openfile)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Save',command=self.savefile)
        self.filemenu.add_command(label='Save as',command=self.saveas)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Exit',command=master.destroy)
        
        #Creating edit menu
        self.editmenu = Menu(self.mainmenu,tearoff=False)
        self.editmenu.add_command(label='Undo',command=self.text.edit_undo)
        self.editmenu.add_command(label='Redo',command=self.text.edit_redo)
        self.editmenu.add_separator()
        self.mainmenu.add_cascade(label="Edit",menu=self.editmenu)
        self.editmenu.add_command(label = 'Copy',command=self.copyfile)
        self.editmenu.add_command(label = 'Cut',command=self.cutfile)
        self.editmenu.add_command(label = 'Paste',command=self.pastefile)
        
        
        #creating format menu
        self.formatmenu = Menu(self.mainmenu,tearoff=False)
        self.mainmenu.add_cascade(label="Format",menu=self.formatmenu)
        self.formatmenu.add_command(label='Font',command=self.fontselection)
        #Creating View menu
        self.viewmenu = Menu(self.mainmenu,tearoff=False)
        self.mainmenu.add_cascade(label="View",menu=self.viewmenu)
        #Creating Help menu
        self.helpmenu = Menu(self.mainmenu,tearoff=False)
        self.mainmenu.add_cascade(label="Help",menu=self.helpmenu)

        
        
root = Tk()


te = text_editor(root)

root.mainloop()
