# 03장 연습문제
# https://wikidocs.net/42527

print("---Q.1---")
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt") # 참
elif "need" in a: print("need") # 참
else: print("none")

print("결과는: shirt")
print("--------\n")


print("---Q.2---")
i=0
total=0
while(i<1001):
    if i%3 == 0:
        total += i
    i += 1
print(total)
print("--------\n")


print("---Q.3---")
z=1
while(z<6):
    for x in range(0, z):
        print("*", end = "")
    print(" ")
    z += 1

# 이렇게도 가능
# i = 0
# while True:
#     i += 1 # while문 수행 시 1씩 증가
#     if i > 5: break     # i 값이 5보다 크면 while문을 벗어난다.
#     print ('*' * i)     # i 값 개수만큼 *를 출력한다.
print("--------\n")


print("---Q.4---")
# for t in range(1, 100):
#     print(t)
#     print("\t")
print("--------\n")



print("---Q.5---")
score_lists = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
total = 0
for score in score_lists:
    total += score

print(total / (len(score_lists)))
print("--------\n")



print("---Q.6---")
# 리스트 내포(List comprehension)
numbers = [1, 2, 3, 4, 5]
result = []
for n in numbers:
    if n % 2 == 1:
        result.append(n*2)

print(result)
print([n * 2 for n in numbers if n % 2 == 1])
print("--------\n")
