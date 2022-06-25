#DayDayUp.py
#千分之一的力量
DayUp = pow(1.001,365)
DayDown = pow(0.999,365)
print("向上：{:.2f},向下：{:.2f}".format(DayUp,DayDown))

#千分之五的力量
DayFactor = 0.005
DayUp1 = pow(1+DayFactor,365)
DayDown1 = pow(1-DayFactor,365)
print("向上:{:.2f},向下:{:.2f}".format(DayUp1,DayDown1))
