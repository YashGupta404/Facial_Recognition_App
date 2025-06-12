from tkinter import* 
from tkinter import ttk 
from PIL import Image, ImageTk 

class User:

    def __init__(self, root): 
        self.root = root 
        self.root.title("Face Recognition System") 
        self.root.geometry("1530x790+0+0") 
        
         #background image
        bg_img = Image.open(r"C:\images_face_recog\background.jpg") 
        bg_img = bg_img.resize((1530, 790), Image.LANCZOS)
        self.photobg_img = ImageTk.PhotoImage(bg_img) 
        self.lbl_bg = Label(self.root, image= self.photobg_img)
        self.lbl_bg.place(x=0, y=0, width=1530, height=790)
        
         #logo image
        image = Image.open(r"C:\images_face_recog\face-recognition.png")
        image = image.resize((100, 100), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(image) 
        self.lbl_image = Label(self.root, image= self.photoimage)
        self.lbl_image.place(x=1420, y=10, width=100, height=100)
        
        
if __name__ == "__main__":
    root = Tk()
    app = User(root)
    root.mainloop()        
       