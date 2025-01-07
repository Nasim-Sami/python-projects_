from tkinter import *
from tkinter import messagebox
from sqlite3 import *
import home
def main():
    root=Tk()
    root.title("LOGIN")
    root.geometry('600x650')
    root.resizable(0,0)


    def create_login_table():
        con=connect('connect.db')
        cur=con.cursor()
        cur.execute(''' 
                    CREATE TABLE IF NOT EXISTS login(
                    username TEXT NOT NULL UNIQUE, -- Add UNIQUE constraint here to prevent duplicate username
                    password TEXT NOT NULL)''')
        cur.execute("insert or ignore into login(username,password) values(?,?)",('admin','admin'))

        con.commit()
        con.close()

    create_login_table()

    def list_table():
        con=connect('connect.db')
        cur=con.cursor()
        cur.execute("select name from sqlite_master where type='table';")
        print(cur.fetchall())
        con.close()
    list_table()
    
    def list_login_TABLE_content():
        con=connect('connect.db')
        cur=con.cursor()
        cur.execute("select * from login")
        print(cur.fetchall())
        con.close()
    list_login_TABLE_content()


    # import os
    # if os.path.exists('connect.db'):
    #  os.remove('connect.db')


    def handle_login_btn():
        con=connect('connect.db')
        cur=con.cursor()
        cur.execute("select * from login where username=? and password=?",(username_entry.get(),password_entry.get()))
        result=cur.fetchone()
        # print(cur.fetchone())
        if result is not None:
            messagebox.showinfo("SUCCESSFUL LOGIN")
            root.destroy()
            home.main()
        else:
            messagebox.showerror("INVALID","incorrect username or password")


    header_frame= Frame(root,background='blue',height=60,width=200)
    header_frame.pack(fill='x')
    
    label=Label(header_frame,text='Facebook',bg='blue',fg='white',font=("Arial", 24, "bold"))
    # label.pack(side='left',pady=10)
    label.pack(ipady=10)
    content_frame=Frame(root,background='white')
    content_frame.pack(fill=BOTH,expand=True)
    login_frame=Frame(content_frame,background='#f2f2f2')
    login_frame.place(relx=0.5,rely=0.5,anchor=CENTER)
    login_label=Label(login_frame,text="Login Form",fg='white',bg='blue',width=30,font=("Arial",20, "bold"))
    login_label.grid(row=0,column=0,columnspan=2,ipady=5)

    username_label=Label(login_frame,text='username',fg='black',bg='white',font=("verdana",15,"bold",))
    username_label.grid(row=1,column=0,pady=10)

    username_entry=Entry(login_frame,text='',fg='black',bg='white')
    username_entry.grid(row=1,column=1,pady=10,ipady=5)

    password_label=Label(login_frame,text='password',fg='black',bg='white',font=("verdana",15,"bold",))
    password_label.grid(row=2,column=0,pady=10)

    password_entry=Entry(login_frame,text='',fg='black',bg='white',show='*')
    password_entry.grid(row=2,column=1,pady=10,ipady=5)

    login_btn=Button(login_frame,text='Login',width=7,height=2,bg='blue',fg='green',font=("verdana",15,"bold"),command=handle_login_btn)
    login_btn.grid(row=3,columnspan=2)


    root.mainloop()
 
    

if __name__ == "__main__":
    main()


