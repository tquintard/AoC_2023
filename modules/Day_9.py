from typing import List


def main(inputs: List[str]) -> List[str]:
    histories = [list(map(int, line.split())) for line in inputs]
    sol = [0, 0]
    for history in histories:
        last_digits = [history[-1]]
        first_digits = [history[0]]
        diff = history
        while len(set(diff)) != 1:
            nb_digits = len(diff)
            diff = [diff[i + 1] - diff[i] for i in range(nb_digits - 1)]
            last_digits.append(diff[-1])
            first_digits.append(diff[0])
        sol[0] += sum(last_digits)
        for i, digit in enumerate(first_digits[-2::-1]):
            first_digits[-2 - i] = digit - first_digits[-1 - i]
        sol[1] += first_digits[0]
    return sol
