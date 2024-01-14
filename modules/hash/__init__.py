
def hash(string: str) -> int:
    values = [ord(char) for char in string]
    return sum([char*17**(len(string)-i)
                for i, char in enumerate(values)]) % 256
