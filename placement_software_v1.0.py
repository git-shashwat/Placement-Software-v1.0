import tkinter as tk
from tkinter import font as tkfont
from tkinter import filedialog
from tkinter import messagebox as tkmsg
from tkinter import ttk
import pandas as pd
import re
from PIL import Image, ImageTk
import PS_data_parser as dp
import refined_DB_generator as rdb
import email_module as edm


# Certain changes have to be made to ensure proper event functioning
# Work on branch_input function to add dynamics to it


companyName = ''
tenth_input_choice = 0
twelth_input_choice = 0
btech_input_choice = 0
backlog_entry_choice = 999      # Sentinel Value
gapyear_entry_choice = 999      # Sentinel Value
gender_input = ''
branchChoices = []
parsedFileName = ''
fromValue = ''
toList = ''
emailSubject = ''
emailBody = ''

def branch_input(s):
    global branchChoices
    if s in branchChoices:
        branchChoices.remove(s)
    else:
        branchChoices.append(s)
    
def gender_choice(s):
    global gender_input  
    gender_input = s  

class mainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.title(self,'Placement Software')
        tk.Tk.geometry(self, "1800x980+100+100")

        # *****Theme Fonts*****
        self.heading_font = tkfont.Font(family = 'Roboto', size = 25)
        self.main_font = tkfont.Font(family = 'Arial', size = 14)

        # **** Theme Colors *****
        self.success = "#28a745"
        self.successFocus = "#60C151"
        self.info = "#17a2b8"
        self.infoFocus = "#52C2C2"
        self.grayDark = "#343a40"
        self.light = "#f8f9fa"
        self.primary = "#007bff"
        self.primaryFocus = "#3A99FC"


        # **** Creating Container(for holding multiple pages) ****
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # **** Adding Pages as frames ****
        self.frame_list = {}

        # **** Iterating through different pages ****
        self.frame_list["homePage"] = homePage(parent = container, controller = self)
        self.frame_list["companyProfile"] = companyProfile(parent = container, controller = self)
        self.frame_list["refinedDatabase"] = refinedDatabase(parent = container, controller = self)
        self.frame_list["emailWindow"] = emailWindow(parent = container, controller = self)

        # **** Grid Setup of different pages *****
        self.frame_list["homePage"].grid(row=0, column=0, sticky="nsew")
        self.frame_list["companyProfile"].grid(row=0, column=0, sticky="nsew")
        self.frame_list["refinedDatabase"].grid(row=0, column=0, sticky="nsew")
        self.frame_list["emailWindow"].grid(row = 0, column = 0, sticky= "nsew")

        self.show_frame("homePage")

    def show_frame(self,page_name):
       frame = self.frame_list[page_name]
       frame.tkraise()

    def quitApp(self):
        self.quit()

class homePage(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent, bg=controller.grayDark)
        self.controller = controller

        # Row Configuration
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=2)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        # Column Configuration
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # Login Email
        loginEmail = tk.Label(self, text="Login Email: ", bg=controller.grayDark, fg=controller.light, font=controller.main_font)
        loginEmail.grid(row=1, column = 2)

        loginInput = tk.Entry(self, width=50, fg="#E08237")
        loginInput.grid(row=1, column=3, sticky="w")
        loginInput.bind("<Return>", self.loginWindow)

        message = tk.Label(self, text="UPLOAD WINDOW", font= "Roboto 40", bg=controller.grayDark, fg= controller.light)
        message.grid(row=2, column=2)
        
        importInstruction = tk.Label(self, text="Select file to import:   ", font = controller.main_font, bg=controller.grayDark, fg="#B22C7A")
        importInstruction.grid(row=3, column=1)
        
        importBtn = tk.Button(self, text="Upload File", padx=3, pady=5, relief = "raised", command =self.browseFunc, bg="#000000", fg=controller.light, height=3, activebackground="#f4f4f4")
        importBtn.grid(row=3, column=2, sticky="w")

        companyProfileBtn = tk.Button(self, text="Add Company Profile", command=lambda: controller.show_frame("companyProfile"), bg=controller.success, height=2, font=controller.main_font, activebackground=controller.successFocus)
        companyProfileBtn.grid(row=4, column=1)

        previewBtn = tk.Button(self, text="Preview Record", command= lambda: controller.show_frame("refinedDatabase"), bg=controller.success, height=2, font=controller.main_font, activebackground=controller.successFocus)
        previewBtn.grid(row=4, column=2)


        emailBtn = tk.Button(self, text="Send Email", command= lambda: controller.show_frame("emailWindow"), bg=controller.success, height=2, font=controller.main_font, activebackground=controller.successFocus)
        emailBtn.grid(row=4, column=3)      

    def browseFunc(self):
        pathlabel = tk.Label(self)
        filename = str(filedialog.askopenfilename(filetypes=(("Excel files","*.xlsm"),("CSV files","*.csv"),("Text files","*.txt"))) )

        if(filename != ''):
            answer = tkmsg.askyesno("Upload", "Do you want to upload"+filename+"?")
            if (answer):
                global parsedFileName
                pathlabel.config(text = filename)  
                pathlabel.grid(row=3, column=3)
                result = dp.dataParser(filename)
                result.to_excel('testing_new.xlsm', index = False)
        
        else:
            tkmsg.showwarning("Upload Error", "No file Selected!")

    def loginWindow(self,e):
        global fromValue
        fromValue = e.widget.get()
class companyProfile(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent, bg=controller.grayDark)
        self.controller = controller
        
        # Row Configuration
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)
        self.rowconfigure(5, weight=1)
        self.rowconfigure(6, weight=1)
        self.rowconfigure(7, weight=1)
        self.rowconfigure(8, weight=1)
        self.rowconfigure(9, weight=1)
        self.rowconfigure(10, weight=1)
        self.rowconfigure(11, weight=1)
        self.rowconfigure(12, weight=1)
        self.rowconfigure(13, weight=1)
        self.rowconfigure(14, weight=1)

        # Column configuration
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
     # Creating form fields for company profile

        companyProfileForm = tk.Label(self, text = "Fill the following particulars: ", font = controller.heading_font, bg=controller.grayDark, fg="#30AAAA")
        companyProfileForm.grid(row = 1, column = 2) 

        # ***** Company Name *****
        companyName = tk.Label(self, text = "Company Name:", font = controller.main_font, bg=controller.grayDark, fg=controller.light)
        companyName_entry = tk.Entry(self)
        companyName_entry.bind("<FocusOut>",self.on_change)

        companyName.grid(row = 2, column = 1, sticky="e")
        companyName_entry.grid(row = 2, column =2, sticky="e")

        # *****Branch Section*****

        branch = tk.Label(self, text = "Branch:", font = controller.main_font, bg=controller.grayDark, fg=controller.light)
        cse = tk.BooleanVar()
        ece = tk.BooleanVar()
        eee = tk.BooleanVar()
        it  = tk.BooleanVar()
        All = tk.BooleanVar()

        C1 = tk.Checkbutton(self, text="CSE", variable= cse, height = 2, width = 100, anchor="e", command=lambda: branch_input("cse"), bg=controller.grayDark, fg=controller.light, selectcolor="black")
        C2 = tk.Checkbutton(self, text="ECE", variable= ece, height = 2, width = 100, anchor="e", command=lambda: branch_input("ece"), bg=controller.grayDark, fg=controller.light, selectcolor="black")
        C3 = tk.Checkbutton(self, text="EEE", variable= eee, height = 2, width = 100, anchor="e", command=lambda: branch_input("eee"), bg=controller.grayDark, fg=controller.light, selectcolor="black")
        C4 = tk.Checkbutton(self, text="IT", variable= it, height = 2, width = 100, anchor="e", command=lambda: branch_input("it"), bg=controller.grayDark, fg=controller.light, selectcolor="black")
        C5 = tk.Checkbutton(self, text="All", variable= All, height = 2, width = 100, anchor="e", command=lambda: branch_input("all"), bg=controller.grayDark, fg=controller.light, selectcolor="black")

        # C1.bind("<Button-1>",self.branchChoices)

        branch.grid(row = 3, column = 1, sticky="e")
        C1.grid(row = 3, column = 2, sticky="e")
        C2.grid(row = 4, column = 2, sticky="e")
        C3.grid(row = 5, column = 2, sticky="e")
        C4.grid(row = 6, column = 2, sticky="e")
        C5.grid(row = 7, column = 2, sticky="e")

        # ***** 10th Marks % ******
        tenth = tk.Label(self, text = "10th %:", font = controller.main_font, bg=controller.grayDark, fg=controller.light)
        tenth_input = tk.Entry(self)
        tenth_input.bind("<FocusOut>", self.tenth_input_choice)

        tenth.grid(row = 8, column = 1, sticky="e")
        tenth_input.grid(row = 8, column = 2, sticky="e")

        # ***** 12th Marks % *****
        twelth = tk.Label(self, text = "12th %:", font = controller.main_font, bg=controller.grayDark, fg=controller.light)
        twelth_input = tk.Entry(self)
        twelth_input.bind("<FocusOut>",self.twelth_input_choice)

        twelth.grid(row = 9, column = 1, sticky="e")
        twelth_input.grid(row = 9, column =2, sticky="e")

        # ***** B.Tech Marks % *****
        btech = tk.Label(self, text = "B.Tech %:", font = controller.main_font, bg=controller.grayDark, fg=controller.light)
        btech_input = tk.Entry(self)
        btech_input.bind("<FocusOut>",self.btech_input_choice)

        btech.grid(row = 10, column = 1, sticky="e")
        btech_input.grid(row = 10, column =2, sticky="e")

        # ***** Backlogs Accepted *****
        backlog = tk.Label(self, text = "Backlogs Accepted:", font = controller.main_font, bg=controller.grayDark, fg=controller.light)
        backlog_entry = tk.Entry(self)
        backlog_entry.bind("<FocusOut>",self.backlog_entry_choice)

        backlog.grid(row = 11, column = 1, sticky="e")
        backlog_entry.grid(row = 11, column =2, sticky="e")

        # ***** Max Gap Year Accepted *****
        gapYear = tk.Label(self, text = "Maximum Gap Year Accepted:", font = controller.main_font, bg=controller.grayDark, fg=controller.light)
        gapYear_entry = tk.Entry(self)
        gapYear_entry.bind("<FocusOut>", self.gapyear_entry_choice)

        gapYear.grid(row = 12, column = 1, sticky="e")
        gapYear_entry.grid(row = 12, column =2, sticky="e")         

        # *****Girl Candidate Only*****
        genderValue = tk.IntVar()

        femaleOnly = tk.Label(self, text = "Female Students Only:", font = controller.main_font, bg=controller.grayDark, fg=controller.light)
        Op1 = tk.Radiobutton(self, text="Yes", variable=genderValue, value = 1, command=lambda: gender_choice("yes"), bg=controller.grayDark, fg=controller.light, selectcolor="black")
        Op2 = tk.Radiobutton(self, text="No", variable = genderValue, value = 2, command=lambda: gender_choice("no"), bg=controller.grayDark, fg=controller.light, selectcolor="black")

        femaleOnly.grid(row = 13, column = 1, pady = 10, sticky="e")
        Op1.grid(row = 13, column = 2, pady = 10, sticky="e")
        Op2.grid(row = 14, column = 2, pady=10, sticky="e")

        # ***** Previous Btn Navigation *****
        prevBtn = tk.Button(self, text="Prev", command= lambda: self.controller.show_frame("homePage"), bg=controller.info, height=3, activebackground=controller.infoFocus)
        prevBtn.grid(row=15, sticky="nsew", column=1)

        # ***** Create Refined Database *****
        refinedDatabaseBtn = tk.Button(self, text="Generate Refined Database", command=self.refinedDB, bg= controller.success, activebackground=controller.successFocus)
        refinedDatabaseBtn.grid(row = 15, sticky="nsew", column =2)   

        # ***** Preview Button *****
        previewBtn = tk.Button(self, text = "Preview", command = lambda: self.controller.show_frame("refinedDatabase"), bg=controller.info, height=3, activebackground=controller.infoFocus)
        previewBtn.grid(row = 15, sticky="nsew", column=3)  

    # ****** Event Listeners ********

    def on_change(self,e):
        global companyName
        companyName = e.widget.get()

    def tenth_input_choice(self,e):
        global tenth_input_choice
        tenth_input_choice = float(e.widget.get())

    def twelth_input_choice(self,e):
        global twelth_input_choice
        twelth_input_choice = float(e.widget.get())

    def btech_input_choice(self,e):
        global btech_input_choice
        btech_input_choice = float(e.widget.get())

    def backlog_entry_choice(self,e):
        global backlog_entry_choice
        backlog_entry_choice = int(e.widget.get())

    def gapyear_entry_choice(self,e):
        global gapyear_entry_choice 
        gapyear_entry_choice = int(e.widget.get())    

    # ***** Refined DataBase Generator *****
    def refinedDB(self):
        global companyName
        companyName += '.xlsm'
        result = rdb.refinedDBcreator('testing_new.xlsm', branchChoices, tenth_input_choice, twelth_input_choice, btech_input_choice, backlog_entry_choice, gapyear_entry_choice, gender_input)
        result.to_excel(companyName, index = False)
        tkmsg.showinfo("DataBase Generated",companyName+" is added to local directory.")

class refinedDatabase(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent, bg=controller.grayDark)
        self.controller = controller

        # Row Configurations
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=25)
        self.rowconfigure(3, weight=1)

        # Column Configurations
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        importBtn = tk.Button(self, text="Select file for preview", relief = "raised", command =self.browseFunc, bg=controller.primary, height=2, font=controller.main_font, activebackground=controller.primaryFocus)
        importBtn.grid(row=1, column=2, sticky="s")

        homePageBtn = tk.Button(self, text="Home Page", command=lambda: controller.show_frame("homePage"), bg=controller.success, height=2, font=controller.main_font, activebackground=controller.successFocus)
        homePageBtn.grid(row=3, column=1, sticky="nsew")

        emailBtn = tk.Button(self, text="Send Email", command= lambda: controller.show_frame("emailWindow"), bg=controller.info, height=2, font=controller.main_font, activebackground=controller.infoFocus)
        emailBtn.grid(row=3, column=2, sticky="nsew")

        companyProfileBtn = tk.Button(self, text="Add Company Profile", command= lambda: controller.show_frame("companyProfile"), bg=controller.success, height=2, font=controller.main_font, activebackground=controller.successFocus)
        companyProfileBtn.grid(row=3, column=3, sticky="nsew")

    def browseFunc(self):
        filename = filedialog.askopenfilename(filetypes=(("Excel files","*.xlsm"),("CSV files","*.csv"),("Text files","*.txt")))
        df = pd.read_excel(filename, converters={'University Roll Number': lambda x: str(x),'Residence No': lambda x: str(x),'Mobile Number': lambda x: str(x)})
        previewData = tk.Label(self, text=df, bg="#BBBDC0")
        previewData.grid(row = 2, column=2)

class emailWindow(tk.Frame):
    def __init__(self,parent, controller):
        tk.Frame.__init__(self, parent, bg=controller.grayDark)
        self.controller = controller   

        importBtn = tk.Button(self, text="Select file for Email", padx = 8, pady=10, relief = "raised", command =self.browseFunc, bg=controller.primary, activebackground = controller.primaryFocus)
        importBtn.pack(side="top")

    def browseFunc(self):
        global toList
        filename = filedialog.askopenfilename(filetypes=(("Excel files","*.xlsm"),("CSV files","*.csv"),("Text files","*.txt")))
        df = pd.read_excel(filename, converters={'University Roll Number': lambda x: str(x),'Residence No': lambda x: str(x),'Mobile Number': lambda x: str(x)})

        # CC display ListBox
        ccList = tk.Listbox(self, width=100)

        for index,row in df.iterrows():
            toList += row['Email'] + ','
            ccList.insert(index+1,row['Email'])

        emailLabel = tk.Label(self, text="Write Interview Letter For:   "+ filename, font= self.controller.heading_font, bg=self.controller.grayDark, fg=self.controller.light)
        emailLabel.pack(side="top")

        # Adding 'From' label
        fromLabel = tk.Label(self, text = "From: "+fromValue, font = self.controller.main_font, bg=self.controller.grayDark, fg=self.controller.light)
        fromLabel.pack(side="top")

        # Adding 'To' Label
        toLabel = tk.Label(self, text="To:", font = self.controller.main_font, bg=self.controller.grayDark, fg=self.controller.light)
        toLabel.pack(side="top")
        ccList.pack(side="top",expand="True", fill="both")

        # **** Adding scroll bar to ccList *****
        ccScroll = tk.Scrollbar(ccList)
        ccScroll.pack(side="right", fill="y")
        ccScroll.config(command = ccList.yview)
        ccList.config(yscrollcommand=ccScroll.set)

        # 'Subject' commit Btn
        subjectCommitBtn = tk.Button(self, text="Commit Subject", command=self.retrieve_subject, bg=self.controller.info, fg=self.controller.light, activebackground=self.controller.infoFocus, height=2)
        subjectCommitBtn.pack(side="right")

        # Adding 'Subject' Label
        self.subject = tk.Text(self, font="lucida-13")
        self.subject.pack(fill="x", expand=True, side="top")

        # 'Body' commit Btn
        bodyCommitBtn = tk.Button(self, text="Commit Body", command=self.retrieve_body, bg=self.controller.info, fg=self.controller.light, activebackground=self.controller.infoFocus, height=2)
        bodyCommitBtn.pack(side="right")

        # Adding textbox
        self.TextArea = tk.Text(self, font="lucida-13")
        self.TextArea.pack(fill="both", expand=True, side="top")

        #Add Ctrl-a/Ctrl-A binding
        self.TextArea.bind("<Control-Key-a>", self.select_all)
        self.TextArea.bind("<Control-Key-a>", self.select_all)

        # Scroll Bar
        Scroll = tk.Scrollbar(self.TextArea)
        Scroll.pack(side="right", fill="y")
        Scroll.config(command=self.TextArea.yview)
        self.TextArea.config(yscrollcommand=Scroll.set)

        # SendEmailButton
        sendEmailBtn = tk.Button(self, text="Confirm", command= self.emailSender, bg=self.controller.success, activebackground=self.controller.successFocus, height=2)
        sendEmailBtn.pack(side="bottom")

    # Ctrl-a function
    def select_all(self,event):
        event.widget.tag_add("sel", "1.0", "end")
        event.widget.mark_set("insert", "1.0")
        event.widget.see("insert")
        return 'break'

    def retrieve_subject(self):
        global emailSubject
        emailSubject = self.subject.get("1.0","end")

    def retrieve_body(self):
        global emailBody
        emailBody = self.TextArea.get("1.0","end")

    def emailSender(self):
        edm.emailFunc(fromValue,toList,emailSubject,emailBody)
        

if __name__ == "__main__":
    app = mainWindow()
    app.title("Placement Software")
    app.mainloop()