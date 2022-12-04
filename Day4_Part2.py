# ID numbers overlap
#
# In how many assignment pairs does one range fully contain the other?


file_path = 'day4_input.txt' # backpack contents
total_sum = 0 #counter
with open(file_path) as input_file:
    for line in input_file:
        split_string = line.split(',')
        first_range = split_string[0].split('-')
        second_range = split_string[1].strip().split('-')
        first_range[0] = int(first_range[0])
        first_range[1] = int(first_range[1])
        second_range[0] = int(second_range[0])
        second_range[1] = int(second_range[1])
        print("Line is:",line.strip())
        print("Split string is:", split_string)
        print("First_range is:", first_range)
        print("Second range is:", second_range)
        if first_range[0] <= second_range[1] and first_range[1] >= second_range[0]:
            total_sum+=1
            print("The first range is partially contained the second")
        elif second_range[0] <= first_range[1] and second_range[1] >= first_range[0]:
            total_sum+= 1
            print("The second range partially contained in the first")

print(total_sum)