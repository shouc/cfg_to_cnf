from collections import defaultdict
import copy

def parse():
    cfg = defaultdict(list)
    num_line = int(input())
    for _ in range(num_line):
        inp = input()
        l = inp.split(" ")[0]
        r = inp.split(" ")[1]
        cfg[l].append(r)
    return dict(cfg)


def spit(cfg):
    for i in cfg:
        cfg[i] = set(cfg[i])
    print(sum([len(cfg[x]) for x in cfg]))
    for i in cfg:
        for j in cfg[i]:
            print("%s %s" % (i, j))


def parse_mentor():
    cfg = defaultdict(list)
    num_line = int(input())
    for _ in range(num_line):
        inp = input()
        l, r = inp.split(" -> ")
        cfg[l] = r.split(" | ")
    return dict(cfg)

def eddie_all(cfg):
    for i in cfg:
        cfg[i] = list(set(cfg[i]))


def to_mentor(cfg):
    new_cfg = copy.deepcopy(cfg)
    for i in cfg:
        new_cfg[i] = set(cfg[i])
    result = ""
    for i in cfg:
        result += "%s -> %s\n" % (i, " | ".join(new_cfg[i]))
    return result


