# Given a grid of single-digit integer values representing heights of trees in a forest,
# HOW MANY TREES ARE VISIBLE FROM AT LEAST ONE SIDE?
def visible_from_left(row,column,this_tree):
    tallest_trees_on_left = max(forest_array[row][0:column])
    if this_tree > tallest_trees_on_left:
        return True
    return False


def visible_from_right(row,column, this_tree):
    tallest_trees_on_right = max(forest_array[row][column + 1:])
    if this_tree > tallest_trees_on_right:
        return True
    return False


def visible_from_top(row,column, this_tree):
    for r in range(row):
        if forest_array[r][column] >= this_tree:
            return False
    return True


def visible_from_bottom(row,column,this_tree):
    diff = height - row
    for r in range(1,diff):
        if forest_array[row+r][column] >= this_tree:
            return False
    return True


file_path = 'day8_input.txt'  # tree heights
with open(file_path) as input_file:
    forest = input_file.readlines()  # read all input lines
height = len(forest)
width = len(forest[0].strip())
visible_trees = 2*(height+width)-4 # trees at border are all visible. minus 4 to remove 4 corners that are counted twice.

forest_array = [] # create a 2-D array of integer values for trees, with every tree accessible via forest_array[row][column]
for row in range(height):
    new_row = list(forest[row].strip())
    for i in range(width):
        new_row[i] = int(new_row[i])
    forest_array.append(new_row)

# print(forest_array)
for row in range(1,height-1):
    for column in range(1,width-1):
        this_tree = forest_array[row][column] # get current tree's height
        if (visible_from_left(row, column, this_tree) or
            visible_from_right(row, column, this_tree) or
            visible_from_top(row,column,this_tree) or
            visible_from_bottom(row, column, this_tree)):
            visible_trees+=1 # if tree is visible from any direction, increase count
print(visible_trees)