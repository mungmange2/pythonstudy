import sys
import glob
import time
import random
import os 

# 05장 연습문제
# https://wikidocs.net/42529

#01
class Calculator:
    def __init__(self):
        self.value = 0

    def add(self, val):
        self.value += val

class UpgradeCalculator(Calculator):
    def minus(self, val):
        self.value -= val

cal = UpgradeCalculator()
cal.add(10)
cal.minus(7)

print("Q.01>>>{}".format(cal.value)) 


#02
class MaxLimitCalculator2(Calculator):
    def add(self, val):
        self.value += val
        if self.value > 100: 
            self.value = 100 
cal = MaxLimitCalculator2()
cal.add(50)
cal.add(60)

print("Q.02>>>{}".format(cal.value)) 

class MaxLimitCalculator(Calculator):
    def add(self, val):
        super().add(val)
        if self.value > 100:
            self.value = 100
        
print("Q.02>>>{}".format(cal.value)) 


#03
#all([1, 2, abs(-3)-3]) -> 
#chr(ord('a')) == 'a' -> 아스키코드값 -> 97 -> char
print(all([1, 2, -1]))
print(chr(ord('a')) == 'a')

#04
a = [1, -2, 3, -5, 8, -3]
result = filter(lambda x : x > 0, a)
#print(result)
print("Q.04>>>{}".format(list(result)))


#05
aa = hex(234)
print("Q.05>>>{}".format(int(aa, 16)))


#06
b = [1, 2, 3, 4] 
result = map(lambda x : x*3, b)
print("Q.06>>>{}".format(list(result)))


#07
c = [-8, 2, 7, 5, -3, 5, 0, 1]
print("Q.07>>>{}, {}".format(max(c), min(c)))

low = 0
top = 0
for x in c:
    if c[x] <= low:
        low = c[x]
    if c[x] > top:
        top = c[x]
print("Q.07>>>{}, {}".format(top, low))


#08
d = 17 / 3
print("Q.08>>>{}".format(round(d, 4)))


#9
x = 0
# range_num = int(sys.argv[1]) + 1
# print(range_num)
# for i in range(1, range_num):
#     x += i
# print("Q.10>>>{}".format(x))

print(sys.argv)
for i in range(1, len(sys.argv)):
    x += i
print("Q.10>>>{}".format(x))

#10 
os.chdir('/Users/sohyunpark/IdeaProjects/pythonstudy/wikidocs')
ls = os.system('ls')
print(ls)


#11
output = glob.glob('*.py')
print("Q.11>>>{}".format(output))


#12
tm = time.localtime()
string = time.strftime('%Y-%m-%d %I:%M:%S %p', tm)
print("Q.12>>>{}".format(string))


#13
num = 0
list = []
while len(list) < 6:
    num = int(random.randrange(1, 45))
    if num not in list:
        list.append(num)
list.sort()
print("Q.13>>>{}".format(list))
