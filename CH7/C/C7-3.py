def member_join(*args):
    result = ''
    for arg in args:
        result += arg+' '
    print('가입회원:',result)

member_join('김정연','안서영')