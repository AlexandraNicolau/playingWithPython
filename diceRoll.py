import random
import time
min = 1
max = 12

roll_again = True

# while roll_again == "yes" or roll_again == "y":
#     print("Wait for it")
#     print("Results are in!")
#     print(random.randint(min, max))
#     print(random.randint(min, max))

while roll_again:
    print("Wait for it...")
    time.sleep(random.randint(1, 2))
    result = print(random.randint(min, max))
    # print(result)
    roll_again = False
    txt = input("Let's have another go?")
