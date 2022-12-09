# Input file is series of movement
# Each line indicates the head of the rope is moving
# In the form R 3 (right 3 spaces), L 2 (left 2 spaces),
# U 5 (up 5 spaces), D 1 (down 1 space)
# Assume H (head) and T (tail) of the rope start in the same position
# Any time H is 2 spaces away (horizontal/vertical/diagonal),
# T must move (horizontal/vertical/diagonal) to be within 1 space

# OBJECTIVE: Count all the positions that the T visited at least once