i=0 #index for list
largest_sum = 0 # initial largest placeholder
elves = [0]*300 #Create a list with enough slots to accomodate all elves
file_path = 'day1_input.txt'
with open(file_path) as input_file:
    for line in input_file:
        if line.strip()=="":
            i=i+1
            continue
        elves[i]=elves[i]+int(line)
sorted_elves = sorted(elves)
sorted_elves.reverse()
print(sorted_elves[0])
print(sorted_elves[250])
print("The three with the most calories have",sorted_elves[0], sorted_elves[1], "and", sorted_elves[2],"calories, respectively.")
print("Total calories: ", sorted_elves[0] + sorted_elves[1]+ sorted_elves[2])

