name = input('이른을 입력하세요 : ')
workT = int(input('일주일간 일한 시간을 입력하세요 : '))
if workT<=40:
    overT = 0
    m = workT*12000
else :
    overT = workT-40
    m = overT*12000*1.5+40*12000
print('-이름 : %s\n-일주일간 일한 시간 : %d시간\n-오버타임 : %d시간\n-주급 : %d원'%(name, workT, overT, m))


