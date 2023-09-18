

# grade='FFFFFFDCBAA'
# print(grade[85//10])

keep = "y"
while True:
    a = int(input('성적을 입력하세요 : '))
    if a<0 or a>100: 
        print('입력 오류 재입력')
        continue
    if a>=90:
        grade = "수"
    elif a>=80:
        grade = "우"
    elif a>=70:
        grade = "미"
    elif a>=60:
        grade = "양"
    else:
        grade = "가"
    print('등급:', grade)
    keep = input('계속하시겠습니까?(중단:q, 계속:y)')
    if keep=='q': break





