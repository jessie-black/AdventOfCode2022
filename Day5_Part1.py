#
#
#
#
#
# Create a function that moves top of one stack to top of another
# I only need to pop final items off of stacks in order.
stacks={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
file_path = 'day5_input.txt' # initial stack setup and instructions
with open(file_path) as input_file:
    original_stacks = input_file.readlines()
for i in range(8): # traverse stacks from bottom to top line by line
    # stacks[1].append(original_stacks[7-i][1])
    for j in range(9):
        if original_stacks[7-i][(j*4)+1]!=" ":
            stacks[j+1].append(original_stacks[7-i][(j*4)+1])
# at this point i have all the stacks


#START AT LINE 10
# Read instructions
for i in range(len(original_stacks)-10):
    current_instruction = (original_stacks[i+10])
    current_instruction = current_instruction.strip().split(" ")
    number=int(current_instruction[1])
    origin=int(current_instruction[3])
    destination=int(current_instruction[5])
    for i in range(number):
        stacks[destination].append(stacks[origin].pop())
for i in range(9):
    print(stacks[i+1])