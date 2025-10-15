import tkinter
import tkinter.messagebox as m
import pymysql
r = tkinter.Tk()

r.title("Software Engineer Shailesh Kumar Gupta")
r.geometry("1500x1000")
r.configure(bg="Green")

def connectdb(): 
    return pymysql.connect(host="localhost",database="student",user="root",password="",port=3306)


def insertdata():
     conn=connectdb() 
     a1=a.get() 
     a2=b.get()
     a3=c.get()
     a4=d.get() 
     a5=e.get() 
     a6=f.get() 
     a7=g.get()
     a8=h.get() 
     a9=i.get() 
     b1=j.get() 
     b2=k.get() 
     b3=l.get() 
     b4=m.get() 
     b5=n.get() 
     b6=o.get() 
     b7=p.get() 
     b8=q.get() 
     b9=r1.get()
     if(a1==""or a2=="" or a3=="" or a4=="" or a5=="" or a6=="" or a7=="" or a8=="" or a9=="" or b1=="" or b2=="" or b3=="" or b4=="" or b5=="" or b6=="" or b7=="" or b8=="" or b9=="" ):
        m.showinfo("Insert Status","All Fields are Mandatory") 
     else:
        try:
            conn = connectdb()
            cur=conn.cursor() 
            ar=(a1,a2,a3,a4,a5,a6,a7,a8,a9,b1,b2,b3,b4,b5,b6,b7,b8,b9)
            querty="insert into student_Details values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cur.execute(querty,ar) 
            conn.commit()
            m.showinfo("Insert Status","Data Inserted Successfully") 
            conn.close()
        except Exception as ee:
            print("Data Not Inserted error no.420",ee)



sh = tkinter.Label(r, text="Student Roll Number -:")
sh.place(x=20, y=20)

course = tkinter.Label(r, text="Course Name -:")
course.place(x=20, y=50)

branch = tkinter.Label(r, text="Branch Name -:")
branch.place(x=20, y=80)

fn = tkinter.Label(r, text="Student First Name -:")
fn.place(x=20, y=110)

mn = tkinter.Label(r, text="Student Middle Name -:")
mn.place(x=20, y=140)

mn1 = tkinter.Label(r, text="Student Last Name -:")
mn1.place(x=20, y=170)

f_n = tkinter.Label(r, text="Student Father Name -:")
f_n.place(x=20, y=200)

m_n = tkinter.Label(r, text="Student Mother Name -:")
m_n.place(x=20, y=230)

man = tkinter.Label(r, text="Student Adhaar Number -:")
man.place(x=20, y=260)

mmn = tkinter.Label(r, text="Contact Number -:")
mmn.place(x=20, y=290)

fa_n = tkinter.Label(r, text="Student Address name -:")
fa_n.place(x=20, y=320)

ms_n1= tkinter.Label(r, text="Student Street Adddress name -:")
ms_n1.place(x=20, y=350)

ms_n = tkinter.Label(r, text="Student Entry date -:")
ms_n.place(x=20, y=380)

fees = tkinter.Label(r, text="Addmission Fees -:")
fees.place(x=20, y=410)

quali = tkinter.Label(r, text="Highest Qualification Document -:")
quali.place(x=20, y=440)

adhaar = tkinter.Label(r, text="Adhaar Card Document -:")
adhaar.place(x=20, y=470)

Photo = tkinter.Label(r, text="Student Photo -:")
Photo.place(x=20, y=500)

Tumb = tkinter.Label(r, text="Thumb Image -:")
Tumb.place(x=20, y=530)

# entry box created

a = tkinter.Entry(width=30)
a.place(x=500, y=20)

b = tkinter.Entry(width=30)
b.place(x=500, y=50)

c = tkinter.Entry(width=30)
c.place(x=500, y=80)

d = tkinter.Entry(width=30)
d.place(x=500, y=110)

e = tkinter.Entry(width=30)
e.place(x=500, y=140)

f = tkinter.Entry(width=30)
f.place(x=500, y=170)

g = tkinter.Entry(width=30)
g.place(x=500, y=200)

h = tkinter.Entry(width=30)
h.place(x=500, y=230)

i = tkinter.Entry(width=30)
i.place(x=500, y=260)

j = tkinter.Entry(width=30)
j.place(x=500, y=290)

k = tkinter.Entry(width=30)
k.place(x=500, y=320)

l = tkinter.Entry(width=30)
l.place(x=500, y=350)

m = tkinter.Entry(width=30)
m.place(x=500, y=380)

n = tkinter.Entry(width=30)
n.place(x=500, y=410)

o = tkinter.Entry(width=30)
o.place(x=500, y=440)

p = tkinter.Entry(width=30)
p.place(x=500, y=470)

q = tkinter.Entry(width=30)
q.place(x=500, y=500)

r1 = tkinter.Entry(width=30)
r1.place(x=500, y=530)
# Adding button into main window


Z = tkinter.Button(r, text="Submit", bg="yellow",command=insertdata)
Z.place(x=900, y=600)

tkinter.mainloop()
