import re


def arrangements(springs: str, dam_springs: list, nb_dam: int, count: int = 0, act_springs: str = ''):
    act_dam = act_springs.count('#')
    len_act = len(act_springs)

    if act_dam > nb_dam:
        return count

    if len_act < len(springs):
        while springs[len_act] != '?':
            act_springs += springs[len_act]
            len_act += 1
            if act_dam > nb_dam:
                return count
            if len_act == len(springs):
                break
    if act_dam > nb_dam:
        return count
    if len_act < len(springs):
        count = arrangements(springs, dam_springs, nb_dam,
                             count, act_springs + '#')
        count = arrangements(springs, dam_springs, nb_dam,
                             count, act_springs + '.')
        return count
    else:
        pattern = r'(#+)'
        matches = re.findall(pattern, act_springs)
        if len(matches) == len(dam_springs):
            for i, match in enumerate(matches):
                if len(match) != int(dam_springs[i]):
                    return count
            return count + 1
        else:
            return count
