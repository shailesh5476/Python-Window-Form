import tkinter
import pymysql
r = tkinter.Tk()

r.title("Software Engineer Shailesh Kumar Gupta")
r.geometry("1500x1000")
r.configure(bg="Green")




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


Z = tkinter.Button(r, text="Submit", bg="yellow")
Z.place(x=900, y=600)

tkinter.mainloop()
