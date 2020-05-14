
def is_multiple(k):
    cter = 0
    index = 0
    if len(k) == 0:
        return False
    while True:
        if index >= len(k):
            break
        if not k[index].isalpha() or k[index].upper() != k[index]:
            cter += 1
            index += 1
            continue
        current_i = index + 1
        index += 1
        li = 0
        for i in k[current_i:]:
            li += 1
            if li == 6:
                break
            if i.isalpha():
                cter += 1
                break
            index += 1
    return cter > 1

def split(k):
    return k[:1], k[1:]

def split2(k):
    m = 0
    for c, i in enumerate(k):
        if i.upper() != i:
            m = c
            break
    return k[m], k[m+1:] if k[m+1:] != "" else k[:m], k[m+1:] != "" # true if at left

def is_violate(v):
    return v.upper() != v and v != "_" and len(v) > 1

def get_all_violation(cfg):
    result = []
    for i in cfg:
        for j in cfg[i]:
            if is_violate(j):
                result.append((i,j))
    return result

import copy


def to_cnf(cfg):
    current_index = 99999
    while True:
        cter = 0
        orig_cfg = copy.deepcopy(cfg)
        for i in orig_cfg:
            for k, j in enumerate(cfg[i]):
                if is_multiple(j):
                    cter += 1
                    l, r = split(j)
                    newk = "U%s" % current_index
                    current_index -= 1
                    cfg[newk] = [r]
                    cfg[i][k] = "%s%s" % (l, newk)
        if cter == 0:
            break
    v = get_all_violation(cfg)
    for k in v:
        key, right = k
        char, var, isleft = split2(right)
        newk = "U%s" % current_index
        current_index -= 1
        cfg[newk] = [char]
        if isleft:
            cfg[key][cfg[key].index(right)] = "%s%s" % (newk, var)
        else:
            cfg[key][cfg[key].index(right)] = "%s%s" % (var, newk)

    return cfg


from task2 import *
if __name__ == "__main__":
    spit(to_cnf(remove_unit(remove_epsilon(parse()))))
    # print(is_multiple("S1111111"))
