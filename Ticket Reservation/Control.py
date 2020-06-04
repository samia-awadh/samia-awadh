from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DBcennect import Dbcennect
from list import ListTicket
root=Tk()
style=ttk.Style()
style.theme_use('classic')
dbconnect=Dbcennect()
root.title('Ticket Reservation')
root.configure(background="lightblue")
style.configure('TButton',background="lightblue")
style.configure('TLabel',background="lightblue")
style.configure('TRadiobutton',background="lightblue")
fullnLabel=ttk.Label(root,text='Full Name',font=('Arial',12)).grid(row=0,column=0,padx=10,pady=10)
fullentry=ttk.Entry(root,width=30,font=('Arial',16))
fullentry.grid(row=0,column=1,columnspan=2,pady=10)
GendLabel=ttk.Label(root,text='Gender',font=('Arial',12)).grid(row=1,column=0)
sGender=StringVar()

Radiobu1=ttk.Radiobutton(root,text='Male',value='Male',variable=sGender).grid(row=1,column=1)
Radiobu2=ttk.Radiobutton(root,text='Female',value='Female',variable=sGender).grid(row=1,column=2)
commentLabel=ttk.Label(root,text='Comments',font=('Arial',12)).grid(row=2,column=0)
Txcomment=Text(root,width=30,height=15,font=('Arial',16))
Txcomment.grid(row=2,column=1,columnspan=2,pady=10,padx=10)
busmit=ttk.Button(root,text='Semit')
busmit.grid(row=3,column=2,pady=10,padx=10)
buList=ttk.Button(root,text='List Res.')
buList.grid(row=3,column=1,pady=10,padx=10)


def busave():
 msg=dbconnect.Add(fullentry.get(),sGender.get(),Txcomment.get(1.0,'end'))
 messagebox.showinfo(title='Add info',message=msg)
 print (fullentry.get(),sGender.get(),Txcomment.get(1.0,'end'))
 fullentry.delete(0,'end')
 Txcomment.delete(1.0,'end')
def buListRes():
      Listrequst=ListTicket()
    
busmit.config(command=busave)
buList.config(command=buListRes)
root.mainloop()
