# read file day1_input.txt
# Assign to a given elf: Sum of all lines
# When line break, move to next elf

# Find largest sum, return that elf # and total calories (Key & Value)

#Truthfully, we only need the total calories of the largest pack.
#To simplify, return largest sum
i=0 #index for list
largest_sum = 0 # initial largest placeholder
elves = [0]*300
file_path = 'day1_input.txt'
with open(file_path) as input_file:
    for line in input_file:
        if line.strip()=="":
            if elves[i]>largest_sum:
                largest_sum=elves[i]
            print("elf #", i, "has", elves[i], "calories")
            i=i+1
            continue
        elves[i]=elves[i]+int(line)
print("The elf with the most calories has",largest_sum,"calories")

