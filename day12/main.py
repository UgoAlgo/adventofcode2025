def parse_piece(lines, i, pieces):
    j = i + 1
    while j < len_lines and lines[j][0] != "\n":
        j += 1
    i += 1
    temp = []
    for li in range(0, j-i):
        for lj in range(3):
            if lines[i + li][lj] == "#":
                temp.append((li, lj))
    if temp != []:
        pieces[len(pieces)] = temp
    return j+1


def parse_regions(line):
    shapes, pieces = line.split(":")
    x,y = shapes.split("x")
    return ((int(x),int(y)), [int(p) for p in pieces.split()])


def remove_piece(x, y, occupied, piece):
    for coords in piece:
        occupied.remove((x + coords[0], y + coords[1]))


def rotate(shape):
    return [(y, -x) for (x,y) in shape]


def normalize(shape):
    minx = min(x for x,y in shape)
    miny = min(y for x,y in shape)
    return sorted([(x-minx, y-miny) for x,y in shape])


def all_rotations(shape):
    rots = set()
    cur = shape
    for _ in range(4):
        cur = rotate(cur)
        rots.add(tuple(normalize(cur)))
        flipped = [(-x,y) for (x,y) in cur]
        rots.add(tuple(normalize(flipped)))
    return [list(r) for r in rots]


def can_be_placed(x, y, size, occupied, piece):
    for coords in piece:
        xx = x + coords[0]
        yy = y + coords[1]
        if xx < 0 or yy < 0 or xx >= size[0] or yy >= size[1]:
            return False
        if (xx, yy) in occupied:
            return False
    return True


def place_piece(x, y, occupied, piece):
    for coords in piece:
        occupied.add((x + coords[0], y + coords[1]))

def expand_pieces_needed(pieces_needed):
    res = []
    for shape_id, count in enumerate(pieces_needed):
        res.extend([shape_id] * count)
    return res


def backtracking(i, to_place, pieces, size, occupied):
    width, height = size

    if i == len(to_place):
        return True

    shape_id = to_place[i]

    for shape in pieces[shape_id]:
        for x in range(width):
            for y in range(height):
                if can_be_placed(x, y, size, occupied, shape):
                    place_piece(x, y, occupied, shape)
                    if backtracking(i+1, to_place, pieces, size, occupied):
                        return True
                    remove_piece(x, y, occupied, shape)

    return False


with open("test", "r") as file:
    lines = file.readlines()

pieces = {}
i = 0
len_lines = len(lines)
line = lines[0]

while i < len_lines and line[1] == ":":
    i = parse_piece(lines, i, pieces)
    line = lines[i]

pieces_list = [pieces[k] for k in sorted(pieces.keys(), key=lambda i: -len(pieces[i]))]

pieces_list = [all_rotations(p) for p in pieces_list]

result = 0

while i < len_lines:
    size, pieces_needed = parse_regions(lines[i])
    to_place = expand_pieces_needed(pieces_needed)
    result += backtracking(0, to_place, pieces_list, size, set())
    i += 1

print(result)
