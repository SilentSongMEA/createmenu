from tkinter import *
colorbg="#0b5345"
colorfg="#fbff00"
colorbgb="#a7fff0"
coloracti="#154360"
fontb='B nazanin'
root=Tk()


import sqlite3
con=sqlite3.connect("form.db")
c=con.cursor()



def ckst(i,o,p):
    global a
    global b
    global c
    if i==1:
        a='وب'
    else:
        a=''
    if o==1:
        b='شبکه'
    else:
        b=''
    if p==1:
        c='برنامه نویسی'
    else:
        c=''
    return(i,o,p)

def imp():
    x=inp1.get()
    y=inp2.get()
    z=inp3.get()
    q=ckst(x,y,z)
    d=inp.get()
    dsp1=Label(root,fg=colorfg,bg=colorbg,height=8,width=25,font=(fontb,14,'bold'))
    dsp1.place(x=300,y=400)
    dsp2=Label(root,text=entcodem.get()+('\n'+entname.get())+('\n'+entlast.get())+('\n'+a)+('\n'+b)+('\n'+c)+('\n'+d),fg=colorfg,bg=colorbg,height=8,width=25,font=(fontb,14,'bold'))
    dsp2.place(x=300,y=400)
    t1=[(entcodem.get()),entname.get(),entlast.get(),a,b,c,d]
    c.execute('''INSERT INTO user VALUES(?,?,?,?,?,?,?)''',t1)
    con.commit()

def dell():
    desp1=Label(root,fg=colorfg,bg=colorbg,height=8,width=25,font=(fontb,14,'bold'))
    desp1.place(x=300,y=400)
    y=[]
    c.execute("SELECT * from user")
    o=(c.fetchall())
    z=entcodem.get()
    for i in o:
        y.append(i[0])

    if z in y:
        z=[entcodem.get()]
        c.execute("DELETE FROM user WHERE code=? ;",z)
        desp2=Label(root,text="delete",fg=colorfg,bg=colorbg,height=8,width=25,font=(fontb,14,'bold'))
        desp2.place(x=300,y=350)
        con.commit()
    else:
        desp2=Label(root,text="dont exits this code",fg=colorfg,bg=colorbg,height=8,width=25,font=(fontb,14,'bold'))
        desp2.place(x=300,y=350)
        
root.geometry('640x440')
root.title('register form')
root.configure(bg=colorbg,borderwidth=5,highlightthickness=7,highlightcolor=colorbgb)

lblcodem=Label(root,text='کدملی',height=1,bg=colorbg,width=7,fg=colorfg,font=(fontb,14,'bold'))
lblcodem.grid(row=0,column=0)
entcodem=Entry(root,font=(fontb,14,'bold'))
entcodem.grid(row=0,column=1)


lblname=Label(root,text='نام',height=1,bg=colorbg,width=7,fg=colorfg,font=(fontb,14,'bold'))
lblname.grid(row=1,column=0)
entname=Entry(root,font=(fontb,14,'bold'))
entname.grid(row=1,column=1)


lbllast=Label(root,text='نام خانوادگی',height=1,bg=colorbg,width=7,fg=colorfg,font=(fontb,14,'bold'))
lbllast.grid(row=2,column=0)
entlast=Entry(root,font=(fontb,14,'bold'))
entlast.grid(row=2,column=1)


lblsf=Label(root,text='فیلد خود را انتخاب نمایید ',height=1,bg=colorbg,fg=colorfg,font=(fontb,14,'bold'))
lblsf.place(x=80,y=120)

inp1=IntVar()
inp2=IntVar()
inp3=IntVar()

chweb=Checkbutton(root,text='وب',bg=colorbg,activebackground=coloracti,activeforeground=colorfg,variable=inp1,font=(fontb,14,'bold'))
chweb.place(x=100,y=170)

chnet=Checkbutton(root,text='شبکه',bg=colorbg,activebackground=coloracti,activeforeground=colorfg,variable=inp2,font=(fontb,14,'bold'))
chnet.place(x=200,y=170)

chprog=Checkbutton(root,text='برنامه نویسی',bg=colorbg,activebackground=coloracti,activeforeground=colorfg,variable=inp3,font=(fontb,14,'bold'))
chprog.place(x=300,y=170)

lblradio=Label(root,text='سن خود را وارد نمایید',bg=colorbg,fg=colorfg,font=(fontb,14,'bold'))
lblradio.place(x=10,y=220)
inp=StringVar()
inp.set('age 20-30')
r1=Radiobutton(root,text='age 20-30',bg=colorbg,variable=inp,value='age 20-30',font=(fontb,14,'bold'))
r1.place(x=100,y=250)

r2=Radiobutton(root,text='age 30-40',bg=colorbg,variable=inp,value='age 30-40',font=(fontb,14,'bold'))
r2.place(x=250,y=250)

r3=Radiobutton(root,text='age 40-50',bg=colorbg,variable=inp,value='age 40-50',font=(fontb,14,'bold'))
r3.place(x=400,y=250)

btnimport=Button(root,text='import',bd=6,fg=colorfg,bg=colorbg,font=(fontb,14,'bold'),command=imp)
btnimport.place(x=100,y=330)

btnDelete=Button(root,text='delete',bd=6,fg=colorfg,bg=colorbg,font=(fontb,14,'bold'),command=dell)
btnDelete.place(x=200,y=330)


mainloop()
