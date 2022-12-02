# Challenge: Find the elf with the most calories in their bag.
# the file day1_input.txt contains lines  of integers -- all integers
# belong to the current elf, blank lines indicate changes in elves.

# Find largest overall sum for any single elf & report it

i=0 #index for list
largest_sum = 0 # initial largest placeholder
elves = [0]*300 # create a list with enough lines to accomodate all elves
file_path = 'day1_input.txt'
with open(file_path) as input_file:
    for line in input_file:
        if line.strip()=="":
            if elves[i]>largest_sum:
                largest_sum=elves[i]
            i=i+1
            continue
        elves[i]=elves[i]+int(line)
print("The elf with the most calories has",largest_sum,"calories")

