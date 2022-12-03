# Input = list of all items currently in each backpack
# Items are identified by single (case-sensitive) letter
# List of items for each backpack is given as characters on a single line
# First half of characters are in first compartment, 2nd half are in 2nd

#Lowercase items have priority 1-26
# uppercase items have priority 27-52

# REPORT THE SUM OF PRIORITIES THAT APPEAR IN BOTH SIDES OF BACKPACK
file_path = 'day3_input.txt' # backpack contents
total_sum = 0 #counter
priority = {
    'a':1,
    'b':2,
    'c':3,
    'd':4,
    'e':5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
    'j':10,
    'k':11,
    'l':12,
    'm':13,
    'n':14,
    'o':15,
    'p':16,
    'q':17,
    'r':18,
    's':19,
    't':20,
    'u':21,
    'v':22,
    'w':23,
    'x':24,
    'y':25,
    'z':26,
    'A':27,
    'B':28,
    'C':29,
    'D':30,
    'E':31,
    'F':32,
    'G':33,
    'H':34,
    'I':35,
    'J':36,
    'K':37,
    'L':38,
    'M':39,
    'N':40,
    'O':41,
    'P':42,
    'Q':43,
    'R':44,
    'S':45,
    'T':46,
    'U':47,
    'V':48,
    'W':49,
    'X':50,
    'Y':51,
    'Z':52
}
with open(file_path) as input_file:
    for line in input_file:
        length = len(line) #get full length of string
        for char in line:
            if char in line[length//2:length]: # if a character exists in second half
                total_sum+=priority[char]
                break
print(total_sum)