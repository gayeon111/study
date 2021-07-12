l=int(input("길이를 입력하시오:"))
import turtle as t
t.shape("turtle")

t.circle(l)
t.up()
t.goto(0,l*2)
t.down()
t.circle(l/2)
