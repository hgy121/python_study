a = input('등급을 입력해 주세요(A+,A,B+,...,F) : ')
if a=='A+':
    g = 4.5
elif a=='A':
    g = 4.0
elif a=='B+':
    g = 3.5
elif a=='B':
    g = 3.0
elif a=='C+':
    g = 2.5
elif a=='C':
    g = 2.0
elif a=='D+':
    g = 1.5
elif a=='D':
    g = 1.0
else:
    g = 0

print('등급:%s, 평점:%d'%(a,g))

