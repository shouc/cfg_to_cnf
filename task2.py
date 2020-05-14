from helper import parse, spit, to_mentor, eddie_all
LAMBDA_REPR = "_"

arr = {
    "S": ["A"],
    "A": ["BAB", "ABA", "B", "_"],
    "B": ["0", "_"],
}
from task1 import remove_epsilon

def is_unit_var(k, cfg):
    k = k.replace("_", "")
    if len(k) == 0:
        return False
    if k[0].upper() != k[0]:
        return False
    for i in k[1:]:
        if i.isalpha():
            return False
    return True


def find_last_unit_prod(cfg):
    result = []
    for i in cfg:
        current_k = cfg[i]
        for j in current_k:
            if is_unit_var(j, cfg):
                result.append((i, j))
    if not result:
        return None, None
    return result[0]


def get_all_reachable(cfg, key):
    return cfg[key]


def add_rules(cfg, key, reachable):
    cfg[key] += reachable
    cfg[key] = list(set(cfg[key]))


def remove_rule(cfg, l, r):
    del cfg[l][cfg[l].index(r)]


def remove_unit(cfg):
    unit_tank = []
    while True:
        l, r = find_last_unit_prod(cfg)
        if not l:
            return cfg
        if (l,r) in unit_tank:
            remove_rule(cfg, l, r)
            continue
        else:
            unit_tank.append((l, r))
        try:
            reachable = get_all_reachable(cfg, r.replace(LAMBDA_REPR, ""))
            add_rules(cfg, l, reachable)
        except:
            pass
        remove_rule(cfg, l, r)
        eddie_all(cfg)
        import time
        # time.sleep(0.5)
        # print(l,r,cfg)


if __name__ == "__main__":
    spit(remove_unit(remove_epsilon(parse())))
