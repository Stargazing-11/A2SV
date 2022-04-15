def countSwaps(a):
    count = 0
    for i in range(len(a)): 
        for j in range (len(a)-1):
            if (a[j] > a[j + 1]):
                swap(j, j +1,a)
                count +=1
            elif (a[j]<a[j+1]):
                continue
    print("Array is sorted in "+ str(count) +" swaps.")
    print("First Element: "+str(a[0]))
    print("Last Element: " + str(a[len(a)-1]))
    return
            
def swap(c,d,a):
    c,d = d,c
    a[c], a[d] = a[d], a[c]
    return a

