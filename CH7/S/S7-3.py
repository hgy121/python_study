def square():
    n = int(input('n의 값을 입력하세요 : '))
    for i in range(1,n+1):
        a = i*i
        l.append(a)
    print(l)

l = []
square()