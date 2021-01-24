from tkinter import Tk, Label, Entry, Button, StringVar
import sympy as sp
from sympy.abc import s, t
from sympy.integrals import inverse_laplace_transform
from sympy.parsing.sympy_parser import parse_expr

T_min = -0.2
T_max = 3


def calc():
    X0, X1 = 1, 1 / s
    W = parse_expr(e1.get())
    Y0 = X0 * W
    Y1 = X1 * W
    y0 = inverse_laplace_transform(Y0, s, t)
    y1 = inverse_laplace_transform(Y1, s, t)
    l2['text'] = y0
    l3['text'] = y1
    p = sp.plot(y0, (t, T_min, T_max), line_color='r', show=False)
    p.extend(sp.plot(y1, (t, T_min, T_max), line_color='g', show=False))
    p.show()


#  Interface
root = Tk()
root.title("Step and impulse response")
root.geometry('1000x500')
l1 = Label(text="Transfer function", width=30, height=3)
l2 = Label(text="", width=30, height=3)
l3 = Label(text="", width=30, height=3)
W0 = StringVar(root, value='1/(0.1*s+1)')
e1 = Entry(root, textvariable=W0, width=40)
b1 = Button(text="Plot", width=20, height=1, command=calc)

l1.grid(row=1, column=1)
e1.grid(row=1, column=2)
b1.grid(row=2, column=1)
l2.grid(row=3, column=1)
l3.grid(row=4, column=1)

root.mainloop()