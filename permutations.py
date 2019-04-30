def perm(lst):
    """
    Takes up a lot of space
    """
    if len(lst)==0:
        return []
    elif len(lst)==1:
        return [lst]
    else:
        l = []
        for i in range(len(lst)):
            x = lst[i]
            x_sub = lst[:i]+lst[i+1:]
            for item in perm(x_sub):
                l.append([x]+item)
        return l

def perm2(lst):
    """
    Takes up a lot less space
    """
    if len(lst)==0:
        yield []
    elif len(lst)==1:
        yield [lst]
    else:
        for i in range(len(lst)):
            x = lst[i]
            x_sub = lst[:i]+lst[i+1:]
            for item in perm(x_sub):
                yield [x]+item

                
                
                
if __name__ == "__main__":
    print(perm([3,4,4,]))
    for p in perm2([1,2,3,4,5,5,6 ]):
        print(p)