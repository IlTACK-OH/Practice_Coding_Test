def solution(array):
    dict_arr = {}
    for i in array:
        if i in dict_arr:
            dict_arr[i] += 1
        else:
            dict_arr[i] = 0
    
    max_val_list = [k for k,v in dict_arr.items() if max(dict_arr.values()) == v]
    
    if len(max_val_list) > 1:
        return -1
    return max_val_list[0]