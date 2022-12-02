# Given a strategy guide (input file) with the following info:
# COLUMN 1 = what opponent will play (A = Rock, B = Paper, C = Scissors)
# COLUMN 2 = what you should play in response (X = Rock, Y = Paper, Z = Scissors)
# Total score = sum of scores for each round
# Score for round = shape you selected (1=Rock, 2=Paper, 3=Scissors) + score for outcome (0 = lost, 3 = draw, 6 = won)
# What score would you get IF you followed strategy guide?

file_path = 'day2_input.txt' # strategy guide
total_score = 0
with open(file_path) as input_file:
    for line in input_file:
        opponents_selection=line[0]
        my_selection=line[2] #space between letters skipped
        if my_selection=="X": #If I select rock
            total_score+= 1
            if opponents_selection=="A": total_score+= 3 # draw
            elif opponents_selection=="B": total_score+= 0 # loss
            else: total_score+= 6# win

        elif my_selection=="Y": # if I select paper
            total_score+= 2
            if opponents_selection=="A": total_score+= 6 # win
            elif opponents_selection=="B": total_score+= 3 # draw
            else: total_score+= 0 # lose

        else:   # if I select scissors
            total_score+= 3
            if opponents_selection=="A": total_score+= 0 # loss
            elif opponents_selection=="B": total_score+= 6 # win
            else: total_score+= 3 # draw
        print("Final score:",total_score)
