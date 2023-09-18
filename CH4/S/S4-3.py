
def chk_prime(a):
    chk = 0
    for i in range(2, a):
        if a%i==0: 
            chk=1
            break
    #else: print('prime')
    if chk==0: return 'prime'
    else: return 'not prime'

for i in range(3, 11):
    r = chk_prime(i)
    print(r)
  