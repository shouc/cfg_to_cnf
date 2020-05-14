import copy
from helper import parse, spit, to_mentor, eddie_all
import time
LAMBDA_REPR = "_"

arr = {
    "S": ["A"],
    "A": ["BAB", "ABA", "B", "_"],
    "B": ["0", "_"],
}


def find_last_epsilon_keys(cfg):
    result = []
    for k in cfg:
        if k == "S":
            continue
        if LAMBDA_REPR in cfg[k]:
            result.append(k)
            break
    if not result:
        return cfg, None
    v = result[-1]
    del cfg[v][cfg[v].index(LAMBDA_REPR)]
    return cfg, v


def compensate(v, last_index, key):
    result = [x for x in v]
    try:
        current_index = v[0][last_index + 1:].index(key) + last_index + 1
    except ValueError as e:
        final_result = []
        for i in set(result):
            final_result.append(i.replace("@", ""))
        return final_result
    for i in v:
        result.append(i[:current_index] + "@" + i[current_index + 1:])
    return compensate(result, current_index, key)


def compensate_removal(cfg, key, already_lambdad):
    new_cfg = copy.deepcopy(cfg)
    for k in cfg:
        for j in cfg[k]:
            if key in j:
                new_cfg[k] += compensate([j], -1, key)
                remove_empty(new_cfg[k], key, already_lambdad)
    return new_cfg


def remove_empty(a, key, already_lambdad):
    for k, i in enumerate(a):
        if i == "":
            if key in already_lambdad:
                del a[k]
            else:
                a[k] = "_"
                already_lambdad.append(key)
            return


def remove_epsilon(cfg):
    new_cfg = copy.deepcopy(cfg)
    already_lambdad = []
    while True:
        new_cfg, nullable_key = find_last_epsilon_keys(new_cfg)
        if not nullable_key:
            return new_cfg
        new_cfg = compensate_removal(new_cfg, nullable_key, already_lambdad)
        eddie_all(new_cfg)


# print(0)
# print(to_mentor(remove_epsilon(arr)))

# with open("a.cfg", "w") as fp:
#     fp.write(to_mentor(arr))
# with open("b.cfg", "w") as fp:
#     fp.write()
#
# import os
# os.system("./mentor a.cfg generate 100 > a.txt")
# os.system("./mentor b.cfg generate 100 > b.txt")
if __name__ == "__main__":
    spit(remove_epsilon(parse()))
