# Given a grid of single-digit integer values representing heights of trees in a forest,
# Viewing distance = how many other trees it can see
# Scenic score = product of viewing distance in every direction
# Note: If a tree is on edge, its viewing distance is 0 that direction.
# WHAT IS THE HIGHEST POSSIBLE SCENIC SCORE FOR ANY TREE?
def vd_left(row,column,this_tree):
    if column==0:
        return 0 #tree is on edge
    vd = 1
    for c in range(column):
        if forest_array[row][column-c-1]<this_tree and (column-c>1):
            #fixed edge cases of adding too many close to end
            vd+=1
        else: #stop looking once we've found a taller tree
            break
    return vd


def vd_right(row,column,this_tree):
    if column==width-1:
        return 0 # tree is on edge
    vd = 1
    for c in range(1,width-column):
        if forest_array[row][column+c]<this_tree and (column+c+1) < width:
            # fixed edge cases of adding too many close to end
            vd+=1
        else: # stop looking once we've found a taller tree
            break
    return vd


def vd_up(row,column,this_tree):
    if row==0:
        return 0 # tree is on edge
    vd=1
    for r in range(row):
        if forest_array[row-r-1][column] < this_tree and (row - r > 1):
            # fixed edge cases of adding too many close to end
            vd += 1
        else:  # stop looking once we've found a taller tree
            break
    return vd

def vd_down(row,column,this_tree):
    if row==height-1:
        return 0 # tree is on edge
    vd=1
    for r in range(1,height-row):
        if forest_array[row+r][column] < this_tree and (row +r + 1) < height:
            # fixed edge cases of adding too many close to end
            vd += 1
        else:  # stop looking once we've found a taller tree
            break
    return vd

def visible_from_bottom(row,column,this_tree):
    diff = height - row
    for r in range(1,diff):
        if forest_array[row+r][column] >= this_tree:
            return False
    return True

def get_scenic_score(row,column,this_tree):
    return vd_left(row,column,this_tree) * vd_right(row,column,this_tree) * vd_up(row,column,this_tree) * vd_down(row,column,this_tree)

file_path = 'day8_input.txt'  # tree heights
with open(file_path) as input_file:
    forest = input_file.readlines()  # read all input lines
height = len(forest)
width = len(forest[0].strip())

forest_array = [] # create a 2-D array of integer values for trees, with every tree accessible via forest_array[row][column]
for row in range(height):
    new_row = list(forest[row].strip())
    for i in range(width):
        new_row[i] = int(new_row[i])
    forest_array.append(new_row)

max_scenic_score = 0
for row in range(height):
    for column in range(width):
        this_tree = forest_array[row][column] # get current tree's height
        ss=get_scenic_score(row, column, this_tree)
        if ss > max_scenic_score:
            max_scenic_score = ss
print(max_scenic_score)
