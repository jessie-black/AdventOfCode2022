# Given a single line of characters (input), find first position where the 4 most recently recieved characters
# were all different and report index number of NEXT letter.

# using sliding window technique
file_path = 'day6_input.txt' # datastream
with open(file_path) as input_file:
    stream = input_file.read().strip() # Read string from datastream and remove linebreaks
for start in range(len(stream)):
    if len(set(stream[start:start+4]))==4:
        #if making a set of the next 4 characters, it will only have a length of 4 if all 4 characters are unique.
        print(start+4) #print the index of the first character after the sequence.
        break
