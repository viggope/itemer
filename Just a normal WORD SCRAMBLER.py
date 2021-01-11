#WORD SCRAMBLER

import time
import random


scramble = 1

while scramble:
    command = input('>>>')
    if command == 'scramble word':
        do = input('What do you want to scramble? \n ')
        ran = random.randint(1, 1)
        time.sleep(2)
       # if ran == 1:
        for counter in range(len(do)):
            print(do[counter], end='\n')
            counter -= random.randint(-3, 3)

