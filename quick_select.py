def quick_select(arr, k):
    return qselect(arr,k-1,0,len(arr)-1)
    
def qselect(arr, k, begin, end):
    if begin >= end: return arr[k]
    pivot = arr[(begin+end) // 2]
    i, j = begin, end
    while i <= j:
        while i <= j and arr[i] < pivot:
            i += 1
        while i <= j and arr[j] > pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    if k <= j:
        return qselect(arr,k,begin,j)
    if k >= i:
        return qselect(arr,k,i,end)
    return arr[k]
'''
print(quick_select([1,2,3,4,5],1))
print(quick_select([1,2,3,4,5],2))
print(quick_select([1,2,3,4,5],5))
#print(quick_select([1,2,3,4,5],6))

print(quick_select([1,0,9,5,3,2],3))
print(quick_select([1,0,9,5,3,2],6))
print(quick_select([1,0,9,5,3,2],1))
'''
