a = int(input('첫 번째 수를 입력하세요 : '))
b = int(input('두 번째 수를 입력하세요 : '))
g = input('원하는 연산은?\n+,-,*,/ 중 하나를 선택하세요 : ')

if g=='+':
    print("%d + %d = %d"%(a,b,a+b))
elif g=='-':
    print("%d - %d = %d"%(a,b,a-b))
elif g=='*':
    print("%d * %d = %d"%(a,b,a*b))
elif g=='/':
    print("%d / %d = %.2f"%(a,b,a/b))
else:
    print('선택오류!')