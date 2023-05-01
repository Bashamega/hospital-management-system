from tkinter import *
from tkinter import ttk
import sqlite3

from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from tkinter import messagebox
import os
connect = sqlite3.connect("register.db")
cursor = connect.cursor()
cursor.execute(" CREATE TABLE IF NOT EXISTS  MYTABLE (NAME TEXT ,PASS INTEGER)")
ro = cursor.fetchall()
print(ro)
connect.close()
tree = 0
con = sqlite3.connect("app.db")
cur = con.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS DOC(DODD TEXT, DOCNAME TEXT, DOCEXP TEXT, DOCPASS TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS PAT("
            "PatientID TEXT,"
            " PatientName TEXT,"
            " PatientAddress TEXT,"
            " PatientPhone TEXT,"
            "PatientAge TEXT,"
            "MajorDisease TEXT,"
            "PatientGender TEXT,"
            "PatientBlood TEXT)")
cur.execute(" CREATE TABLE IF NOT EXISTS  DIAGNOSE (DIAGDD TEXT, ID TEXT, NAME TEXT, SYMPTOMS TEXT, DIAGNOSE TEXT, MEDICINE TEXT)")

con.close()

def up_doc():
    global tree
    for record in tree.get_children():
        tree.delete(record)

    con = sqlite3.connect("app.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM DOC")
    ro = cur.fetchall()
    print(ro)
    for i in ro:
        row = (i[0], i[1], i[2], i[3])

        tree.insert('', 'end', text="1", values=row)

    messagebox.showinfo("Hospital Management system", "Completed")
def home():

    root = Tk()
    root.title("Hospital Management system")
    root.geometry("400x400")
    root.resizable(0,0)
    Label(root, text="Hospital Management system").pack()
    input1 = 0
    input2 = 0
    input3 = 0
    input4 = 0

    def fun_doc():
        global input1
        global input2
        global input3
        global input4
        input1a = input1.get()
        input2a = input2.get()
        input3a = input3.get()
        input4a = input4.get()
        print(input1a + input2a + input3a + input4a + "D")
        co = sqlite3.connect("app.db")
        cursor = co.cursor()
        cursor.execute('INSERT INTO DOC VALUES(?, ?, ?, ?)', (input1a, input2a, input3a, input4a,))

        co.commit()
        co.close()
        co.close()
        up_doc()

    def update_doc():
        global input1
        global input2
        global input3
        global input4
        input1a = input1.get()
        input2a = input2.get()
        input3a = input3.get()
        input4a = input4.get()
        print(input1a + input2a + input3a + input4a + "D")
        connect = sqlite3.connect("app.db")
        cursor = connect.cursor()
        cursor.execute("UPDATE DOC SET DODD=? , DOCEXP=?, DOCPASS=? WHERE DocName=?", (input1a, input3a, input4a, input2a,))
        connect.commit()
        connect.close()
        up_doc()

    def Delete_doc():
        global input1
        global input2
        global input3
        global input4
        input1a = input1.get()
        input2a = input2.get()
        input3a = input3.get()
        input4a = input4.get()
        print(input1a + input2a + input3a + input4a + "D")
        print(input2a)
        connect = sqlite3.connect("app.db")
        cursor = connect.cursor()
        cursor.execute("DELETE FROM DOC WHERE DOCNAME=?", (input2a,))
        connect.commit()
        connect.close()
        up_doc()

    def doc():
        global tree
        global input1
        global input2
        global input3
        global input4
        doc_root = Tk()
        doc_root.resizable(0,0)
        doc_root.geometry("800x500")
        doc_root.title("Doctor")
        top = Frame(doc_root, background="lightgreen", width=800, height=100)
        top.pack(side="top")
        leb = Label(top, text="Doctor", background="lightgreen", font=("Arial Bold", 50))
        leb.place(relx=0.5, rely=0.5, anchor=CENTER)
        input1 = Entry(doc_root)
        input1.place(x=100, y=150)

        input2 = Entry(doc_root)
        input2.place(x=100, y=200)
        input3 = Entry(doc_root)
        input3.place(x=100, y=250)
        input4 = Entry(doc_root)
        input4.place(x=100, y=300)
        Label(doc_root, text="Dodd").place(x=25, y=150)
        Label(doc_root, text="Doc name").place(x=25, y=200)
        Label(doc_root, text="Doc EXP").place(x=25, y=250)
        Label(doc_root, text="Doc Pass").place(x=25, y=300)
        Button(doc_root, text="Add", background="lightgreen", command=fun_doc).place(x=100, y=400)
        Button(doc_root, text="Update", background="lightgreen", command=update_doc).place(x=150, y=400)
        Button(doc_root, text="Delete", background="lightgreen", command=Delete_doc).place(x=220, y=400)
        Button(doc_root, text="Home", background="lightgreen", command=home).place(x=150, y=450)
        # treeview


        tree = ttk.Treeview(doc_root, column=("Dodd", "Doc name", "Doc Exp", "Doc Pass"), show='headings', height=8)
        tree.place(x=250, y=200)
        tree.column("# 1", anchor=CENTER, minwidth=0, width=100)
        tree.heading("# 1", text="Dodd")
        tree.column("# 2", anchor=CENTER, minwidth=0, width=100)
        tree.heading("# 2", text="Doc name")
        tree.heading("#3", text="Doc Exp")
        tree.column("#3", anchor=CENTER, minwidth=0, width=100)
        tree.heading("#4", text="Doc pass")
        tree.column("#4", anchor=CENTER, minwidth=0, width=100)
        con = sqlite3.connect("app.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM DOC")
        ro = cur.fetchall()
        print(ro)
        for i in ro:
            row = (i[0], i[1], i[2], i[3])

            tree.insert('', 'end', text="1", values=row)


    def sick():

        root_sick = Tk()
        root_sick.resizable(0,0)

        root_sick.geometry("1500x700")
        root_sick.title("Patient")
        top = Frame(root_sick, background="lightgreen", width=1500, height=100)
        top.pack(side="top")
        leb = Label(top, text="Patient", background="lightgreen", font=("Arial Bold", 50))
        leb.place(relx=0.5, rely=0.5, anchor=CENTER)
        entry1 = Entry(root_sick)
        entry2 = Entry(root_sick)
        entry3 = Entry(root_sick)
        entry4 = Entry(root_sick)
        entry5 = Entry(root_sick)
        entry6 = Entry(root_sick)

        entry1.place(x=100, y=200)
        entry2.place(x=100, y=250)
        entry3.place(x=100, y=300)
        entry4.place(x=100, y=350)
        entry5.place(x=100, y=400)
        entry6.place(x=100, y=450)

        val = ['FEMALE', 'MALE']
        Gender = ttk.Combobox(root_sick, values=val)
        Gender.place(x=250,y=200)
        val = ["A+", "c+", "B+", "AB+", "A-", "O-", "B-", "AB-"]
        blood = ttk.Combobox(root_sick, values=val)
        blood.place(x=250, y=400)
        tree = ttk.Treeview(root_sick, column=("PatientID",
                                               "PatientName",
                                               "PatientAddress",
                                               "PatientPhone", "PatientAge",
                                               "PatientGender", "PatientBlood",
                                               "MajorDisease"), show='headings', height=8)
        tree.place(x=500, y=200)
        tree.column("# 1", anchor=CENTER, minwidth=0, width=100)
        tree.heading("# 1", text="PatientID")
        tree.column("# 2", anchor=CENTER, minwidth=0, width=100)
        tree.heading("# 2", text="PatientName")
        tree.heading("#3", text="PatientAddress")
        tree.column("#3", anchor=CENTER, minwidth=0, width=100)
        tree.heading("#4", text="PatientPhone")
        tree.column("#4", anchor=CENTER, minwidth=0, width=100)
        tree.heading("#5", text="PatientAge")
        tree.column("#5", anchor=CENTER, minwidth=0, width=100)
        tree.heading("#6", text="PatientGender")
        tree.column("#6", anchor=CENTER, minwidth=0, width=100)
        tree.heading("#7", text="PatientBlood")
        tree.column("#7", anchor=CENTER, minwidth=0, width=100)
        tree.heading("#8", text="MajorDisease")
        tree.column("#8", anchor=CENTER, minwidth=0, width=100)

        con = sqlite3.connect("app.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM PAT")
        ro = cur.fetchall()
        print(ro)
        for i in ro:
            row = i

            tree.insert('', 'end', text="1", values=row)
        def up():
            for record in tree.get_children():
                tree.delete(record)

            con = sqlite3.connect("app.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM PAT")
            ro = cur.fetchall()
            print(ro)
            for i in ro:
                row = (i[0], i[1], i[2], i[3])

                tree.insert('', 'end', text="1", values=row)

            messagebox.showinfo("Hospital Management system", "Completed")
        def add():
            entry1a = entry1.get()
            entry2a = entry2.get()
            entry3a = entry3.get()
            entry4a = entry4.get()
            entry5a = entry5.get()
            entry6a = Gender.get()
            entry7a = blood.get()
            entry8a = entry6.get()
            print(entry1a)
            print(entry2a)
            print(entry3a)
            print(entry4a)
            print(entry5a)
            print(entry6a)
            print(entry7a)
            print(entry8a)
            co = sqlite3.connect("app.db")
            cursor = co.cursor()
            cursor.execute('INSERT INTO PAT VALUES(?, ?, ?, ?, ?, ?, ?, ?)', (entry1a, entry2a, entry3a, entry4a, entry5a, entry6a, entry7a, entry8a,))
            co.commit()
            up()


        def update():
            entry1a = entry1.get()
            entry2a = entry2.get()
            entry3a = entry3.get()
            entry4a = entry4.get()
            entry5a = entry5.get()
            entry6a = Gender.get()
            entry7a = blood.get()
            entry8a = entry6.get()
            print(entry1a)
            print(entry2a)
            print(entry3a)
            print(entry4a)
            print(entry5a)
            print(entry6a)
            print(entry7a)
            print(entry8a)
            co = sqlite3.connect("app.db")
            cursor = co.cursor()
            cursor.execute("UPDATE PAT SET PatientID=?"
                           " , PatientAddress=?, "
                           "PatientPhone=?,"
                           " PatientAge=?, MajorDisease=?, PatientGender=?, PatientBlood=? WHERE PatientName=?",
                           (entry1a, entry3a, entry4a, entry5a, entry6a, entry7a, entry8a, entry2a,))
            co.commit()
            up()
        def Delete():

            entry1a = entry1.get()
            entry2a = entry2.get()
            entry3a = entry3.get()
            entry4a = entry4.get()
            entry5a = entry5.get()
            entry6a = Gender.get()
            entry7a = blood.get()
            entry8a = entry6.get()
            print(entry1a)
            print(entry2a)
            print(entry3a)
            print(entry4a)
            print(entry5a)
            print(entry6a)
            print(entry7a)
            print(entry8a)
            co = sqlite3.connect("app.db")
            cursor = co.cursor()
            cursor.execute("DELETE FROM PAT WHERE PatientName=?", (entry2a,))
            co.commit()
            up()
        Button(root_sick, text="Add", background="lightgreen", command=add).place(x=100, y=550)
        Button(root_sick, text="Update", background="lightgreen", command=update).place(x=150, y=550)
        Button(root_sick, text="Delete", background="lightgreen", command=Delete).place(x=220, y=550)
        Button(root_sick, text="Home", background="lightgreen", command=home).place(x=150, y=600)





    def diagnose_fun():
        root_diagnose = Tk()
        root_diagnose.geometry("1500x700")
        root_diagnose.title("Diagnose")
        root_diagnose.resizable(0,0)

        top = Frame(root_diagnose, background="lightgreen", width=1500, height=100)
        top.pack(side="top")

        leb = Label(top, text="Patient", background="lightgreen", font=("Arial Bold", 50))
        leb.place(relx=0.5, rely=0.5, anchor=CENTER)
        entry1 = Entry(root_diagnose)
        val = ['101', '102', '103', '105']
        entry2 = ttk.Combobox(root_diagnose, values=val)
        entry3 = Entry(root_diagnose)
        entry4 = Entry(root_diagnose)
        entry5 = Entry(root_diagnose)
        entry6 = Entry(root_diagnose)
        entry1.place(x=100, y=150)
        entry2.place(x=100, y=200)
        entry3.place(x=100, y=250)
        entry4.place(x=300, y=150)
        entry5.place(x=300, y=200)
        entry6.place(x=300, y=250)
        tree = ttk.Treeview(root_diagnose, column=("DIAGDD, ID, NAME, SYMPTOMS, DIAGNOSE, MEDICINE"), show='headings', height=8)
        tree.place(x=100, y=450)
        tree.column("# 1", anchor=CENTER, minwidth=0, width=100)
        tree.heading("# 1", text="DIAGDD")
        tree.column("# 2", anchor=CENTER, minwidth=0, width=100)
        tree.heading("# 2", text="ID")
        tree.heading("#3", text="NAME")
        tree.column("#3", anchor=CENTER, minwidth=0, width=100)
        tree.heading("#4", text="SYMPTOMS")
        tree.column("#4", anchor=CENTER, minwidth=0, width=100)
        tree.heading("#5", text="DIAGNOSE")
        tree.column("#5", anchor=CENTER, minwidth=0, width=100)
        tree.heading("#6", text="MEDICINE")
        tree.column("#6", anchor=CENTER, minwidth=0, width=100)

        con = sqlite3.connect("app.db")
        cur = con.cursor()

        cur.execute("SELECT * FROM diagnose")
        ro = cur.fetchall()
        print(ro)
        for i in ro:
            row = i

            tree.insert('', 'end', text="1", values=row)

        def up():
            for record in tree.get_children():
                tree.delete(record)

            con = sqlite3.connect("app.db")
            cur = con.cursor()

            cur.execute("SELECT * FROM Diagnose")
            ro = cur.fetchall()
            print(ro)
            for i in ro:
                row = (i[0], i[1], i[2], i[3])

                tree.insert('', 'end', text="1", values=row)

            messagebox.showinfo("Hospital Management system", "Completed")
        def add():
            entry1a = entry1.get()
            entry2a = entry2.get()
            entry3a = entry3.get()
            entry4a = entry4.get()
            entry5a = entry5.get()
            entry6a = entry6.get()

            print(entry1a)
            print(entry2a)
            print(entry3a)
            print(entry4a)
            print(entry5a)
            print(entry6a)

            co = sqlite3.connect("app.db")
            cursor = co.cursor()
            cursor.execute('INSERT INTO Diagnose VALUES(?, ?, ?, ?, ?, ?)', (entry1a, entry2a, entry3a, entry4a,
                                                                              entry5a, entry6a,))
            co.commit()
            up()
        def update():
            entry1a = entry1.get()
            entry2a = entry2.get()
            entry3a = entry3.get()
            entry4a = entry4.get()
            entry5a = entry5.get()
            entry6a = entry6.get()

            print(entry1a)
            print(entry2a)
            print(entry3a)
            print(entry4a)
            print(entry5a)
            print(entry6a)

            co = sqlite3.connect("app.db")
            cursor = co.cursor()
            cursor.execute("UPDATE Diagnose SET DIAGDD=?"
                           " , ID=?, "
                           "SYMPTOMS=?,"
                           " DIAGNOSE=?, MEDICINE=? WHERE Name=?",
                           (entry1a, entry2a, entry4a, entry5a, entry6a,  entry3a,))
            co.commit()
            up()

        def Delete():
            entry1a = entry1.get()
            entry2a = entry2.get()
            entry3a = entry3.get()
            entry4a = entry4.get()
            entry5a = entry5.get()
            entry6a = entry6.get()

            print(entry1a)
            print(entry2a)
            print(entry3a)
            print(entry4a)
            print(entry5a)
            print(entry6a)

            co = sqlite3.connect("app.db")
            cursor = co.cursor()
            cursor.execute("DELETE FROM Diagnose WHERE Name=?", (entry3a,))
            co.commit()
            up()
        def pdfprint():
            co = sqlite3.connect("app.db")
            cursor = co.cursor()
            cursor.execute('SELECT * FROM Diagnose')
            data = cursor.fetchall()

            # Create the PDF document
            doc = SimpleDocTemplate("Print.pdf", pagesize=landscape(letter))

            # Create the table and add the data
            table = Table(data)
            table.setStyle(TableStyle([

                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),

                ('GRID', (0, 0), (-1, -1), 1, colors.black)
            ]))

            # Add the table to the PDF document
            doc.build([table])

            os.startfile("Print.pdf")

        Button(root_diagnose, text="Add", background="lightgreen", command=add).place(x=100, y=300)
        Button(root_diagnose, text="Update", background="lightgreen", command=update).place(x=150, y=300)
        Button(root_diagnose, text="Delete", background="lightgreen", command=Delete).place(x=220, y=300)
        Button(root_diagnose, text="Home", background="lightgreen", command=home).place(x=150, y=400)
        Button(root_diagnose, text="print", command=pdfprint).place(x=600, y=350)

    doctor_var = Button(root, text="Doctor", command=doc)
    patient_var = Button(root, text="Patient", command=sick)
    diagnose_var = Button(root, text="Diagnose", command=diagnose_fun)

    doctor_var.place(x=100, y=200)
    patient_var.place(x=200, y=200)
    diagnose_var.place(x=300, y=200)
    root.mainloop()


def log():
    root = Tk()
    root.resizable(0,0)
    root.title("Log")
    root.geometry("300x400")
    Label(root, text="WELCOME").pack()
    user = Entry()
    password = Entry(show="*")
    user.place(x=100, y=100)
    password.place(x=100, y=200)

    def sql_log():
        user1 = user.get()
        password1 = password.get()
        print(user1)
        print(password1)
        co = sqlite3.connect("register.db")
        cur1 = co.cursor()
        cur1.execute("SELECT * FROM MyTable WHERE Name=? and Pass=?", [user1, password1])

        if cur1.fetchone() == None:
            Label(root, text='Incorrect Username, or password').pack()
        else:

            root.destroy()
            home()

    Button(root, text="Login", command=sql_log).place(x=100, y=300)
    root.mainloop()


log()

