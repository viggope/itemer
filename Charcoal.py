import time
import random




houses = 0
coins = 0
loans = 0
rent = 0
month = 0



print('STARTING HOMESHOP SIMULATOR')
time.sleep(2)
print('You are home. . .')
time.sleep(2)
print('You dont have any money. . .')
time.sleep(1)
print('Type L to loan.')
print('Example:  \n  l \n Then they ask how much;')
print('Example:  How much do you want to loan?')
print('Example:  100')
print('Example:  100 coins loaned')
do = input('Try to loan some coins:      ')
did = 1
while did:
    do = int(input('How much?'))
    if 100 <= do <= 10000:
        coins += do
        print(str(do) + ' coins loaned')
        print('Rent:', str(round(do / 50)), 'coins')
        play = 1
        print('Now you learned how to loan.  Press H to get help and examples\n Press I to get info.')
        print('Month 1. . .')
        did = 0
        starttime = time.time()
while play:
    do = input('\n')
    if time.time() - 10 >= starttime():
        print('You need to pay rent ', str(rent))
    if do == 'l':
        do = int(input('How much?'))
        if 100 <= do:
            coins += do
            print(str(do) + ' coins loaned')
            rent += do / 50
            print('Rent:', rent, 'coins')

            starttime = time.time()
    if do == 'p':
        print('Pay rent?\nY yes\nN no')
        do = input('')
        if do == 'y' and coins >= rent:
            coins -= rent
            rent = 0
            print('Rent paid')
        elif coins <= rent - 1:
            print('Oh no. You cannot pay rent. You is enough poor')
        else:
            print('Well do that later.')

    if do == 'b':
        print('Inventory:')
        print('Coins: ' + str(coins))






