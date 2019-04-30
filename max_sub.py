def max_sequence(arr, count = 0):
    """
    The maximum sum subarray problem consists in 
    finding the maximum sum of a contiguous 
    subsequence in an array or list of integers
    >>> max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    6
    
    solution is a follow behind solution: 
    max(sum([-2,1]),sum([1,-3]),sum([-3,4]),sum(4,-1))
    this is 2 but its done for 1 through max length
    """
    # if num = len(arr):
    #     return sum(arr)
    # else:
    #     max_sequence(arr, count+1)
    
    
    if len(arr) == 0:
        return 0
    max = 0
    for i in range(len(arr)):
        for x in range(len(arr)-i):
            a = arr[x:x+i+1]
            if sum(a)> max:
                max=sum(a)
    return max