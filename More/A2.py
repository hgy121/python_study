l1 = sorted([float(i) for i in input().split()])
l2 = [[abs(3.5-a),a] for a in l1]

sol1 = min(l2)[1]
sol2 = max(l2, key=lambda x: (x[0], -x[1]))[1]
print(f'{sol1:f} {sol2:f}')