#
#
#
#
#

# Create a function that moves top of one stack to top of another

# I only need to pop final items off of stacks in order.
stacks={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
stack1 = stack2 = stack3 = stack4 = stack5 = stack6 = stack7 = stack8 = stack9 = []
file_path = 'day5_input.txt' # initial stack setup and instructions
with open(file_path) as input_file:
    original_stacks = input_file.readlines()
for i in range(8): # traverse stacks from bottom to top line by line
    # stacks[1].append(original_stacks[7-i][1])
    for j in range(9):
        if original_stacks[7-i][(j*4)+1]!=" ":
            stacks[j+1].append(original_stacks[7-i][(j*4)+1])
# at this point i have all the stacks
for i in range(9):
    print(stacks[i+1])
# 1 = [1]
# 2 = [5]
# 3 = [9]
# 4 = [13]
# 5 = [17]
# 6 = [21]
# 7 = [25]
# 8 = [29]
# 9 = [33]