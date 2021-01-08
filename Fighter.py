import time
import random

version = 'Alpha '

ehealth = 0   #enemy health
health = 0
sword = 0
swole = 1    #sword level
level = 1


print('The enemy is raiding our island! You need to stop them!')
time.sleep(2)
print('Here take this sword')
print('1x sword (1)')
time.sleep(2)
print('Sword info:\nDamage:', swole * 5, '\nLevel:', swole, '\nSword accuracy:', swole * 10, '% ')
time.sleep(3)
print('An enemy comming! Fight with your sword. You can select heal instead of stabbing with sword if you are low')
time.sleep(5)
print('Starting fight. . .')
time.sleep(2.3)
fight = 1
ingame = 1
pturn = 1
eturn = 0
while ingame:
    ehealth = (level * 20) - 5
    health = (level * 15) + 5

    while fight:
        while pturn:
            print('Enemy has', ehealth)
            time.sleep(0.1)
            print('Your health:', health)
            time.sleep(0.1)
            print('1 Stab with sword')
            time.sleep(0.1)
            print('2 Heal')
            do = int(input(''))
            if do == 1:
                ran = random.randint(1, 100 / swole * 10)
                if ran == 1:
                    ehealth -= swole * 5
                    print('You stabbed the enemy. He has now', ehealth, 'health')
                else:
                    print('You missed')
            if do == 2:
                health += level * 2
                print('Healed', level * 2 , 'health')

            #Samma sak med fienden sen




