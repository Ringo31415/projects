from time import time 

l = [45, 23, 12, 34, 89, 78, 53, 48, 20, 9]

def merge(l1,l2):
    i,j = 0,0
    l_result=[]
    while i < len(l1) and j < len(l2):
        if l1[i] < l2[j]:
            l_result.append(l1[i])
            i += 1
        else:
            l_result.append(l2[j])
            j += 1
    for k in range(i,len(l1)):
        l_result.append(l1[k])
    for  k in range(j,len(l2)):
        l_result.append(l2[k])
    return l_result

def merge_sort(l):
    length = len(l)
    if length == 1:
        return l
    else:
        mid = length//2
        l1 = merge_sort(l[:mid])
        l2 = merge_sort(l[mid:])
        return merge(l1,l2)

print(merge_sort(l))