n = int(input('n값을 입력해 주세요 : '))
print("2~%d까지의 정수 중 소수 : "%n,end='')

for i in range(2,n):
    a =0
    for j in range(2,i):
        if i%j == 0:
            a = 1
            break
    if a == 0:
        print(i,end=' ')