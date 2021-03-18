#author : comma
#date : 2021/1/18 10:31

'''
【程序5】
题目：输入三个整数x,y,z，请把这三个数由小到大输出。
1.程序分析：我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，
　　　　　　然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。
2.程序源代码：
'''

a = 176
b = 219
print (chr(b),chr(a),chr(a),chr(a),chr(b))
print (chr(a),chr(b),chr(a),chr(b),chr(a))
print (chr(a),chr(a),chr(b),chr(a),chr(a))
print (chr(a),chr(b),chr(a),chr(b),chr(a))
print (chr(b),chr(a),chr(a),chr(a),chr(b))