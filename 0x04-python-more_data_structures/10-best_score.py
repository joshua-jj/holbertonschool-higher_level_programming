#!/usr/bin/python3
def best_score(my_dict):
    if my_dict and len(my_dict):
        max = list(my_dict.values())[0]
        for key in my_dict:
            if my_dict[key] > max:
                max = my_dict[key]
        return max
    return None
