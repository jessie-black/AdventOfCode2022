# Each line has a set of integer ranges in the form a-b,c-d where a<=b and c<=d
# In how many sets does one set entirely contain the other?
file_path = 'day4_input.txt' # list of sets
total_sum = 0 #counter
with open(file_path) as input_file:
    for line in input_file:
        split_string = line.split(',') # divide into 2 sets of ranges like ["a-b",'c-d\n"]
        first_range = split_string[0].split('-')    #split the first set into separate integers like ['a','b'])
        second_range = split_string[1].strip().split('-')   # split the second set and get rid of newline like ['c','d']
        #Convert all remaining values from character to integer format
        first_range[0] = int(first_range[0])
        first_range[1] = int(first_range[1])
        second_range[0] = int(second_range[0])
        second_range[1] = int(second_range[1])
        if first_range[0] >= second_range[0] and first_range[1] <= second_range[1]:
            # The first range is completely contained within the second
            total_sum+=1
        elif second_range[0]>= first_range[0] and second_range[1] <= first_range[1]:
            # The second range is completely contained within the first
            total_sum+= 1
print(total_sum) # report the total number of sets with complete overlap.