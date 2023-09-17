
print('gugudan1=================')

for i in range(2,10):
    for j in range(1, 10):
        print(f'{i}*{j}={i*j}')

print('gugudan2================')

l = [ f'{i}*{j}={i*j}' for i in range(2, 10) for j in range(1, 10) ]
print(*l, sep='\n')
