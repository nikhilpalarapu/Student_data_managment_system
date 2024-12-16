from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk  # pip install pillow
import mysql.connector  # pip install mysql-connector-python
import database_credential
from PIL import Image

class Student:
    def __init__(self, root):
        self.root = root
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()

        # maximize the tkinter window
        root.state('zoomed')
        self.root.title("STUDENT MANAGEMENT SYSTEM")

        # Variables
        self.var_dept = StringVar()
        self.var_course = StringVar()
        self.var_admission_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_father_name = StringVar()
        self.var_father_mobile = StringVar()
        self.var_blood_group = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_mentor = StringVar()

        # Database Connectivity Variables
        self.host = database_credential.host
        self.username = database_credential.username
        self.password = database_credential.password
        self.database = database_credential.database

        # bg image
        img_4 = Image.open(r"images\university.jpg")
        img_4 = img_4.resize((width, height), Image.Resampling.LANCZOS)
        self.photoImg_4 = ImageTk.PhotoImage(img_4)

        bg_lbl = Label(self.root, image=self.photoImg_4, bd=2, relief=RIDGE)
        bg_lbl.place(x=0, y=0, width=width, height=height)

        # title label
        lbl_title = Label(bg_lbl, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 37, "bold"),
                          fg="blue", bg="white")
        lbl_title.place(x=0, y=0, width=width, height=50)

        # manage frame
        manage_frame = Frame(bg_lbl, bd=2, relief=RIDGE, bg="white")
        manage_frame.place(x=10, y=60, width=width - 20, height=height - 130)

        # left frame
        data_left_frame = LabelFrame(manage_frame, bd=4, relief=RIDGE,
                                     padx=2, text="Student Information",
                                     font=("times new roman", 12, "bold"),
                                     fg="red", bg="white")
        data_left_frame.place(x=10, y=5, width=(width - 50) / 2, height=height - 150)

        # image - inside left frame
        image_width = int((width - 50) / 2)
        left_frame_width = int((width - 50) / 2 - 10)
        img_5 = Image.open(r"images\left_frame.jpg")
        img_5 = img_5.resize((width, height), Image.Resampling.LANCZOS)
        self.photoImg_5 = ImageTk.PhotoImage(img_5)

        left_top_img = Label(data_left_frame, image=self.photoImg_5, bd=2, relief=RIDGE,
                             borderwidth=0, highlightthickness=0)
        left_top_img.place(x=0, y=0, width=left_frame_width, height=220)

        # current course label frame Information
        std_lbl_info_frame = LabelFrame(data_left_frame, bd=4,
                                        padx=2, text="Current Course Information",
                                        font=("times new roman", 12, "bold"),
                                        fg="red", bg="white", borderwidth=3, relief="ridge")
        std_lbl_info_frame.place(x=0, y=220, width=left_frame_width, height=115)

        # Label and Combobox
        # department
        lbl_dept = Label(std_lbl_info_frame, text="Department: ",
                         font=("arial", 11, "bold"), bg="white")
        lbl_dept.grid(row=0, column=0, padx=(10, 2), sticky=W)

        combo_dept = ttk.Combobox(std_lbl_info_frame,
                                  textvariable=self.var_dept,
                                  font=("arial", 10, "bold"),
                                  width=24, state="readonly")
        combo_dept["value"] = ("Select Department",
                               "Mechanical Engineering",
                               "Computer Science",
                               "Information Technology",
                               "Electrical Engineering",
                               "Civil Engineering",
                               "Computer Application")
        combo_dept.current(0)
        combo_dept.grid(row=0, column=1, padx=2, pady=10, sticky=W)

        # course
        course_std = Label(std_lbl_info_frame, text="Course Type: ",
                           font=("arial", 11, "bold"), bg="white")
        course_std.grid(row=0, column=2, padx=(50, 2), pady=10, sticky=W)

        combo_course = ttk.Combobox(std_lbl_info_frame,
                                    textvariable=self.var_course,
                                    font=("arial", 10, "bold"),
                                    width=18, state="readonly")
        combo_course["value"] = ("Select Course Type",
                                 "Under Graduation",
                                 "Post Graduation")
        combo_course.current(0)
        combo_course.grid(row=0, column=3, padx=2, pady=10, sticky=W)

        # admission year
        admission_year = Label(std_lbl_info_frame, text="Admission Year: ",
                               font=("arial", 11, "bold"), bg="white")
        admission_year.grid(row=1, column=0, padx=(10, 2), pady=10, sticky=W)

        combo_admission_year = ttk.Combobox(std_lbl_info_frame,
                                            textvariable=self.var_admission_year,
                                            font=("arial", 10, "bold"),
                                            width=24, state="readonly")
        combo_admission_year["value"] = ("Select Year",
                                         "2018",
                                         "2019",
                                         "2020",
                                         "2021")
        combo_admission_year.current(0)
        combo_admission_year.grid(row=1, column=1, padx=2, sticky=W)

        # semester
        semester_label = Label(std_lbl_info_frame, text="Semester: ",
                               font=("arial", 11, "bold"), bg="white")
        semester_label.grid(row=1, column=2, padx=(50, 2), pady=10, sticky=W)

        combo_semester_label = ttk.Combobox(std_lbl_info_frame,
                                            textvariable=self.var_semester,
                                            font=("arial", 10, "bold"),
                                            width=18, state="readonly")
        combo_semester_label["value"] = ("Select Semester",
                                         "Semester-1",
                                         "Semester-2",
                                         "Semester-3",
                                         "Semester-4",
                                         "Semester-5",
                                         "Semester-6",
                                         "Semester-7",
                                         "Semester-8")
        combo_semester_label.current(0)
        combo_semester_label.grid(row=1, column=3, padx=2, pady=0, sticky=W)

        # student class label frame Information
        std_lbl_class_frame = LabelFrame(data_left_frame, bd=4, relief=RIDGE,
                                         padx=2, text="Student Class Information",
                                         font=("times new roman", 12, "bold"),
                                         fg="red", bg="white")
        std_lbl_class_frame.place(x=0, y=335, width=left_frame_width, height=270)

        # Label and Combobox
        # ID
        lbl_id = Label(std_lbl_class_frame, text="Student ID: ",
                       font=("arial", 11, "bold"), bg="white")
        lbl_id.grid(row=0, column=0, padx=(10, 2), pady=7, sticky=W)

        id_entry = ttk.Entry(std_lbl_class_frame,
                             textvariable=self.var_std_id,
                             font=("arial", 10, "bold"),
                             width=24)
        id_entry.grid(row=0, column=1, padx=2, pady=7, sticky=W)

        # Name
        lbl_name = Label(std_lbl_class_frame, text="Student Name: ",
                         font=("arial", 11, "bold"), bg="white")
        lbl_name.grid(row=0, column=2, padx=(50, 2), pady=7, sticky=W)

        name_entry = ttk.Entry(std_lbl_class_frame,
                               textvariable=self.var_std_name,
                               font=("arial", 10, "bold"),
                               width=24)
        name_entry.grid(row=0, column=3, padx=2, pady=7, sticky=W)

        # Father's Name
        lbl_father_name = Label(std_lbl_class_frame, text="Father Name: ",
                                font=("arial", 11, "bold"), bg="white")
        lbl_father_name.grid(row=1, column=0, padx=(10, 2), pady=7, sticky=W)

        father_name_entry = ttk.Entry(std_lbl_class_frame,
                                      textvariable=self.var_father_name,
                                      font=("arial", 10, "bold"),
                                      width=24)
        father_name_entry.grid(row=1, column=1, padx=2, pady=7, sticky=W)

        # Father Mobile
        lbl_father_mobile = Label(std_lbl_class_frame, text="Father Mobile: ",
                                  font=("arial", 11, "bold"), bg="white")
        lbl_father_mobile.grid(row=1, column=2, padx=(50, 2), pady=7, sticky=W)

        father_mobile_entry = ttk.Entry(std_lbl_class_frame,
                                        textvariable=self.var_father_mobile,
                                        font=("arial", 10, "bold"),
                                        width=24)
        father_mobile_entry.grid(row=1, column=3, padx=2, pady=7, sticky=W)

        # Blood Group
        lbl_bd_grp_class = Label(std_lbl_class_frame, text="Blood Group:",
                                 font=("arial", 11, "bold"), bg="white")
        lbl_bd_grp_class.grid(row=2, column=0, padx=(10, 2), pady=7, sticky=W)

        blood_group_combo = ttk.Combobox(std_lbl_class_frame,
                                         textvariable=self.var_blood_group,
                                         font=("arial", 10, "bold"),
                                         width=20, state="readonly")
        blood_group_combo["value"] = ("Select Blood Group",
                                      "A+",
                                      "O+",
                                      "B+",
                                      "AB+",
                                      "A-",
                                      "O-",
                                      "B-",
                                      "AB-"
                                      )
        blood_group_combo.current(0)
        blood_group_combo.grid(row=2, column=1, padx=2, pady=7, sticky=W)

        # Roll
        lbl_roll = Label(std_lbl_class_frame, text="Roll No.:",
                         font=("arial", 11, "bold"), bg="white")
        lbl_roll.grid(row=2, column=2, padx=(50, 2), pady=7, sticky=W)

        roll_entry = ttk.Entry(std_lbl_class_frame,
                               textvariable=self.var_roll,
                               font=("arial", 10, "bold"),
                               width=24)
        roll_entry.grid(row=2, column=3, padx=2, pady=7, sticky=W)

        # Gender
        lbl_gender = Label(std_lbl_class_frame, text="Gender:",
                           font=("arial", 11, "bold"), bg="white")
        lbl_gender.grid(row=3, column=0, padx=(10, 2), pady=7, sticky=W)

        gender_combo = ttk.Combobox(std_lbl_class_frame,
                                    textvariable=self.var_gender,
                                    font=("arial", 10, "bold"),
                                    width=20, state="readonly")
        gender_combo["value"] = ("Male",
                                 "Female",
                                 "Other")
        gender_combo.current(0)
        gender_combo.grid(row=3, column=1, padx=2, pady=7, sticky=W)

        # Date Of Birth
        lbl_dob = Label(std_lbl_class_frame, text="DOB:",
                        font=("arial", 11, "bold"), bg="white")
        lbl_dob.grid(row=3, column=2, padx=(50, 2), pady=7, sticky=W)

        dob_entry = ttk.Entry(std_lbl_class_frame,
                              textvariable=self.var_dob,
                              font=("arial", 10, "bold"),
                              width=24)
        dob_entry.grid(row=3, column=3, padx=2, pady=7, sticky=W)

        # Email
        lbl_email = Label(std_lbl_class_frame, text="Email:",
                          font=("arial", 11, "bold"), bg="white")
        lbl_email.grid(row=4, column=0, padx=(10, 2), pady=7, sticky=W)

        email_entry = ttk.Entry(std_lbl_class_frame,
                                textvariable=self.var_email,
                                font=("arial", 10, "bold"),
                                width=24)
        email_entry.grid(row=4, column=1, padx=2, pady=7, sticky=W)

        # phone
        lbl_phone = Label(std_lbl_class_frame, text="Mobile:",
                          font=("arial", 11, "bold"), bg="white")
        lbl_phone.grid(row=4, column=2, padx=(50, 2), pady=7, sticky=W)

        phone_entry = ttk.Entry(std_lbl_class_frame,
                                textvariable=self.var_phone,
                                font=("arial", 10, "bold"),
                                width=24)
        phone_entry.grid(row=4, column=3, padx=2, pady=7, sticky=W)

        # Address
        lbl_address = Label(std_lbl_class_frame, text="Address:",
                            font=("arial", 11, "bold"), bg="white")
        lbl_address.grid(row=5, column=0, padx=(10, 2), pady=7, sticky=W)

        address_entry = ttk.Entry(std_lbl_class_frame,
                                  textvariable=self.var_address,
                                  font=("arial", 10, "bold"),
                                  width=24)
        address_entry.grid(row=5, column=1, padx=2, pady=7, sticky=W)

        # Teacher
        lbl_mentor = Label(std_lbl_class_frame, text="Mentor:",
                           font=("arial", 11, "bold"), bg="white")
        lbl_mentor.grid(row=5, column=2, padx=(50, 2), pady=7, sticky=W)

        mentor_entry = ttk.Entry(std_lbl_class_frame,
                                 textvariable=self.var_mentor,
                                 font=("arial", 10, "bold"),
                                 width=24)
        mentor_entry.grid(row=5, column=3, padx=2, pady=7, sticky=W)

        # button frame
        button_frame = Frame(data_left_frame, bd=2, relief="solid", borderwidth=0,
                             highlightthickness=0, bg="white")
        button_frame.place(x=0, y=610, width=left_frame_width, height=75)

        # save button
        btn_add = Button(button_frame, text="SAVE",
                         font=("arial", 12, "bold"),
                         command=self.add_data,
                         width=16, height=2, bg="blue", fg="white")
        btn_add.grid(row=0, column=0, padx=6, pady=10, sticky=W)

        # update button
        btn_update = Button(button_frame, text="UPDATE",
                            font=("arial", 12, "bold"),
                            command=self.update_data,
                            width=16, height=2, bg="blue", fg="white")
        btn_update.grid(row=0, column=1, padx=6, pady=6, sticky=W)

        # delete button
        btn_delete = Button(button_frame, text="DELETE",
                            font=("arial", 12, "bold"),
                            command=self.delete_data,
                            width=16, height=2, bg="blue", fg="white")
        btn_delete.grid(row=0, column=2, padx=6, pady=6, sticky=W)

        # reset button
        btn_reset = Button(button_frame, text="RESET",
                           font=("arial", 12, "bold"),
                           command=self.reset_data,
                           width=16, height=2, bg="blue", fg="white")
        btn_reset.grid(row=0, column=3, padx=6, pady=6, sticky=W)

        # right frame
        data_right_frame = LabelFrame(manage_frame, bd=4, relief=RIDGE,
                                      padx=2, text="Student Information",
                                      font=("times new roman", 11, "bold"),
                                      fg="red", bg="white")
        data_right_frame.place(x=(width - 50) / 2 + 15, y=5, width=(width - 50) - (width - 50) / 2, height=height - 150)

        # image - inside right frame
        right_frame_width = int((width - 50) / 2 - 10)
        img_6 = Image.open(r"images\right_frame.jpg")
        img_6 = img_6.resize((width, height), Image.Resampling.LANCZOS)
        self.photoImg_6 = ImageTk.PhotoImage(img_6)

        right_top_img = Label(data_right_frame, image=self.photoImg_6, bd=2, borderwidth=0,
                              highlightthickness=0, relief=RIDGE)
        right_top_img.place(x=0, y=0, width=image_width - 10, height=220)

        # search frame
        search_frame = LabelFrame(data_right_frame, bd=4, relief=RIDGE,
                                  padx=2, text="Search Student Information",
                                  font=("times new roman", 11, "bold"),
                                  fg="red", bg="white")
        search_frame.place(x=0, y=220, width=right_frame_width, height=60)

        # search by label
        search_by = Label(search_frame, text="Search By:",
                          font=("arial", 11, "bold"), fg="black")
        search_by.grid(row=0, column=0, padx=5, sticky=W)

        # search
        self.var_combo_search = StringVar()
        search_combo = ttk.Combobox(search_frame,
                                    textvariable=self.var_combo_search,
                                    font=("arial", 10, "bold"),
                                    width=18, state="readonly")
        search_combo["value"] = ("Select Option",
                                 "Roll_No",
                                 "Phone",
                                 "Student_id")
        search_combo.current(0)
        search_combo.grid(row=0, column=1, padx=5, sticky=W)

        self.var_search = StringVar()
        search_entry = ttk.Entry(search_frame,
                                 textvariable=self.var_search,
                                 font=("arial", 10, "bold"),
                                 width=28)
        search_entry.grid(row=0, column=2, padx=2, sticky=W)

        # search button
        btn_search = Button(search_frame, text="Search",
                            font=("arial", 11, "bold"),
                            command=self.search_data,
                            width=12, bg="blue", fg="white")
        btn_search.grid(row=0, column=3, padx=8, sticky=W)

        # show all button
        btn_show_all = Button(search_frame, text="Show All",
                              font=("arial", 11, "bold"),
                              command=self.fetch_data,
                              width=12, bg="blue", fg="white")
        btn_show_all.grid(row=0, column=4, padx=5, sticky=W)

        # Student Table & scroll bar
        table_frame = Frame(data_right_frame, bd=4, relief="ridge")
        table_frame.place(x=0, y=280, width=right_frame_width, height=410)

        scroll_bar_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_bar_y = ttk.Scrollbar(table_frame, orient=VERTICAL)
        self.student_table = ttk.Treeview(table_frame, column=("dept",
                                                               "course",
                                                               "admit_year",
                                                               "sem",
                                                               "id",
                                                               "name",
                                                               "father_name",
                                                               "father_mobi",
                                                               "bd_grp",
                                                               "roll",
                                                               "gender",
                                                               "dob",
                                                               "email",
                                                               "phone",
                                                               "address",
                                                               "mentor"),
                                          xscrollcommand=scroll_bar_x.set,
                                          yscrollcommand=scroll_bar_y.set)
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

        scroll_bar_x.config(command=self.student_table.xview)
        scroll_bar_y.config(command=self.student_table.yview)

        self.student_table.heading("dept", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("admit_year", text="Admission Year")
        self.student_table.heading("sem", text="Semester")
        self.student_table.heading("id", text="Student ID")
        self.student_table.heading("name", text="Student Name")
        self.student_table.heading("father_name", text="Father Name")
        self.student_table.heading("father_mobi", text="Father Mobile")
        self.student_table.heading("bd_grp", text="Blood Group")
        self.student_table.heading("roll", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone No")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("mentor", text="Mentor")

        self.student_table["show"] = "headings"

        self.student_table.column("dept", width=150)
        self.student_table.column("course", width=100)
        self.student_table.column("admit_year", width=100)
        self.student_table.column("sem", width=100)
        self.student_table.column("id", width=100)
        self.student_table.column("name", width=150)
        self.student_table.column("father_name", width=150)
        self.student_table.column("father_mobi", width=100)
        self.student_table.column("bd_grp", width=100)
        self.student_table.column("roll", width=100)
        self.student_table.column("gender", width=100)
        self.student_table.column("dob", width=100)
        self.student_table.column("email", width=150)
        self.student_table.column("phone", width=100)
        self.student_table.column("address", width=150)
        self.student_table.column("mentor", width=100)

        self.student_table.pack(fill=BOTH, expand=1)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if (self.var_dept.get() == "" or
                self.var_dept.get() == "Select Department" or
                self.var_course.get() == "" or
                self.var_course.get() == "Select Course Type" or
                self.var_admission_year.get() == "" or
                self.var_admission_year.get() == "Select Year" or
                self.var_semester.get() == "" or
                self.var_semester.get() == "Select Semester" or
                self.var_std_id.get() == "" or
                self.var_std_name.get() == "" or
                self.var_father_name.get() == "" or
                self.var_father_mobile.get() == "" or
                self.var_blood_group.get() == "" or
                self.var_blood_group.get() == "Select Blood Group" or
                self.var_roll.get() == "" or
                self.var_gender.get() == "" or
                self.var_dob.get() == "" or
                self.var_email.get() == "" or
                self.var_phone.get() == "" or
                self.var_address.get() == "" or
                self.var_mentor.get() == ""):
            messagebox.showerror("Error", "All Field are required!")
        else:
            try:
                connection = mysql.connector.connect(host=self.host,
                                                     username=self.username,
                                                     password=self.password,
                                                     database=self.database)
                cursor = connection.cursor()
                cursor.execute(
                    "insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                    (self.var_dept.get(),
                     self.var_course.get(),
                     self.var_admission_year.get(),
                     self.var_semester.get(),
                     self.var_std_id.get(),
                     self.var_std_name.get(),
                     self.var_father_name.get(),
                     self.var_father_mobile.get(),
                     self.var_blood_group.get(),
                     self.var_roll.get(),
                     self.var_gender.get(),
                     self.var_dob.get(),
                     self.var_email.get(),
                     self.var_phone.get(),
                     self.var_address.get(),
                     self.var_mentor.get()
                     ))
                connection.commit()
                self.fetch_data()
                connection.close()
                messagebox.showinfo("Success", "Student has been Added!", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # fetch function
    def fetch_data(self):
        connection = mysql.connector.connect(host=self.host,
                                             username=self.username,
                                             password=self.password,
                                             database=self.database)
        cursor = connection.cursor()
        cursor.execute("select * from student")
        data = cursor.fetchall()
        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values=i)
            connection.commit()
        connection.close()

    # Get Cursor
    def get_cursor(self, event=""):
        cursor_row = self.student_table.focus()
        content = self.student_table.item(cursor_row)
        data = content["values"]

        self.var_dept.set(data[0])
        self.var_course.set(data[1])
        self.var_admission_year.set(data[2])
        self.var_semester.set(data[3])
        self.var_std_id.set(data[4])
        self.var_std_name.set(data[5])
        self.var_father_name.set(data[6])
        self.var_father_mobile.set(data[7])
        self.var_blood_group.set(data[8])
        self.var_roll.set(data[9])
        self.var_gender.set(data[10])
        self.var_dob.set(data[11])
        self.var_email.set(data[12])
        self.var_phone.set(data[13])
        self.var_address.set(data[14])
        self.var_mentor.set(data[15])

    # update data
    def update_data(self):
        if (self.var_dept.get() == "" or
                self.var_dept.get() == "Select Department" or
                self.var_course.get() == "" or
                self.var_course.get() == "Select Course Type" or
                self.var_admission_year.get() == "" or
                self.var_admission_year.get() == "Select Year" or
                self.var_semester.get() == "" or
                self.var_semester.get() == "Select Semester" or
                self.var_std_id.get() == "" or
                self.var_std_name.get() == "" or
                self.var_father_name.get() == "" or
                self.var_father_mobile.get() == "" or
                self.var_blood_group.get() == "" or
                self.var_blood_group.get() == "Select Blood Group" or
                self.var_roll.get() == "" or
                self.var_gender.get() == "" or
                self.var_dob.get() == "" or
                self.var_email.get() == "" or
                self.var_phone.get() == "" or
                self.var_address.get() == "" or
                self.var_mentor.get() == ""):
            messagebox.showerror("Error", "All Field are required!")
        else:
            try:
                update = messagebox.askyesno("Update", "Are you sure update this student data",
                                             parent=self.root)
                if update > 0:
                    connection = mysql.connector.connect(host=self.host,
                                                         username=self.username,
                                                         password=self.password,
                                                         database=self.database)
                    cursor = connection.cursor()
                    cursor.execute(
                        "update student set dept=%s,course=%s,admit_year=%s,semester=%s,name=%s,father_name=%s,"
                        "father_mobi=%s,bd_grp=%s,roll_no=%s,gender=%s,dob=%s,email=%s,phone=%s,address=%s,"
                        "mentor=%s where student_id=%s",
                        (self.var_dept.get(),
                         self.var_course.get(),
                         self.var_admission_year.get(),
                         self.var_semester.get(),
                         self.var_std_name.get(),
                         self.var_father_name.get(),
                         self.var_father_mobile.get(),
                         self.var_blood_group.get(),
                         self.var_roll.get(),
                         self.var_gender.get(),
                         self.var_dob.get(),
                         self.var_email.get(),
                         self.var_phone.get(),
                         self.var_address.get(),
                         self.var_mentor.get(),
                         self.var_std_id.get()
                         ))
                else:
                    if not update:
                        return
                connection.commit()
                self.fetch_data()
                connection.close()

                messagebox.showinfo("Success", "Student successfully updated", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # delete data
    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error", "All Field are required! Select from left table.")
        else:
            try:
                delete = messagebox.askyesno("Delete", "Are you sure delete this student data",
                                             parent=self.root)
                if delete > 0:
                    connection = mysql.connector.connect(host=self.host,
                                                         username=self.username,
                                                         password=self.password,
                                                         database=self.database)
                    cursor = connection.cursor()
                    sql_query = "delete from student where student_id=%s"
                    value = (self.var_std_id.get(),)
                    cursor.execute(sql_query, value)
                else:
                    if not delete:
                        return
                connection.commit()
                self.fetch_data()
                connection.close()

                messagebox.showinfo("Delete", "Student successfully deleted", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)

    # reset
    def reset_data(self):
        self.var_dept.set("Select Department")
        self.var_course.set("Select Course")
        self.var_admission_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_father_name.set("")
        self.var_father_mobile.set("")
        self.var_blood_group.set("Select Blood Group")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_mentor.set("")

    # search data
    def search_data(self):
        if self.var_combo_search.get() == "" or self.var_search.get() == "":
            messagebox.showerror("Error", "Please select option")
        else:
            try:
                connection = mysql.connector.connect(host=self.host,
                                                     username=self.username,
                                                     password=self.password,
                                                     database=self.database)
                cursor = connection.cursor()
                cursor.execute("Select * from student where " + str(self.var_combo_search.get()) +
                               " LIKE '%" + str(self.var_search.get()) + "%'")
                data = cursor.fetchall()
                if len(data) != 0:
                    self.student_table.delete(*self.student_table.get_children())
                    for i in data:
                        self.student_table.insert("", END, values=i)
                    connection.commit()
                else:
                    messagebox.showerror("Search Result", "No Such Student Found")
                connection.close()
            except Exception as es:
                messagebox.showerror("Error", f"Due To:{str(es)}", parent=self.root)
