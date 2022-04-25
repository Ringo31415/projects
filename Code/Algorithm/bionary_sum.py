l = [1,2,3]

def bionary_sum(l):
    length = len(l)
    if length == 1:
        return l[0]
    else:
        mid = length // 2 
        return bionary_sum(l[:mid]) + bionary_sum(l[mid:])


print(bionary_sum(l))