# Read text in put as visual representation of 9 stacks (string format)
# move top N values of one stack onto the top of another - all items moved at once (order conserved)
# Final result = top value from each stack at end of transformations
stacks={1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
file_path = 'day5_input.txt' # initial stack setup and instructions
with open(file_path) as input_file:
    original_stacks = input_file.readlines()
for i in range(8): # traverse stacks from bottom to top line by line to populate stacks
    for j in range(9):
        if original_stacks[7-i][(j*4)+1]!=" ":
            stacks[j+1].append(original_stacks[7-i][(j*4)+1])
# All stacks now represented in list form

# Starting at line 10, read all instructions for movement between stacks
temp_stack=[] # temp stack to preserve order in final move
for i in range(len(original_stacks)-10):
    current_instruction = (original_stacks[i+10])
    current_instruction = current_instruction.strip().split(" ")
    number=int(current_instruction[1])
    origin=int(current_instruction[3])
    destination=int(current_instruction[5])
    for i in range(number): #move items to temporary stack (reversed order)
        temp_stack.append(stacks[origin].pop())
    for i in range(number): #move items to final stack (original order preserved)
        stacks[destination].append(temp_stack.pop())
for i in range(9): #get top item from each stack
    print(stacks[i+1].pop(),end="")