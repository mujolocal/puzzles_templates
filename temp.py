def sort_by(lists):
    lista,listb = lists.split("|")
    lists = list(zip(lista.split(","),listb.split(",")))
    sorted_lists = merge_sort(lists)
    return ",".join([word[1] for word in sorted_lists])

def merge_sort(lists):
    if len(lists)==1:
        return lists
    if len(lists)>1:
        left,right = split(lists)
        
        return sort(merge_sort(left), merge_sort(right) )

def sort(left, right):
    return_list = []

    while len(left)>0 and len(right)>0:
        return_list.append(left.pop(0)if left[0][0]<right[0][0] else right.pop(0))
    return_list+= left if len(left)>0 else right    
    return return_list

def split(lists):
    return lists[:len(lists)//2],lists[len(lists)//2:]
    
if __name__ == "__main__":
    sort_by("c,a,e,b,d|has,this,ordered,list,been")