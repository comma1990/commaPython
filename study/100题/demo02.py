# @Author  :  comma 
# @Date    :  2021-01-17 10:56


'''
【程序2】
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高
　　　于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提
　　　成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于
　　　40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于
　　　100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
1.程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。　
    　　　　　
2.程序源代码：
'''
lr=eval(input('请输入利润（单位：万）：'))
if lr<=10:
    jiang=lr*0.1
elif lr<=20:
    jiang=(lr-10)*0.075+10*0.1
elif lr<=40:
    jiang=1+0.75+(lr-20)*0.03
elif lr<60:
    jiang=1+0.75+0.6+(lr-40)
elif lr<100:
    jiang=1+0.75+0.6+(lr-60)*0.015
else:
    jiang=1+0.75+0.6+0.6+(lr-100)*0.01
print(jiang)