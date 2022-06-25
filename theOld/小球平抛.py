import math as m
t=float(input("输入下落时间："))
v0=5.0
g=9.8
x=v0*t
h=0.5*g*(t*t)

s=m.sqrt(h*h+x*x)
print("小球距原点：",s)


