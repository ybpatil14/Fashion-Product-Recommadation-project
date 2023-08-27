from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Management System")


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

        title_lbl=Label(bg_img,text="Student Management System",font=("times new roman",35,"bold"),bg="white",fg="darkblue")
        title_lbl.place(x=0,y=0,width=1550,height=45)


        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=50,width=1480,height=600)

        # Left Label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=730,height=580)

        img_left=Image.open(r"C:\Users\HP-8440P\Desktop\Face Recognation system\Image\students-7630653_1280.jpg")
        img_left=img_left.resize((720,130),Image.LANCZOS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        bg_img=Label(Left_frame,image=self.photoimg_left)
        bg_img.place(x=5,y=0,width=720,height=130)

        # Current Course Information
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=715,height=125)

        # Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

         # Course
        course_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year
        year_label=Label(current_course_frame,text="Course",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_label_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=20)
        year_label_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_label_combo.current(0)
        year_label_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        # Semister
        semister_label=Label(current_course_frame,text="Semister",font=("times new roman",12,"bold"),bg="white")
        semister_label.grid(row=1,column=2,padx=10,sticky=W)

        semister_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="readonly",width=20)
        semister_combo["values"]=("Select Semister","Sem-1","Sem-2")
        semister_combo.current(0)
        semister_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


         # Class Student Information
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="Class Students Information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)

        # StudentID
        studentID_label=Label(class_student_frame,text="StudentID",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # Student Name
        studentname_label=Label(class_student_frame,text="Student Name",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # Class Division
        class_div_label=Label(class_student_frame,text="Class Division",font=("times new roman",12,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)
        
        # Roll NUmber
        roll_no_label=Label(class_student_frame,text="Roll Number",font=("times new roman",12,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # Gender
        gender_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # Date of Birth
        DOB_label=Label(class_student_frame,text="DOB",font=("times new roman",12,"bold"),bg="white")
        DOB_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        DOB_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        DOB_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

         # Email
        email_label=Label(class_student_frame,text="Email",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

         # Phone no.
        phone_label=Label(class_student_frame,text="Phone no.",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

         # Address
        add_label=Label(class_student_frame,text="Address",font=("times new roman",12,"bold"),bg="white")
        add_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        add_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        add_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

         # Teacher Name
        teacher_label=Label(class_student_frame,text="Teacher Name",font=("times new roman",12,"bold"),bg="white")
        teacher_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teacher_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        teacher_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        # Radio Buttons
        radiobtn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",value="Yes")
        radiobtn1.grid(row=5,column=0)

        radiobtn2=ttk.Radiobutton(class_student_frame,text="No Photo Sample",value="Yes")
        radiobtn2.grid(row=5,column=1)

        #Buttons Frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=70)

        save_btn=Button(btn_frame,text="Save",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)


        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)

        take_photo_btn=Button(btn_frame,text="Take Photo Sample",width=15,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=1,column=0)

        # Right Label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Students Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=750,y=10,width=720,height=580)


if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()