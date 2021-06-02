# 04장 연습문제
# https://wikidocs.net/42528

# 01
is_odd = lambda a, b: True if a % 2 == 0 else False
print('01 --> {0}'.format(is_odd(1, 2)))

#02
#print('02 --> {0}'.format(is_odd(1, 2)))


#03 
# a = 1
# b = 2
# c = input("입력값 1")
# d = input("입력값 2")

# print(a + b)
# print(int(c) + int(d))

#04
print("you","need","python")


#05, 06
f1 = open("test.txt", 'w')
f1.write("Life is too short\nyou need java")
f1.close();

f2 = open("test.txt", 'r')
before_body = f2.read()
print("before:::: {0}".format(before_body))
after_body = before_body.replace("java", "python")
print("after:::: {0}".format(after_body))
f2.close()

f3 = open("test.txt", 'w')
f3.write(after_body)
f3.close()
