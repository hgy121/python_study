def pl(a,b):
    c = a+b
    global e
    e = '+'
    return c
def ma(a,b):
    c = a-b
    global e
    e ='-'
    return c
def gop(a,b):
    c = a*b
    global e
    e ='*'
    return c
def na(a,b):
    c = a/b
    global e
    e ='/'
    return c



print('-선택 옵션\n1.더하기\n2.빼기\n3.곱하기\n4.나누기')
calcuate = input('원하는 연산을 선택하세요(1/2/3/4) : ')
a = int(input('첫 번째 숫자를 입력하세요 : '))
b = int(input('두 번째 숫자를 입력하세요 : '))

if calcuate == '1':
    d = pl(a,b)
elif calcuate == '2':
    d = ma(a,b)
elif calcuate == '3':
    d = gop(a,b)
else:
    d = na(a,b)



print('%d %s %d = %d'%(a,e,b,d))