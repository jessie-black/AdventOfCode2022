# Given a single line of characters (input), find first position where the 14 most recently recieved characters
# were all different and report index number of NEXT letter.
file_path = 'day6_input.txt' # datastream
with open(file_path) as input_file:
    stream = input_file.read().strip() # Read string from datastream and remove linebreaks
for start in range (len(stream)):
    if len(set(stream[start:start+14]))==14:
        # if making a set of the next 14 characters, it will only have a length of 14 if all 14 characters are unique.
        print(start + 14)  # print the index of the first character after the sequence.
        break
