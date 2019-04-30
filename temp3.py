import json
def merge_hashes(hashes):
    list0, list1 = hashes.split("|")
    list0 = json.loads(list0)
    list1 = json.loads(list1)
    keys = list(list1.keys())+list(list0.keys())
    print(keys)
    return_hash = {}
    for key in keys:
        if not isinstance(list1[key], int)and  key in list1.keys() and key in list0.keys() and "]" in list1[key]:
            return_hash[key] = list0[key]+list1[key]
        elif not isinstance(list1[key], int)and key in list1.keys() and key in list0.keys() and "}" in list1[key]:
            return_hash[key] = merge_hashes("{}|{}".format(list0[key],list1[key]))    
        elif key in list1.keys() and key in list0.keys():
            return_hash[key]= list1[key]
        elif key in list1.keys() and (key not in list0.keys()):
            return_hash[key] = list1[key] 
        else:
            return_hash[key]= list0[key] 
    return str(return_hash)
            
    


if __name__ == "__main__":
    print(merge_hashes('{"foo": "bar"} | {"foo": "baz", "fibonacci": [1, 1, 2, 3, 5]}'))