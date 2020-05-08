import random
min = 1
max = 12

roll_again = "yes"

while roll_again == "yes" or roll_again == "y":
    print "Wait for it"
    print "Results are in"
    print random.randInt(min, max)
