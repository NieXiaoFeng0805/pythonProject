#身体质量指数BMI#

height,weight = eval(input("输入身高(m)体重(kg)[“，”隔开 ]"))#eval() 计算单个表达式的值#

bmi = weight / pow(height,2)
print("BIM 数值为：{:.2f}".format(bmi))

people = ""
if( bmi <18.5):
    people = "偏瘦"
elif 18.5<= bmi <25:
    people = "正常"
elif 25 <= bmi <32:
    people = "偏胖"
else:
    people = "肥胖"

print("BMI 指标为：国际'{0}'".format(people))
