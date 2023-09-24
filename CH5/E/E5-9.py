numbers = [7,9,15,18,30,-3,7,12,-16,-12]
l = []
s = 0
print('짝수 번째 요소 :',end=' ')
for i in range(0,len(numbers)):
    if i%2==1:
        print(numbers[i],end=' ')
        l.append(numbers[i])
    s += numbers[i]

s = sum(l)

print('\n합계 : %d'%s)