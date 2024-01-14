from re import findall as fa


class Bricks:
    landed_blocks, z_landed, reaction = dict(), {0}, 0

    def __init__(self, vector: str) -> None:
        self.vector = vector
        xa, ya, za, xb, yb, zb = list(map(int, fa(r'(\d+)', vector)))
        self.z_min = za
        self.landed, self.is_vert = False, za != zb
        self.below, self.above = set(), set()
        self.blocks = [(x, y, z) for z in range(za, zb + 1)
                       for y in range(ya, yb + 1) for x in range(xa, xb + 1)]

    def __repr__(self) -> str:
        return str(self.id)

    def collid(self, x: int, y: int, z: int) -> bool:
        if (x, y, z) in self.landed_blocks:
            brick_below = self.landed_blocks[(x, y, z)]
            self.below.add(brick_below)
            brick_below.above.add(self)
            self.landed = True
            return True
        return False

    def chain(self, visited: set):
        for brick in self.above:
            if brick not in visited and set(brick.below).issubset(visited):
                visited.add(brick)
                Bricks.reaction += 1
                brick.chain(visited)

    @classmethod
    def bricks_fall(cls) -> None:
        cls.bricks.sort(key=lambda x: x.z_min)
        for brick in cls.bricks:
            for z in sorted(cls.z_landed, reverse=True):
                if z > 0:
                    if brick.is_vert:
                        dz = z - brick.z_min + 1
                        if brick.collid(*brick.blocks[0][:2], z):
                            for block in brick.blocks:
                                cls.landed_blocks[(
                                    *block[:2], block[2] + dz)] = brick
                            cls.z_landed.add(block[2] + dz)
                            break
                    else:
                        for block in brick.blocks:
                            _ = brick.collid(*block[:2], z)

                if z == 0 or brick.landed:
                    cls.z_landed.add(z + 1)
                    for block in brick.blocks:
                        if brick.is_vert:
                            dz = z - brick.z_min + 1
                            cls.landed_blocks[(
                                *block[:2], block[2] + dz)] = brick
                        else:
                            cls.landed_blocks[(*block[:2], z + 1)] = brick
                    break

    @classmethod
    def desintegrate(cls) -> int:
        cls.mandatory_bricks = set(brick_ for brick in cls.bricks
                                   for brick_ in brick.below if len(brick.below) == 1)
        return len(cls.bricks) - len(cls.mandatory_bricks)

    @classmethod
    def chain_reaction(cls) -> int:
        for brick in cls.mandatory_bricks:
            brick.chain({brick})
        return cls.reaction
