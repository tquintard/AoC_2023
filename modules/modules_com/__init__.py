from collections import defaultdict
from re import findall as fa


def last_flipflops(modules: dict) -> tuple:
    last_con = list(modules['rx'].inputs.keys())[0]
    return {module for module in modules[last_con.name].inputs}


class Modules:
    all_modules, queue, pulses = defaultdict(list), list(), [0, 0]

    def __init__(self, type: str, name: str, dest: list()) -> None:
        self.name, self.type = name, type
        self.inputs, self.outputs = dict(), list()
        self.status = 0
        self.all_modules[name] = self
        self.add_outputs(dest)

    def add_outputs(self, outputs: list()):
        for output in outputs:
            if output not in self.all_modules.keys():
                Modules(None, output, [])
            self.all_modules[output].inputs[self] = 0
            self.outputs.append(self.all_modules[output])

    def __repr__(self) -> str:
        return f'{self.name}'

    @classmethod
    def process_sig(cls, src: 'Modules', dest: 'Modules', sig: int) -> None:
        cls.pulses[sig] += 1
        if dest.type == '%' and sig == 0:
            sig = dest.status = 1 - dest.status
        elif dest.type == '&':
            dest.inputs[src] = sig
            sig = 0 if all(value == 1 for value in dest.inputs.values()) else 1
        else:
            return None
        cls.queue += [(dest, output, sig) for output in dest.outputs]

    @classmethod
    def print_sig(cls, src: 'Modules', dest: 'Modules', sig: int) -> None:
        print(f"{src.name} -{'low' if sig == 0 else 'high'}-> {dest.name}")

    @classmethod
    def create_modules(cls, inputs: list) -> None:
        for line in inputs:
            type, name, *outputs = line[0], *fa(r'(\w+)', line)
            if name not in cls.all_modules.keys():
                cls(type, name, outputs)
            else:
                module = cls.all_modules[name]
                module.type = type
                module.add_outputs(outputs)
