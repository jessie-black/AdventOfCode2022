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
        selection_score = 0
        opponents_selection=line[0]
        outcome=line[2]
        if outcome=="X": # I need to lose
            selection_score = 0
            if opponents_selection=="A": # and opponent selects rock
                selection_score = selection_score + 3 # I need to select scissors
            elif opponents_selection=="B": # and opponent selects paper
                selection_score = selection_score + 1 # I need to select rock
            else: # and opponent selects scissors
                selection_score = selection_score + 2 # I need to select paper

        elif outcome=="Y": # I need to tie
            selection_score = 3
            if opponents_selection=="A": # and opponent selects rock
                selection_score = selection_score + 1 # rock
            elif opponents_selection=="B": # and opponent selects paper
                selection_score = selection_score + 2 # paper
            else: # and opponent selects scissors
                selection_score = selection_score + 3 # scissors

        else:   # I need to win
            selection_score = 6
            if opponents_selection=="A": # and opponent selects rock
                selection_score = selection_score + 2 # paper
            elif opponents_selection=="B": # and opponent selects paper
                selection_score = selection_score + 3 # scissors
            else: # and opponent selects scissors
                selection_score = selection_score + 1 # rock
        total_score = total_score + selection_score
        print("This round:", selection_score)
        print("Running score:",total_score)
