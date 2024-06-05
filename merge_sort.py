def merge(esq, dir):
    A = []
    i = j = 0
    while i<len(esq) and j<len(dir):
        if esq[i] <= dir[j]:
            A.append(esq[i])
            i += 1
        else:
            A.append(dir[j])
            j += 1
    A.extend(esq[i:])
    A.extend(dir[j:])
    return A

def merge_sort(A):
    if len(A) <= 1:
        return A
    
    mid = len(A) //2
    esq = merge_sort(A[:mid])
    dir = merge_sort(A[mid:])
    return merge(esq, dir)