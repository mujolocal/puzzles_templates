def mergesort(start):
    """
    sort a list of unsorted things
    merge sort is basically a split function; which breaks down the list into smaller list 
    until the list contains either 1 item or 2 items
    ; and a sort function which does a normal job of sorting
    the idea being its easier to sort a semi sorted function that it is to sort a completely unsorted function
    >>> mergesort([2,19,4,7,45,5,7])
    [2, 4, 5, 7, 7, 19, 45]
    """
    if len(start)==1:
        return start
    if len(start) > 1:
        a,b = split(start)
        return sort(mergesort(a), mergesort(b))

def split(a):
    """
    split cuts the list into two pieces and returns both
    >>> split([1,2,3])
    ([1], [2,3])
    """
    return a[:len(a)//2],a[len(a)//2:]
        
def sort(left,right):
    """
    sorts two sorted lists
    >>> sort([1,3,4,7],[3,5,7])
    [1, 3, 3, 4, 5, 7, 7]
    """
    return_list = []
    while  len(left)>0 and  len(right)>0:
        "note to self, while rechecks criteria every time, so left and right and constantly checked"
        return_list.append(left.pop(0) if left[0]< right[0] else right.pop(0))
    return_list+= left if len(left)>0 else right
    return return_list 

if __name__ == "__main__":
    print(mergesort([1,3,4,7,3,5,7]))
        