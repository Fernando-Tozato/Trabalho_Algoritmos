def merge(A:list, p:int, q:int, r:int):
    L = A[p:q+1] + [float('inf')]
    R = A[q+1:r+1] + [float('inf')]
    i, j = 0, 0
    
    for k in range(p,r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

def merge_sort(A:list, p:int, r:int):
    if p < r:
        q = (p + r)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)
        return A