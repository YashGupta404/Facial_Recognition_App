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
        image = Image.open(r"C:\images_face_recog\background.jpg")
        image = image.resize((100, 100), Image.LANCZOS)
        self.photoimage = ImageTk.PhotoImage(image) 
        self.lbl_image = Label(self.root, image= self.photoimage)
        self.lbl_image.place(x=1420, y=10, width=100, height=100)

        #frame
        main_frame=Frame(self.lbl_bg, bd=2, bg="white")
        main_frame.place(x=20, y = 55, width=1480,height=600)
        
        #left label frame
        Left_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Left_frame.place(x=10, y = 10, width=730, height=580)
        img_left=Image.open(r"C:\images_face_recog\background.jpg")
        img_left=img_left.resize((720,130), Image.LANCZOS)
        self.photoimg_left=ImageTk. PhotoImage(img_left)
        f_lbl=Label(Left_frame,image=self.photoimg_left)
        f_lbl.place( x = 5 ,y=0,width=720, height=130)
        
        #current course
        curr_frame=LabelFrame(Left_frame, bd=2,bg="white", relief=RIDGE, text="Current Course Details", font=("times new roman", 12, "bold"))
        curr_frame.place( x = 5, y = 135, width=720, height=200)

        #dept
        dep_label=Label (curr_frame, text="Department", font=("times new roman", 12, "bold"), bg="white")
        dep_label.grid(row=0,column=0, padx=10, sticky=W)
        dep_combo=ttk.Combobox(curr_frame, font=("times new roman", 12, "bold"), state="readonly", width=20)
        dep_combo["values"]=("Select Department", "Computer", "IT", "Civil", "Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1, padx=2, pady=10, sticky=W)
        
        #course
        course_label=Label (curr_frame, text="Course", font=("times new roman", 12, "bold"), bg="white")
        course_label.grid(row=0,column=2, padx=10, sticky=W)
        course_combo=ttk.Combobox(curr_frame, font=("times new roman", 12, "bold"), state="readonly", width=20)
        course_combo["values"]=("Select Course", "FE", "SE", "TE", "BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3, padx=2, pady=10, sticky=W)

        #year
        yr_label=Label (curr_frame, text="Year", font=("times new roman", 12, "bold"), bg="white")
        yr_label.grid(row=1,column=0, padx=10, sticky=W)
        yr_combo=ttk.Combobox(curr_frame, font=("times new roman", 12, "bold"), state="readonly", width=20)
        yr_combo["values"]=("Select Year", "1", "2", "3", "4")
        yr_combo.current(0)
        yr_combo.grid(row=1,column=1, padx=2, pady=10, sticky=W)

        #Sem
        sem_label=Label (curr_frame, text="Semester", font=("times new roman", 12, "bold"), bg="white")
        sem_label.grid(row=1,column=2, padx=10, sticky=W)
        sem_combo=ttk.Combobox(curr_frame, font=("times new roman", 12, "bold"), state="readonly", width=20)
        sem_combo["values"]=("Select Semester", "1", "2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3, padx=2, pady=10, sticky=W)

        #class student info
        cls_frame=LabelFrame(Left_frame, bd=2,bg="white", relief=RIDGE, text="Class Student Information", font=("times new roman", 12, "bold"))
        cls_frame.place( x = 5, y = 250, width=720, height=300)

        #id
        studentId_label=Label(cls_frame, text="Student ID:", font=("times new roman", 13, "bold"), bg="white")
        studentId_label.grid(row=0, column=0, padx=10, sticky=W)
        studentID_entry=ttk.Entry (cls_frame, width=20, font=("times new roman", 13, "bold"))
        studentID_entry.grid(row=0,column=1, padx=10, pady=5, sticky=W)
        
        #name
        studentname_label=Label(cls_frame, text="Student Name:", font=("times new roman", 13, "bold"), bg="white")
        studentname_label.grid(row=0, column=2, padx=10, sticky=W)
        studentname_entry=ttk.Entry (cls_frame, width=20, font=("times new roman", 13, "bold"))
        studentname_entry.grid(row=0,column=3, padx=10, pady=5, sticky=W)
        
        #class
        studentclass_label=Label(cls_frame, text="Student Class:", font=("times new roman", 13, "bold"), bg="white")
        studentclass_label.grid(row=1, column=0, padx=10, sticky=W)
        studentclass_entry=ttk.Entry (cls_frame, width=20, font=("times new roman", 13, "bold"))
        studentclass_entry.grid(row=1,column=1, padx=10, pady=5, sticky=W)
        
        #roll
        studentroll_label=Label(cls_frame, text="Student Roll no:", font=("times new roman", 13, "bold"), bg="white")
        studentroll_label.grid(row=1, column=2, padx=10, sticky=W)
        studentroll_entry=ttk.Entry (cls_frame, width=20, font=("times new roman", 13, "bold"))
        studentroll_entry.grid(row=1,column=3, padx=10, pady=5, sticky=W)
        
        #gender
        studentgender_label=Label(cls_frame, text="Student Gender:", font=("times new roman", 13, "bold"), bg="white")
        studentgender_label.grid(row=2, column=0, padx=10, sticky=W)
        studentgender_entry=ttk.Entry (cls_frame, width=20, font=("times new roman", 13, "bold"))
        studentgender_entry.grid(row=2,column=1, padx=10, pady=5, sticky=W)
        
        #dob
        studentdob_label=Label(cls_frame, text="Student DOB:", font=("times new roman", 13, "bold"), bg="white")
        studentdob_label.grid(row=2, column=2, padx=10, sticky=W)
        studentdob_entry=ttk.Entry (cls_frame, width=20, font=("times new roman", 13, "bold"))
        studentdob_entry.grid(row=2,column=3, padx=10, pady=5, sticky=W)
        
        #email
        studentmail_label=Label(cls_frame, text="Student Email:", font=("times new roman", 13, "bold"), bg="white")
        studentmail_label.grid(row=3, column=0, padx=10, sticky=W)
        studentmail_entry=ttk.Entry (cls_frame, width=20, font=("times new roman", 13, "bold"))
        studentmail_entry.grid(row=3,column=1, padx=10, pady=5, sticky=W)
        
        #phone
        studentph_label=Label(cls_frame, text="Student Phone No:", font=("times new roman", 13, "bold"), bg="white")
        studentph_label.grid(row=3, column=2, padx=10, sticky=W)
        studentph_entry=ttk.Entry (cls_frame, width=20, font=("times new roman", 13, "bold"))
        studentph_entry.grid(row=3,column=3, padx=10, pady=5, sticky=W)
        
        #address
        studentadd_label=Label(cls_frame, text="Student Address:", font=("times new roman", 13, "bold"), bg="white")
        studentadd_label.grid(row=4, column=0, padx=10, sticky=W)
        studentadd_entry=ttk.Entry (cls_frame, width=20, font=("times new roman", 13, "bold"))
        studentadd_entry.grid(row=4,column=1, padx=10, pady=5, sticky=W)
        
        #Teacher name
        teacher_label=Label(cls_frame, text="Teacher Name:", font=("times new roman", 13, "bold"), bg="white")
        teacher_label.grid(row=4, column=2, padx=10, sticky=W)
        teacher_entry=ttk.Entry (cls_frame, width=20, font=("times new roman", 13, "bold"))
        teacher_entry.grid(row=4,column=3, padx=10, pady=5, sticky=W)

        # radio Buttons
        radionbtn1=ttk.Radiobutton(cls_frame, text="Take Photo Sample", value="Yes")
        radionbtn1.grid(row=6,column=0)
        radionbtn2=ttk.Radiobutton(cls_frame, text="No Photo Sample", value="Yes")
        radionbtn2.grid(row=6,column=1)
        
        #bbuttons frame
        btn_frame=Frame(cls_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(btn_frame, text="Save", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0,column=0)

        upd_btn=Button(btn_frame, text="Update", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        upd_btn.grid(row=0,column=1)

        del_btn=Button(btn_frame, text="Delete", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        del_btn.grid(row=0,column=2)

        res_btn=Button(btn_frame, text="Reset", width=17, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        res_btn.grid(row=0,column=3)

        btn_frame1=Frame(cls_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame1.place(x=0,y=235,width=715,height=35)

        take_photo_btn=Button(btn_frame1, text="Take Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1, text="Update Photo Sample", width=35, font=("times new roman", 13, "bold"), bg="blue", fg="white")
        update_photo_btn.grid(row=0,column=1)

        #right label frame
        Right_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Details", font=("times new roman", 12, "bold"))
        Right_frame.place(x=750, y = 10, width=720, height=580)
        img_right=Image.open(r"C:\images_face_recog\background.jpg")
        img_right=img_right.resize((720,130), Image.LANCZOS)
        self.photoimg_right=ImageTk. PhotoImage(img_right)
        f_lbl=Label(Left_frame,image=self.photoimg_right)
        f_lbl.place( x = 5 ,y=0,width=720, height=130)

        #search system
        search_frame=LabelFrame(Right_frame, bd=2,bg="white", relief=RIDGE, text="Search System", font=("times new roman", 12, "bold"))
        search_frame.place( x = 5, y = 150, width=710, height=70)

        search_label=Label(search_frame, text="Search By:", font=("times new roman", 13, "bold"), bg="red", fg="white")
        search_label.grid(row=0, column=0, padx=10, sticky=W)

        search_combo=ttk.Combobox (search_frame, font=("times new roman", 13, "bold"), state="readonly", width=20)
        search_combo ["values"]=("Select", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row=0,column=1, padx=2, pady=10, sticky=W)
        
        search_entry=ttk.Entry (search_frame, width=15, font=("times new roman", 13, "bold"))
        search_entry.grid(row=0,column=2, padx=10, pady=5, sticky=W)
        
        search_btn=Button(search_frame, text="Search", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        search_btn.grid(row=0,column=3, padx=4)
        
        showAll_btn=Button(search_frame, text="Show All", width=12, font=("times new roman", 12, "bold"), bg="blue", fg="white")
        showAll_btn.grid(row=0, column=4, padx=4)

        #table frame
        table_frame=Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        table_frame.place(x=5,y=210, width=710, height=350)
        scroll_x=ttk.Scrollbar (table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar (table_frame, orient=VERTICAL)
        self.student_table=ttk.Treeview(table_frame, column=("dep", "course", "year", "sem", "id", "name", "div", "roll", "gender", "dob", "email", "gender", "phone", "address", "teacher", "photo"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="StudentId")
        self.student_table.heading("name", text="Name")
        self.student_table.heading("div", text="Division")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("teacher", text="Teacher")
        self.student_table.heading("photo", text="PhotoSampleStatus")
        self.student_table["show"]="headings"
        
        self.student_table.column("dep", width=100)
        self.student_table.column("course", width=100)
        self.student_table.column("year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("div", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=100)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=100)
        self.student_table.column("teacher", width=100)
        self.student_table.column("photo", width=150)
        
        self.student_table.pack(fill=BOTH, expand=1)

        
if __name__ == "__main__":
    root = Tk()
    app = User(root)
    root.mainloop()        
       