from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import database_credential
from student import Student


class Authentication:
    def __init__(self, root):
        self.root = root
        self.width = root.winfo_screenwidth()
        self.height = root.winfo_screenheight()

        # variables
        self.var_username = StringVar()
        self.var_password = StringVar()

        # maximize the tkinter window
        self.root.state('zoomed')
        self.root.title("Database Authentication")

        # authentication frame
        self.auth_frame = LabelFrame(self.root, bd=4, relief=RIDGE,
                                     borderwidth=0, highlightthickness=0, padx=2,
                                     font=("times new roman", 12, "bold"),
                                     fg="red", bg="white")
        self.auth_frame.place(x=0, y=0, width=self.width, height=self.height)

        # heading
        # title label
        lbl_title = Label(self.auth_frame, text="Database Authentication",
                          font=("times new roman", 28, "bold"),
                          fg="blue", bg="white")
        lbl_title.place(x=0, y=50, width=self.width, height=150)

        # input frame
        self.input_frame = LabelFrame(self.auth_frame, bd=4, relief=RIDGE, padx=2,
                                      borderwidth=0, highlightthickness=0,
                                      font=("times new roman", 12, "bold"),
                                      fg="red", bg="white")
        self.input_frame.place(x=0, y=280, anchor="c", relx=.5)

        # username label and entry
        self.lbl_username = Label(self.input_frame, text="Username: ",
                                  font=("arial", 14, "bold"), bg="white")
        self.lbl_username.grid(row=0, column=0, padx=7, pady=14, sticky=W)

        self.username_entry = ttk.Entry(self.input_frame,
                                        textvariable=self.var_username,
                                        font=("arial", 12),
                                        width=24)
        self.username_entry.grid(row=0, column=1, padx=7, pady=14, sticky=W)

        # password label and entry
        self.lbl_password = Label(self.input_frame, text="Password: ",
                                  font=("arial", 14, "bold"), bg="white")
        self.lbl_password.grid(row=1, column=0, padx=7, pady=14, sticky=W)

        self.password_entry = ttk.Entry(self.input_frame, show="*",
                                        textvariable=self.var_password,
                                        font=("arial", 12, "bold"),
                                        width=24)
        self.password_entry.grid(row=1, column=1, padx=7, pady=14, sticky=W)

        # button frame
        self.button_frame = Frame(self.auth_frame, bd=2, relief="ridge",
                                  borderwidth=0, highlightthickness=0, bg="white")
        self.button_frame.place(x=0, y=400, width=180, height=60, anchor="c", relx=.5)

        # auth button
        self.btn_authenticate = Button(self.button_frame, text="Authenticate",
                                       font=("arial", 12, "bold"),
                                       command=self.authenticate_data,
                                       width=16, height=1, bg="blue", fg="white")
        self.btn_authenticate.place(x=0, y=0, width=180, height=60)

    # authenticate data
    def authenticate_data(self):
        if self.var_username.get() == "" or self.var_password.get() == "":
            messagebox.showerror("Error", "All Field are required!")
        elif (self.var_username.get() == database_credential.username and
              self.var_password.get() == database_credential.password):
            Student(self.root)
            self.root.mainloop()
        else:
            messagebox.showerror("Error", "Incorrect Username and Password")
