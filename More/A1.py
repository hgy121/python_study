N,P = map(int,input().split())
if P%2==1:
    l = [P+1, N-P, N-P+1]
else:
    l = [P-1, N-P+1, N-P+2]

print(*sorted(l))