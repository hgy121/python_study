p = int(input('필기시험 점수는?'))
s = int(input('실기시험 점수는?'))
if p>=80 and s>=80:
    result = '합격'
else:
    result = '불합격'
print('-필기시험 점수 : %d'%p)
print('-실기시험 점수 : %d'%s)
print('-판정 : %s'%result)