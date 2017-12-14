#!/usr/bin/python3
def best_score(my_dict):
    highest = None
    scorer = None
    if my_dict:
        for k, v in my_dict.items():
            if highest is None or v > highest:
                highest = v
                scorer = k
    return scorer
