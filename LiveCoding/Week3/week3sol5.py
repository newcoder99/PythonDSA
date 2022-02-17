def quicksort(L,l,r):
    if (r-l) <= 1:
        return L
    (pivot,lower,upper) = (L[l][1],l+1,l+1)
    for i in range(l+1,r):
        if L[i][1]>pivot:
            upper=upper+1
        else:
            L[i],L[lower]=L[lower],L[i]
            (lower,upper)=(lower+1,upper+1)
    L[l],L[lower-1]=L[lower-1],L[l]
    lower=lower-1
    quicksort(L,l,lower)
    quicksort(L,lower+1,upper)
def Arrange(L):
    l = 0
    r = len(L)
    if (r-l) <= 1:
        return L
    (lower,upper) = (l+1,l+1)
    pivot = 'F'
    for i in range(l+1,r):
        if L[i][2]>pivot:
            upper=upper+1
        else:
            L[i],L[lower]=L[lower],L[i]
            (lower,upper)=(lower+1,upper+1)
    L[l],L[lower-1]=L[lower-1],L[l]
    lower=lower-1
    quicksort(L,l,lower)
    quicksort(L,lower,upper)
L = eval(input())
Arrange(L)
print(L)