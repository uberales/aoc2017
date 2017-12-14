# -*- coding: utf-8 -*-

x = 0
y = 0

corners = [[0, 0]]

n_max = 347991
odd_i = 0
odd_square = 0

while odd_square < n_max:
    odd_n = odd_i * 2 + 1
    odd_square = odd_n * odd_n
    
    last_corner = corners[-1]
    square_side = (odd_square - last_corner[0]) / 4
    corners.append([odd_square, square_side])
    
    odd_i += 1

last_corner = corners[-1]
diff = n_max - last_corner[0]
delta_center = last_corner[1] / 2
delta_mid = diff % last_corner[1] - last_corner[1] / 2

delta_total = delta_center + delta_mid

print delta_total

grid = {}

grid_zero = 0

row = {}
row[0] = 1

grid[0] = row

def GetDxDy(grid, x, y):
    def GetMask(grid, x, y):
        mask = []
        for y_i in range(y - 1, y + 2):
            mask_line = []
            for x_i in range(x - 1, x + 2):
                grid_row = grid[y_i] if y_i in grid else {}
                grid_point = grid_row[x_i] if x_i in grid_row else 0
                mask_line.append(grid_point)
            mask.append(mask_line)
        return mask
                
    def CompareMask(mask_a, mask_b):
        for y_i in range(3):
            for x_i in range(3):
                if not(mask_a[y_i][x_i] == mask_b[y_i][x_i]):
                    return False
        return True
    
    mask_1 = GetMask(grid, x, y)
    mask_2 = GetMask(grid, x + 1, y)
    tf =  CompareMask(mask_1, mask_2)
    

GetDxDy(grid, 0, 0)
        
# this solution is incomplete