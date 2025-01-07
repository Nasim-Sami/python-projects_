from tkinter import *
from tkinter import messagebox

def main():
    root=Tk()
    root.title("LOGIN")
    root.geometry('900x650')
    root.resizable(0,0)

    label=Label(root,text='''Alogorithm you followed to make "connect with database.py" : \n\n1.Import dependencies
        \n2.write main function>create tk() instance and define its geometry,title etc
         \n3.design the interface
                ---make a header frame 
                ---make a content frame
                ---make a login frame
                   ---design username and password
                 label and their entry
                ---design a login button
                
        \n4.Now create a database table
                ---connect>cursor object to execute command>Execute command for making a table>
                commit>close
        \n 5.create a function to view list of table and another function to view content of table
        \n6.Make a function for handling login button  ''',
                background='Red',foreground='Black',font=("Aerial",15,'bold'))
    label.pack()
    

    root.mainloop()

if __name__ == "__main__":
    main()