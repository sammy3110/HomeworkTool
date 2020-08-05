from tkinter import *
from tkinter import font
from tkinter import filedialog
from PIL import Image
from Homework import Homework

class HomeworkGUI:      

    global image_location, folder_location
    image_location = ""
    folder_location = ""

    def __init__(self):

        self.root = Tk()
        self.root.title("Homework")
        self.root['bg'] = "#4f4f4f"
        self.createGUI()
        self.root.mainloop()

    def doHome(self, img, loc):
        self.lbl_Ilocation['text'] = ""
        self.lbl_Flocation['text'] = ""
        self.frame_Display.destroy()
        instance = Homework()
        instance.doHomework(img, loc)

    def browseFile(self):
        global image_location
        
        image_location = filedialog.askopenfilename()
        self.lbl_Ilocation['text'] = image_location
        list_image_location = image_location.split('/')
        image_location = "\\\\".join(list_image_location)

    def browseFolder(self):
        global folder_location
        myFont = font.Font(family="Bembo", size=13)

        folder_location = filedialog.askdirectory()
        self.lbl_Flocation['text'] = folder_location
        folder_location = folder_location.split('/')
        folder_location = "\\".join(folder_location)
        
        new = Image.open(image_location)
        self.frame_Display = Frame(self.root, bg="#4f4f4f")
        self.frame_Display.grid(row=1, column=0, columnspan=2)
        self.btn_doHomework = Button(self.frame_Display, text="Do Homework",font=myFont, padx='5', pady='5', bg="black", fg="white", command= lambda: self.doHome(new, folder_location))
        self.btn_doHomework.grid(row=0, column=0, pady=10)
        

    def createGUI(self):

        global image_location, folder_location

        #............................... FONT ...................................
        myFont = font.Font(family="Bembo", size=13)

        #............................... FRAME ..................................
        frame_Image = Frame(self.root, bg="#4f4f4f")
        frame_Image.grid(row=0, column=0)
        frame_Folder = Frame(self.root, bg="#4f4f4f")
        frame_Folder.grid(row=0, column=1)

        #............................... WIDGETS ................................
        lbl_selectImage = Label(frame_Image, text="Please select Image to do homework.", font=myFont, padx='10', pady='10', bg="#4f4f4f")
        lbl_selectImage.grid(row=0, column=0)
        btn_browseImage = Button(frame_Image, text="Browse", font=myFont, padx='5', pady='5', command=self.browseFile, bg="black", fg="white")
        btn_browseImage.grid(row=1, column=0)  
        self.lbl_Ilocation = Label(frame_Image, text="", font=myFont, padx='10', pady='10', bg="#4f4f4f", fg="white")
        self.lbl_Ilocation.grid(row=2, column=0)

        lbl_selectFolder = Label(frame_Folder, text="Please select location to save image.", font=myFont, padx='10', pady='10', bg="#4f4f4f")

        lbl_selectFolder.grid(row=0, column=0)
        btn_browseFolder = Button(frame_Folder, text="Select Folder", font=myFont, padx='5', pady='5', command=self.browseFolder, bg="black", fg="white")
        btn_browseFolder.grid(row=1, column=0)
        self.lbl_Flocation = Label(frame_Folder, text="", font=myFont, padx='10', pady='10', bg="#4f4f4f", fg="white")
        self.lbl_Flocation.grid(row=2, column=0)

instance = HomeworkGUI()