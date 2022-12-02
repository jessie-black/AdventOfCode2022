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
        selection_score = 0
        opponents_selection=line[0]
        my_selection=line[2] #space between letters skipped
        if my_selection=="X": #If I select rock
            selection_score = 1
            if opponents_selection=="A": # and opponent selects rock
                selection_score = selection_score + 3 # draw
            elif opponents_selection=="B": # and opponent selects paper
                selection_score = selection_score + 0 # loss
            else: # and opponent selects scissors: win
                selection_score = selection_score + 6 # win

        elif my_selection=="Y": # if I select paper
            selection_score = 2
            if opponents_selection=="A": # and opponent selects rock
                selection_score = selection_score + 6 # win
            elif opponents_selection=="B": # and opponent selects paper
                selection_score = selection_score + 3 # draw
            else: # and opponent selects scissors
                selection_score = selection_score + 0 # lose

        else:   # if I select scissors
            selection_score = 3
            if opponents_selection=="A": # and opponent selects rock
                selection_score = selection_score + 0 # loss
            elif opponents_selection=="B": # and opponent selects paper
                selection_score = selection_score + 6 # win
            else: # and opponent selects scissors
                selection_score = selection_score + 3 # draw
        total_score = total_score + selection_score
        print("This round:", selection_score)
        print("Running score:",total_score)
