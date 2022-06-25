x=float(input('输入身高(m)：'))
y=float(input('输入体重(kg)：'))

BMIG=y/(x*x)
BMIChina=y/(x*x)
if BMIG<18.5:
    print('你的BMI为：%.2f,体态状况是偏瘦。'%BMIG)
if 18.5<=BMIChina<=24:
    print('你的BMI（国内）为:%.2f,体态状况是正常。'%BMIChina)
elif 18.5<=BMIG<=25:
    print('你的BMI(国际)为:%.2f，体态状况是正常。'%BMIG)
if 25<BMIG<=30:
    print('你的BMI(国际)为:%.2f，体态状况是偏胖。'% BMIG)
elif 24<BMIChina<=28:
    print('你的BMI(国内)为:%.2f，体态状况是偏胖。' % BMIChina)
if BMIG>=30:
    print('你的BMI(国际)为:%.2f，体态状况是肥胖。' % BMIG)
elif BMIChina>=30:
    print('你的BMI(国内)为:%.2f，体态状况是肥胖。' % BMIChina)






#print('BMI为：',BMI)