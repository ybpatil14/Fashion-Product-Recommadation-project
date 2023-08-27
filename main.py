from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Face_Recognition_system:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")

        # First image
        img=Image.open(r"C:\Users\HP-8440P\Desktop\Face Recognation system\Image\university-6699377_1280.jpg")
        img=img.resize((500,130),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=15,y=0,width=500,height=130)

        # Second image
        img1=Image.open(r"C:\Users\HP-8440P\Desktop\Face Recognation system\Image\students-7630653_1280.jpg")
        img1=img1.resize((500,130),Image.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=515,y=0,width=500,height=130)

        #Third image
        img2=Image.open(r"C:\Users\HP-8440P\Desktop\Face Recognation system\Image\yale-university-1604156_1280.jpg")
        img2=img2.resize((500,130),Image.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1015,y=0,width=500,height=130)

        # Background Image
        img3=Image.open(r"C:\Users\HP-8440P\Desktop\Face Recognation system\Image\tiles-shapes-2617112_1280.jpg")
        img3=img3.resize((1550,710),Image.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1550,height=710)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDENCE SYSTEM SOFTWEAR",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        # Student Button
        img4=Image.open(r"C:\Users\HP-8440P\Desktop\Face Recognation system\Image\pencils-6099511_1280.jpg")
        img4=img4.resize((220,220),Image.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(bg_img,text="Student Details",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)


        # Face Detection Button
        img5=Image.open(r"C:\Users\HP-8440P\Desktop\Face Recognation system\Image\face-detection-4760281_1280.jpg")
        img5=img5.resize((220,220),Image.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b2.place(x=500,y=100,width=220,height=220)

        b2_1=Button(bg_img,text="Face Detection",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=500,y=300,width=220,height=40)


        
        # Attendance Button
        img6=Image.open(r"C:\Users\HP-8440P\Desktop\Face Recognation system\Image\students-250164_1280.jpg")
        img6=img6.resize((220,220),Image.LANCZOS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b3.place(x=800,y=100,width=220,height=220)

        b3_1=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=800,y=300,width=220,height=40)


        
        # Help Desk Button
        img7=Image.open(r"C:\Users\HP-8440P\Desktop\Face Recognation system\Image\help-153094_1280.png")
        img7=img7.resize((220,220),Image.LANCZOS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b4.place(x=1100,y=100,width=220,height=220)

        b4_1=Button(bg_img,text="Helf Desk",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1100,y=300,width=220,height=40)


         # Train Data Button
        img8=Image.open(r"C:\Users\HP-8440P\Desktop\Face Recognation system\Image\to-learn-3325490_1280.jpg")
        img8=img8.resize((220,220),Image.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b5.place(x=200,y=380,width=220,height=220)

        b5_1=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=200,y=580,width=220,height=40)


        # Photos Button
        img9=Image.open(r"C:\Users\HP-8440P\Desktop\Face Recognation system\Image\camera-1130731_1280.jpg")
        img9=img9.resize((220,220),Image.LANCZOS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b6.place(x=500,y=380,width=220,height=220)

        b6_1=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_1.place(x=500,y=580,width=220,height=40)


        
        # Developer Button
        img10=Image.open(r"C:\Users\HP-8440P\Desktop\Face Recognation system\Image\man-1839500_1280.jpg")
        img10=img10.resize((220,220),Image.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b7=Button(bg_img,image=self.photoimg10,cursor="hand2")
        b7.place(x=800,y=380,width=220,height=220)

        b7_1=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_1.place(x=800,y=580,width=220,height=40)


        
        # Exit Button
        img11=Image.open(r"C:\Users\HP-8440P\Desktop\Face Recognation system\Image\sign-575715_1280.png")
        img11=img11.resize((220,220),Image.LANCZOS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b8=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b8.place(x=1100,y=380,width=220,height=220)

        b8_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_1.place(x=1100,y=580,width=220,height=40)



if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_system(root)
    root.mainloop()