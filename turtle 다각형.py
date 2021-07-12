m=int(input("주기:"))
n=int(input("크기:"))

import turtle as t
t.shape("turtle")


t.left(90)
for i in range(2):
    t.forward(m/2)
    t.right(90)
    t.forward(n)
    t.right(90)
    t.forward(n*2)
    t.left(90)
    t.forward(m/2)
    t.left(90)
    t.forward(n)
