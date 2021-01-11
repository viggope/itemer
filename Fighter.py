import time
import random

version = 'Alpha '

ehealth = 0   #enemy health
health = 0
sword = 0
swole = 1    #sword level
bow = 0
bowle = 0
swohe = 1  # swohe = 0
swohele = 1  # swohele = 0
level = 4   # level = 1
eneacc = 10

print('The enemy is raiding our island! You need to stop them!')
time.sleep(2)
print('Here take this sword')
print('1x sword (1)')
time.sleep(2)
print('Sword info:\nDamage:', swole * 5, '\nLevel:', swole, '\nSword accuracy: 60')#, swole * 15, '% ')
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
    eneacc = level * 15 - 10
    if level == 1:
        eneacc = 20
    while fight:
        while pturn:
            print('Your turn')
            time.sleep(0.1)
            print('Enemy has', ehealth, 'health')
            time.sleep(0.1)
            print('Your health:', health)
            time.sleep(0.1)
            print('1 Stab with sword (' + str(swole * 5) + ')  level', swole)
            time.sleep(0.1)
            print('2 Heal (' + str(level * 2) + ')  level', level)
            if swohe >= 1:
                print('3 Sword heal combo (', swohe, ')  level', swohele)
            do = input('')
            if do == '1':
                ran = random.randint(1, (100 / (swole * 20)))
                if ran == 1:
                    ehealth -= swole * 5
                    print('You stabbed the enemy. He have now', ehealth, 'health')
                else:
                    print('You missed')
                eturn = 1
                pturn = 0
            if do == '2':
                health += level * 2
                print('Healed', level * 2, 'health')
                eturn = 1
                pturn = 0
            if do == '3' and swohe <= 1:
                ran = random.randint(1, round(100 / (swole * 20)))
                if ran == 1:
                    ehealth -= swohele * 5
                    health += swohele
                    print('You stabbed the enemy. He have now', ehealth, 'health and you healed', swohele, 'health')
                else:
                    health += swohele
                    print('You missed but healed', swohele, 'health')
                    eturn = 1
                    pturn = 0
        if ehealth <= 0:
            swole += 1
            bowle += 1
            print('YOU WON!')
            print('You got:')
            print('Sword level', swole)
            print('Bow level', bowle)
            if level == 4:
                swohe += 1
                print('Sword heal combo (', swohele * 5, '&', level * 3 - swohele, ')')
            if swohe >= 1:
                print('Sword heal combo level', swohele)

            time.sleep(5)
            pturn = 0
            fight = 0

        while eturn:
            time.sleep(4)
            print('Enemies turn')
            time.sleep(0.1)
            print('Enemy has', ehealth, 'health')
            time.sleep(0.1)
            print('Your health:', health)
            time.sleep(0.1)
            print('1 Stab with sword (', level * 5, ')')
            time.sleep(0.1)
            print('2 Shoot with bow (', level * 3 + 1, ')')
            time.sleep(0.1)
            print('3 Heal (', level * 2 - 1, ')')
            time.sleep(2)
            ran = random.randint(1, 6)
            if ran == 1 or ran == 2:
                ran = random.randint(1, eneacc / level * 10)
                if ran == 1:
                    health -= level * 5
                    print('The enemy stabbed you. You have now', health, 'health')
                else:
                    print('The enemy missed you')
            if ran == 3 or ran == 4:
                health -= level * 3 + 1
                print('The enemy hit you with bow which has perfectly aim. You have now', health, 'health')
            if ran == 5:
                ehealth += level * 2 - 1
                print('The enemy healed', level * 2 - 1)
            if ran == 6:
                print('The enemy missed')
            pturn = 1
            eturn = 0
            time.sleep(3)

        if health <= 0:
            print('YOU LOSE!')
            print('The enemy killed you. Devolving level. . .')
            level -= 1
            time.sleep(5)
            if level <= 0:
                level = 1








