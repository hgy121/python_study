def multiply(l,x):
    i = 0
    while i < len(l):
        l[i] *= x
        i +=1

numbers = [10,20,30,40,50]

multiply(numbers,20)
print(numbers)