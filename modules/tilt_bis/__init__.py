from common import reverse


def tilt(grid: list, direction: str) -> list:
    grid = reverse(grid) if direction == 'S' else grid
    for i, line in enumerate(grid):
        # tilt the reflector in North/South direction
        for j, col in enumerate(line):
            if col == '.':
                for k, next_line in enumerate(grid[i+1:], start=i+1):
                    if next_line[j] == 'O':
                        grid[i][j] = 'O'
                        grid[k][j] = '.'
                        break
                    elif next_line[j] == '#':
                        break
        # tilt the reflector in West/East direction
        line = ''.join(reverse(line) if direction == 'S' else line)
        chuncks = line.split('#')
        temp = list()
        for chunck in chuncks:
            l_chunck = len(chunck)
            nb_O = chunck.count('O')
            temp.append(f'{"O"*nb_O}{"."*(l_chunck-nb_O)}')
        grid[i] = list(reverse('#'.join(temp)) if direction ==
                       'S' else '#'.join(temp))
    return reverse(grid) if direction == 'S' else grid


def load_beam(grid: list) -> int:
    return sum([line.count('O') * i for i, line in enumerate(reverse(grid), 1)])
