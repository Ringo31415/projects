L=[1,23,4,4,42,78]

def Bsearch(L,target,left,right):
    if left > right:
        return -1
    
    mid = (left+right)//2

    if L[mid] == target:
        return mid
    elif L[mid] > target:
        return Bsearch(L,target,left,mid-1)
    elif L[mid] < target:
        return Bsearch(L,target,mid+1,right)

print(Bsearch(L,78,0,len(L)-1))
