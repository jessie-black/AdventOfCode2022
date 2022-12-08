#Puzzle input = height of each tree, each tree = single digit integer 0-9 (0 is a short tree, not an empty space)
# visible: if all other trees between it and an edge are shorter
# Only consider interior 9



# HOW MANY TREES ARE VISIBLE FROM OUTSIDE?

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
    for i in range(row):
        if forest_array[i][column] >= this_tree:
            return False
    return True

def visible_from_bottom(row,column, this_tree):
    for i in range(height,row+1):
        if forest_array[i][column] >= this_tree:
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

#print(forest_array)
for row in range(1,height-1):
    for column in range(1,width-1):
        this_tree = forest_array[row][column] # get current tree's height


        if (visible_from_left(row, column, this_tree) or
            visible_from_right(row, column, this_tree) or
            visible_from_top(row,column,this_tree) or
            visible_from_bottom(row, column, this_tree)):
            visible_trees+=1
print(visible_trees)
            #print("I can see tree [",row,"][",column,"] of height",this_tree)
    #if visible_from_left(1,column):
    #    print("I can see the tree in row","1",", column",column,"of height",forest_array[1][column])
    #if visible_from_right(1,column):
    #    print("I can see the tree in row","1",", column",column,"of height",forest_array[1][column])

#inner_forest=[]
#for row in range(height-2): #skipping top and bottom rows
#    row_of_trees = list(forest[row+1].strip()[1:-1]) # list of trees, each element is a single tree, excluding line break and excluding first and last trees
#    inner_forest.append(row_of_trees)


#for column in range(width-2):
#        if visible_from_left(row+1,column+1)
#    print(row_of_trees)
    #for column in range(width-2):#skip outer columns
    #    tree = (int(forest[current_row][column+1])
    #    if visible_from_left(current_row, column + 1, tree):
     #       print("I can see the tree in row",current_row,", column",column+1,"of height",tree)
        #if visible_from_right(current_row,column+1,tree):
            #print("I can see the tree in row",row+1,", column",column+1,"of height",tree)
