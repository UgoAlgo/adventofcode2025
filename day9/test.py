from shapely.geometry import Polygon, Point

coords = [(7,1),(11,1),(11,7),(9,7),(9,5),(2,5),(2,3),(7,3)]
poly = Polygon(coords)

# créer la grille raster
max_x = max(x for x,_ in coords)
max_y = max(y for _,y in coords)
grid = [[0]*(max_x+1) for _ in range(max_y+1)]

for y in range(max_y+1):
    for x in range(max_x+1):
        if poly.contains(Point(x, y)) or poly.touches(Point(x, y)):
            grid[y][x] = 1

def largestRectangle(grid):
    height = len(grid)
    width = len(grid[0])
    max_area = 0
    heights = [0]*width

    for row in grid:
        for i in range(width):
            heights[i] = heights[i]+1 if row[i]==1 else 0

        stack = []
        for i in range(width+1):
            cur_height = heights[i] if i<width else 0
            while stack and cur_height < heights[stack[-1]]:
                h = heights[stack.pop()]
                w = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, h*w)
            stack.append(i)
    return max_area

print(largestRectangle(grid))

