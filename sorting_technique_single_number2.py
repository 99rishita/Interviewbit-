#a = [2,3,4,5,5,2,5,3,3,2]
#a = [3,7,3,3]
a = [5,2,4,4,5,5,4]
n = len(a)
a.sort()
print(a)
i = 1
while i < len(a):
    if a[i]!=a[i-1]:
        print(a[i-1])
        break
    elif a[n-1]!=a[n-2]:
        print(a[n-1])
        break
    elif a[i] == a[i-1]:
        i += 3