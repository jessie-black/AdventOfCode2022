# Given a strategy guide (input file) with the following info:
# COLUMN 1 = what opponent will play (A = Rock, B = Paper, C = Scissors)
# COLUMN 2 = Required outcome (X = Lose, Y = Draw, Z = Win)
# Total score = sum of scores for each round
# Score for round = shape you selected (1=Rock, 2=Paper, 3=Scissors) + score for outcome (0 = lost, 3 = draw, 6 = won)
# What score would you get IF you followed strategy guide?

file_path = 'day2_input.txt' # strategy guide
total_score = 0
with open(file_path) as input_file:
    for line in input_file:
        opponents_selection=line[0]
        outcome=line[2]
        if outcome=="X": # lose
            if opponents_selection=="A": total_score+=3 # scissors
            elif opponents_selection=="B": total_score+=1 #rock
            else: total_score+=2 #paper

        elif outcome=="Y": # draw
            total_score+=3
            if opponents_selection=="A": total_score +=1 # rock
            elif opponents_selection=="B":total_score +=2 # paper
            else: total_score +=3 # scissors

        else:   # I need to win
            total_score += 6
            if opponents_selection=="A":total_score +=2 # paper
            elif opponents_selection=="B": total_score +=3 # scissors
            else: total_score +=1 # rock

    print("Final score:",total_score)
