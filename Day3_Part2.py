# A group of 3 lines will have one letter in common. this is their badge
# what is sum of priorities of badges.

file_path = 'day3_input.txt' # backpack contents
total_sum = 0 #counter
priority = {
    'a':1,'b':2,'c':3,'d':4,'e':5,'f':6,'g':7,'h':8,'i':9,'j':10,'k':11,'l':12,'m':13,'n':14,'o':15,'p':16,'q':17,'r':18,'s':19,'t':20,'u':21,'v':22,'w':23,'x':24,'y':25,'z':26,'A':27,'B':28,'C':29,'D':30,'E':31,'F':32,'G':33,'H':34,'I':35,'J':36,'K':37,'L':38,'M':39,'N':40,'O':41,'P':42,'Q':43,'R':44,'S':45,'T':46,'U':47,'V':48,'W':49,'X':50,'Y':51,'Z':52
}
start=0
end=3
with open(file_path) as input_file:
    all_elves = input_file.readlines()
    for i in range(len(all_elves)//3):
        # because the code examines 3 lines per loop, we only need to loop (total number of lines divided by 3) times.
        for char in all_elves[start]:
            if char in all_elves[start+1] and char in all_elves[start+2]:
                total_sum += priority[char]
                start+=3
                break
print(total_sum)