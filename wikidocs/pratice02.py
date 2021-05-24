# 02장 연습문제
# https://wikidocs.net/42526

# Q01
print("---Q.01---")
korean = 80
english = 75
math = 55
print((korean + english + math) / 3)
print("--------\n")


print("---Q.02---")
# Q02
if float(13 % 2) == 0:
    print("짝수")
else:
    print("홀수")
print("--------\n")


pin = "881120-1068234" # 03, 04
print("---Q.03---")
print(pin[0:6])
print(pin[7:14])
#print(pin[7:])  # 이렇게 해도 됨
print("--------\n")

print("---Q.04---")
if pin[7] == "2":
    print("여자")
else:
    print("남자")
print("--------\n")



print("---Q.05---")
a = "a:b:c:d"
print(a.replace(":", "#"))
print("--------\n")



print("---Q.06---")
list = [1, 3, 5, 4, 2]
list.sort()
list.reverse()
print(list)
print("--------\n")


print("---Q.07---")
str_list = ['Life', 'is', 'too', 'short']
str_data = " ".join(str_list)
print(str_data)
print("--------\n")


print("?---Q.08---")
t1 = (1,2,3) + (4,) # (4,) 같이 한개의 요소를 가질때에 ,을 붙여줘야 함.
print(t1)
print("--------\n")


print("?---Q.09---")
a = dict()
# a['name'] = 'python'
# a[('a',)] = 'python'
#a[[1]] = 'python' # -> {}안에 빈 {}을 넣을 수 없음. 정확히는 딕셔너리 키로 변하는 값을 사용할 수 없음 (문자열 튜프 숫자등은 가능)
# a[250] = 'python'
print(a)
print("--------\n")


print("---Q.10---")
aa = {'A':90, 'B':80, 'C':70}
print(aa.pop('B'))
print("--------\n")


print("?---Q.11---")
# aaaa = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
# aSet = set(aaaa)     # a 리스트를 집합자료형으로 변환
# b = list(aSet)    # 집합자료형을 리스트 자료형으로 다시 변환
# print(b)          # [1,2,3,4,5] 출력
print("--------\n")


print("---Q.12---")
a = b = [1, 2, 3]
a[1] = 4
print(b) # b = [1,2,3] 이고 b[1] 에 4로 치환하여(a[1]=4할당한것이 참조됨) [1, 4, 3] 이 됨
print("--------\n")
