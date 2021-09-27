a = [5566,23,5,456,556,845,123]

swap = True

while swap:
    swap = False
    for j in range(len(a)-1):
        if a[j] > a[j+1]:
            swap =True
            a[j], a[j+1] = a[j+1],a[j]

print(a)
