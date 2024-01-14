from typing import List, Tuple


def out_of_bound(p: int, v: int, bounds: Tuple[int]) -> bool:
    return p <= bounds[0] and v < 0 or p >= bounds[1] and v > 0


def in_bound(p: float, bounds: Tuple[int]) -> bool:
    return bounds[0] <= p <= bounds[1]


def time_cross(pi: int, vi: int, px: float) -> float:
    return (px - pi) / vi


def path_cross(stoneA: Tuple[float], stoneB: Tuple[float], bounds: Tuple[int]) -> bool:
    if stoneA[0] == stoneB[0]:
        # path are parallels
        return False
    x = (stoneB[1] - stoneA[1]) / (stoneA[0] - stoneB[0])
    y = stoneA[0]*x + stoneA[1]

    # print(x, y)
    if all(in_bound(p, bounds) for p in (x, y)):
        tA = time_cross(stoneA[2], stoneA[3], x)
        tB = time_cross(stoneB[2], stoneB[3], x)

        if tA < 0 or tB < 0:
            return False
        else:
            return True
    else:
        return False


def lin_eq(stoneA: Tuple[int], stoneB: Tuple[int], coef_mat: list, const_mat: list) -> Tuple[list]:
    xa, ya, za, vxa, vya, vza = stoneA
    xb, yb, zb, vxb, vyb, vzb = stoneB
    # x vs y
    coef_mat.append([vyb - vya, ya - yb, vxa - vxb, xb - xa, 0, 0])
    const_mat.append(xb*vyb - xa*vya + ya*vxa - yb*vxb)
    # x vs z
    coef_mat.append([vzb - vza, za - zb, 0, 0, vxa - vxb, xb - xa])
    const_mat.append(xb*vzb - xa*vza + za*vxa - zb*vxb)
    # z vs y
    coef_mat.append([0, 0, vza - vzb, zb - za, vyb - vya, ya - yb])
    const_mat.append(zb*vyb - za*vya + ya*vza - yb*vzb)

    return coef_mat, const_mat
