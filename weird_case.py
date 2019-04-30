def to_weird_case(string):
    l_string = string.split(" ")
    ret_list = []
    for item in l_string:
        ret_list.append(
        "".join([item[i].upper() if i%2==0 else item[i].lower() for i in range(len(item)) ] )
        )
    return ret_list

    
if __name__ == "__main__":
    print(to_weird_case('This is a test'))