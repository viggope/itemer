import os
import time
import random




a = 0

fipole = 0                #rare
mybox = 1
keys = 0                    #common
huntri = 0               #epic
pen = 0                     #common
phoca = 0
coins = 0              #common
daysaleint = random.randint(1, 9)
salepercent = random.randint(18, 68)


 #values
dia = 0
gold = 0

#Prices
fi2 = 105
ba1 = 15
bait2 = 155
am2 = 10


balloon = 0                 #uncommon
aumo: int = 0                 #rare


ammo: int = 0               #uncommon
fiwork: int = 0                #rare
bait: int = 0               #uncommon


cofish = 0                  #common
rafish = 0                  #rare           tip: you can't get fishes in mystery boxes. You can only buy them in the shop.
epfish = 0                  #epic

fox = 0                     #common
boar = 0                    #rare
duck = 0                    #common
bear = 0                    #epic
rabbit = 0                  #common

def clear():
    os.system('clear')

daysales=['Fishing pole', 'Mystery box', 'Key', 'Hunting rifle', 'Pen', 'Phone call', 'Bait', 'Ammunition', 'Fire works']
daysale=daysales[daysaleint-1]
#if daysaleint == 1:
#    daysale = 'Fishing pole'
#if daysaleint == 2:
#    daysale = 'Mystery box'
#if daysaleint == 3:
#    daysale = 'Key'
#if daysaleint == 4:
#    daysale = 'Hunting rifle'
#if daysaleint == 5:
#    daysale = 'Pen'
#if daysaleint == 6:
#    daysale = 'Phone call'
#if daysaleint == 7:
#    daysale = 'Bait'
#if daysaleint == 8:
#    daysale = 'Ammunition'
#if daysaleint == 9:
#    daysale = 'Fire works'

print('____________________________')
print('============================')
print('Alternatives:')
print('Fish')
play = 1
while play:
    do = input('>>> ')
    if do == 'fish':
        if fipole >= 1:
            if bait >= 1:
                bait -= 1
                print('Fishing. . .')
                time.sleep(random.randint(1, 3))
                ran = random.randint(1, 10)
                if ran == 1 or ran == 2 or ran == 3:
                    print('You missed')
                elif ran == 4 or ran == 5:
                    print('You got 3x |Common fish|')
                    cofish += 3
                elif ran == 6:
                    print('You got a |Rare fish|')
                    rafish += 1
                elif ran == 7:
                    print('You got an |EPIC FISH|')
                    epfish += 1
                elif ran == 8:
                    print('JACK POT! You got 5x |EPIC FISH|')
                    epfish += 5
                elif ran == 9 and rafish >= 1:
                    print('Oh no! A cat stole all your fishes.\nTip: You should |sell| your fishes more often')
                    cofish = 0
                    rafish = 0
                    epfish = 0
                elif ran == 10:
                    print('EPIC MOMENT: A shark took your fishing pole. But he left a |Common fish|')
                    fipole -= 1
                    cofish += 1
                else:
                    print('You got 2x |Rare fishes|')
                    rafish += 2

            else:
                ran = random.randint(0, 5)
                if ran == 1:
                    print('No idea to fish without any bait.\nTip:     Go to the |shop| and buy some.')
                else:
                    print('No idea to fish without any bait.')
        else:
            ran = random.randint(0, 5)
            if ran == 1:
                print('No idea to fish without fishing pole.\nTip:     Go to the |shop| and buy one.')
            else:
                print('No idea to fish without fishing pole.')



    if do == 'shop':
        clear()
        b = 200
        c = 75
        d = 50
        e = 250
        f = 20
        g = 100
        h = 25
        i = 40
        j = 45
        if daysaleint == 1:
            a = 200
            b = round(a / (salepercent / 10))
        if daysaleint == 2:
            a = 75
            c = round(a / (salepercent / 10))
        if daysaleint == 3:
            a = 50
            d = round(a / (salepercent / 10))
        if daysaleint == 4:
            a = 250
            e = round(a / (salepercent / 10))
        if daysaleint == 5:
            a = 20
            f = round(a / (salepercent / 10))
        if daysaleint == 6:
            a = 100
            g = round(a / (salepercent / 10))
        if daysaleint == 7:
            a = 25
            h = round(a / (salepercent / 10))
        if daysaleint == 8:
            a = 40
            i = round(a / (salepercent / 10))
        if daysaleint == 9:
            a = 45
            j = round(a / (salepercent / 10))


        print('Going to shop. . .')
        # time.sleep(random.randint(2, 3))
        print('_ _ _ _   S H O P   _ _ _ _')
        print(': Fishing pole           ' + str(b) + ' coins (', fipole, ')')
        print(': Bait 3x          ' + str(h) + ' coins (', bait, ')')
        print(': Mystery box            ' + str(c) + ' coins (', mybox, ')')
        print(': Key                     ' + str(d) + ' coins (', keys, ')')
        print(': Hunting rifle          ' + str(e) + ' coins (', huntri, ')')
        print(': Ammunition 20x       ' + str(i) + ' coins (', ammo, ')')
        print(': Pen                     ' + str(f) + ' coins (', pen, ')')
        print(': Phone call             ' + str(g) + ' coins (', phoca, ')')
        print(': Fireworks 3x             ' + str(j) + ' coins (', fiwork, ')')
        print(':--------------------------------------:')
        print('| Todays offer:  |', daysale, '|', salepercent, '% ', str(round(a / (salepercent / 10))), 'coins  |')
    if do[0:3] == 'buy':
     #   print(do[4:len(do)])
        item=do[4:len(do)]
        items={'fishing pole': (b, 1), 'mystery box': (c, 1), 'key': (d, 1), 'hunting rifle': (e, 1),  'bait': (h, 3), 'ammonition': (i, 20), 'fireworks': (j, 3), 'pen': (f, 1), 'phone call': (g, 1)}
        i_name=item
        item=items.get(item)
        if coins>=item[0]:
            print(f'{i_name.capitalize()} bought')
            coins-=item[0]
            if i_name=='fishing pole':
                fipole+=item[1]
            if i_name=='mystery box':
                mybox+=item[1]
            if i_name=='key':
                keys+=item[1]
            if i_name=='hunting rifle':
                huntri+=item[1]
            if i_name=='bait':
                bait+=item[1]
            if i_name=='ammonition':
                ammo+=item[1]
            if i_name=='fireworks':
                fiwork+=item[1]
            if i_name=='pen':
                pen+=item[1]
            if i_name=='phone call':
                phoca+=item[1]
            coins-=item[0]
        else:
            print(f'You dont have enough money ({str(coins)}/ {str(item[0])} )')
##        if do[4:len(do)] == 'fishing pole' and coins >= 200:
##            print('Fishing pole bought')
##
##            fipole += 1
##            if daysaleint == 1:
##                coins -= (200 / (salepercent / 10))
##            else:
##                coins -= 200
##        elif do[4:len(do)] == 'fishing pole' and not coins >= 200:
##            print('You dont have enough money (', coins, '/ 200 )')
##        if (do[4:len(do)] == 'mystery box') and coins >= 75 or (do[4:len(do)] == 'box') and coins >= 75:
##            print('Mystery box bought')
##            mybox += 1
##            if daysaleint == 2:
##                coins -= (75 / (salepercent / 10))
##            else:
##                coins -= 75
##        elif do[4:len(do)] == 'mystery box' and not coins >= 75:
##            print('You dont have enough money (', coins, '/ 75 )')
##        if do[4:len(do)] == 'key' and coins >= 50:
##            print('Key bought')
##            keys += 1
##            if daysaleint == 3:
##                coins -= (50 / (salepercent / 10))
##            else:
##                coins -= 50
##        elif do[4:len(do)] == 'key' and not coins >= 50:
##            print('You dont have enough money (', coins, '/ 50 )')
##        if do[4:len(do)] == 'hunting rifle' and coins >= 250:
##            print('Hunting rifle bought')
##            huntri += 1
##            if daysaleint == 4:
##                coins -= (250 / (salepercent / 10))
##            else:
##                coins -= 250
##        elif do[4:len(do)] == 'hunting rifle' and not coins >= 250:
##            print('You dont have enough money (', coins, '/ 250 )')
##        if do[4:len(do)] == 'bait' and coins >= 25:
##            print('3x Bait bought')
##            bait += 3
##            if daysaleint == 7:
##                coins -= (25 / (salepercent / 10))
##            else:
##                coins -= 25
##        elif do[4:len(do)] == 'bait' and not coins >= 25:
##            print('You dont have enough money (', coins, '/ 25 )')
##        if do[4:len(do)] == 'ammonition' and coins >= 40:
##            print('20x Ammunition bought')
##            ammo += 20
##            if daysaleint == 8:
##                coins -= (40 / (salepercent / 10))
##            else:
##                coins -= 40
##        elif do[4:len(do)] == 'ammunition' and not coins >= 40:
##            print('You dont have enough money (', coins, '/ 40 )')
##        if do[4:len(do)] == 'fireworks' and coins >= 45:
##            print('3x Fireworks bought')
##            fiwork += 3
##            if daysaleint == 9:
##                coins -= (45 / (salepercent / 10))
##            else:
##                coins -= 45
##        elif do[4:len(do)] == 'fireworks' and not coins >= 45:
##            print('You dont have enough money (', coins, '/ 45 )')



    if do == 'wallet' or do == 'inv':
        round(coins)
        print('Wallet: ', round(coins))
        if rabbit >= 1:
            print('Rabbits: ', rabbit)
        if boar >= 1:
            print('Boars: ', boar)
        if fox >= 1:
            print('Foxes: ', fox)
        if bear >= 1:
            print('Bears: ', bear)
        if duck >= 1:
            print('Ducks: ', duck)
        if fipole >= 1:
            print('Fishing pole')
        if huntri >= 1:
            print('Hunting rifle')
        if keys >= 1:
            print('Keys: ', keys)
        if mybox >= 1:
            print('Mystery boxes: ', mybox)
        if pen >= 1:
            print('Pens: ', pen)
        if bait >= 1:
            print('Baits: ', bait)
        if ammo >= 1:
            print('Ammunition: ', ammo)
        if cofish >= 1:
            print('Common fish: ', cofish)
        if rafish >= 1:
            print('Rare fish: ', rafish)
        if epfish >= 1:
            print('Epic fish: ', epfish)
        if fiwork >= 1:
            print('Fireworks: ', fiwork)
        if balloon >= 1:
            print('Balloons: ', balloon)
        if aumo >= 1:
            print('Automatic aim ammunition: ', aumo)



    if do == 'hunt':
        if huntri >= 1:
            if aumo >= 1:
                print('Hunting with auto ammunition. . .')
                aumo -= 1
                time.sleep(2.6)
                ran = random.randint(1, 10)
                if ran == 1:
                    print('PANG!')
                    print('You hit a whole |Duck| family. (4)')
                    duck += 4
                elif ran == 2:
                    print('PANG!')
                    print('Wow! You hit a target 500 meter away! You got a reward on 500 coins!')
                    duck += 4
                elif ran == 3 or  ran == 4:
                    print('PANG!')
                    print('You shot a |Rabbit|')
                    rabbit += 1
                elif ran == 5:
                    print('PANG!')
                    print('You scoped at wrong direction. You shot yourself.')
                    coins = 0
                    duck = 0
                    rabbit = 0
                    boar = 0
                    fox = 0
                    bear = 0
                    cofish = 0
                    rafish = 0
                    epfish = 0
                    bait = 0
                    fipole = 0
                    huntri = 0
                    fiwork = 0
                    ammo = 0
                    key = 0
                    phoca = 0
                    pen = 0
                    mybox = 0
                    aumo = 0
                elif ran == 6:
                    print('PANG!')
                    print('You shot a |Duck|')
                    duck += 1
                elif ran == 7:
                    print('PANG!')
                    print('You shot an |BOAR|')
                    boar += 1
                elif ran == 8:
                    print('PANG!')
                    print('You shot a EPIC |BEAR|')
                    bear += 1
                elif ran == 9 or ran == 10:
                    print('PANG!')
                    print('You shot an |Fox|')
            if ammo >= 1:
                ammo -= 1
                print('Hunting. . .')
                time.sleep(2.5)
                ran = random.randint(1, 12)
                if ran == 1 or ran == 2:
                    print('All animals were hiding')
                elif ran == 3 or  ran == 4 or ran == 5:
                    print('PANG!')
                    print('You shot a |Rabbit|')
                    rabbit += 1
                elif ran == 6:
                    print('PANG!')
                    print('You shot a |Duck|')
                    duck += 1
                elif ran == 7:
                    print('PANG!')
                    print('You shot a |BOAR|')
                    boar += 1
                elif ran == 8:
                    print('PANG!')
                    print('You shot an EPIC |BEAR|')
                    bear += 1
                elif ran == 9 or ran == 10:
                    print('PANG!')
                    print('You shot an |Fox|')
                    fox += 1
                elif ran == 11:
                    print('PANG!')
                    print('Wow. . . you hit a robber that were running from the police. \nThe police gave you so much money that you can buy a new rifle.\nThey took all your rifles because killing a human.')
                    coins += 300
                    huntri = 0
                elif ran == 12:
                    print('LEGENDARY MOMENT: \n An |Unicorn| came with a good advice,\n"Stop shoot animals".\nPANG!\nYou ignore that and killed the unicorn.\nThe unicorn took all your money, your rifle and then disapeared.')
                    coins = 0
                    huntri = 0

            else:
                ran = random.randint(0, 5)
                if ran == 1:
                    print('Hahaha. You think you have an air rifle. Shooting air is maybe good for the climate.\nTip:     Go to the |shop| and buy some |Ammunition|.')
                else:
                    print('No idea to fish without any bait.')
        else:
            ran = random.randint(0, 5)
            if ran == 1:
                print('No idea to hunt without |Hunting rifle|.\nTip:     Go to the |shop| and buy one.')
            else:
                print('No idea to hunt without |Hunting rifle|.')



    if do[0:4] == 'sell':
        #   print(do[4:len(do)])
        if do[5:len(do)] == 'fishing pole' and fipole >= 1:
            print('|Fishing pole| sold for 75 coins')

            fipole -= 1

            coins += 75
        elif do[5:len(do)] == 'fishing pole' and not fipole >= 1:
            print('You dont own that item')

        if do[5:len(do)] == 'common fish' and cofish >= 1:
            print('|Common fish| sold for 15 coins')

            cofish -= 1

            coins += 15
        elif do[5:len(do)] == 'common fish' and cofish >= 1:
            print('You dont own that item')

        if do[5:len(do)] == 'rare fish' and rafish >= 1:
            print('|Rare fish| sold for 25 coins')

            rafish -= 1

            coins += 25
        elif do[5:len(do)] == 'rare fish' and rafish >= 1:
            print('You dont own that item')

        if do[5:len(do)] == 'epic fish' and epfish >= 1:
            print('|Epic fish| sold for 45 coins')

            epfish -= 1

            coins += 45
        elif do[5:len(do)] == 'epic fish' and epfish >= 1:
            print('You dont own that item')

        if do[5:len(do)] == 'hunting rifle' and huntri >= 1:
            print('|Hunting rifle| sold for 110 coins')

            huntri -= 1

            coins += 110
        elif do[5:len(do)] == 'hunting rifle' and huntri >= 1:
            print('You dont own that item')

        if do[5:len(do)] == 'rabbit' and rabbit >= 1:
            print('|Rabbit| sold for 25 coins')

            rabbit -= 1

            coins += 25
        elif do[5:len(do)] == 'rabbit' and rabbit >= 1:
            print('You dont own that item')

        if do[5:len(do)] == 'fox' and fox >= 1:
            print('|Fox| sold for 20 coins')

            fox -= 1

            coins += 20
        elif do[5:len(do)] == 'fox' and fox >= 1:
            print('You dont own that item')

        if do[5:len(do)] == 'boar' and boar >= 1:
            print('|Boar| sold for 55 coins')

            boar -= 1

            coins += 55
        elif do[5:len(do)] == 'boar' and boar >= 1:
            print('You dont own that item')

        if do[5:len(do)] == 'bear' and bear >= 1:
            print('|Bear| sold for 75 coins')

            bear -= 1

            coins += 75
        elif do[5:len(do)] == 'bear' and bear >= 1:
            print('You dont own that item')

        if do[5:len(do)] == 'duck' and duck >= 1:
            print('|Duck| sold for 30 coins')

            duck -= 1

            coins += 30
        elif do[5:len(do)] == 'duck' and duck >= 1:
            print('You dont own that item')

        if do[5:len(do)] == 'gold' and gold >= 1:
            print('|Gold| sold for 150 coins')

            gold -= 1

            coins += 150
        elif do[5:len(do)] == 'gold' and gold >= 1:
            print('You dont own that item')

        if do[5:len(do)] == 'diamond' and dia >= 1:
            print('|Diamond| sold for 3000 coins')

            dia -= 1

            coins += 3000
        elif do[5:len(do)] == 'diamond' and dia >= 1:
            print('You dont own that item')

        if do[5:len(do)] == 'key' and keys >= 1:
            print('|Diamond| sold for 3000 coins')

            keys -= 1

            coins += 30
        elif do[5:len(do)] == 'key' and keys >= 1:
            print('You dont own that item')



    if do == 'light firework' or do == 'use firework':
        if fiwork >= 1:
            fiwork -= 1
            print('Lights fireworks. . .')
            time.sleep(2)
            print('BOOM!')
            ran = random.randint(1, 5)
            if ran == 1 or ran == 2:
                print('An amazing pattern shows up in the sky')
            if ran == 3:
                print('Oops. You hit a whole duck family. (4x)')
                duck += 4
            if ran == 4:
                print('WOW!. It rains to many coins that I cant count them. (300x)')
                coins += 300
            if ran == 5:
                print('Oops. It tipped over and BOOM! It hit you. You simply exploded.')
                coins = 0
                duck = 0
                rabbit = 0
                boar = 0
                fox = 0
                bear = 0
                cofish = 0
                rafish = 0
                epfish = 0
                bait = 0
                fipole = 0
                huntri = 0
                fiwork = 0
                ammo = 0
                key = 0
                phoca = 0
                pen = 0
                mybox = 0
                balloon = 0

        else:
            print('You dont own that item. Tip: Go to the |shop| and buy one')

    if do == 'shop limited' or do == 'limited shop':
        j = 45
        if daysaleint == 9:
            a = 45
            j = round(a / (salepercent / 10))


        print('Going to shop. . .')
        # time.sleep(random.randint(2, 3))
        print('_ _ _ _ _   S H O P   _ _ _ _ _')
        print('  L I M I T E D   O F F E R S  ')
        print(': Fireworks 3x     code: fireworks     ' + str(j) + ' coins (', fiwork, ')')
        print(': Fireworks 12x     code: fireworks2     ' + str(fi2) + ' coins (', fiwork, ')')
        print(': Balloon     code: balloon     ' + str(ba1) + ' coins (', balloon, ')')
        print(': Bait 15x     code: bait2     ' + str(bait2) + ' coins (', bait, ')')
        print(': Automatic aim ammo 3x     code: autoammo     ' + str(am2) + ' coins (', aumo, ')')
        print(':-----------------------------------------------------:')
        print('| Todays offer:  |', daysale, '|', salepercent, '% ', str(round(a / (salepercent / 10))), 'coins  |')
    if do[0:3] == 'buy':
     #   print(do[4:len(do)])
        if do[4:len(do)] == 'fireworks2' and coins >= fi2:
            print('12x Fireworks bought')

            fiwork += 12
            if daysaleint == 9:
                coins -= (fi2 / (salepercent / 15))
            else:
                coins -= fi2
        elif do[4:len(do)] == 'fireworks2' and not coins >= fi2:
            print('You dont have enough money (', coins, '/', fi2, ')')

        if do[4:len(do)] == 'balloon' and coins >= ba1:
            print('Balloon bought')

            balloon += 12
            coins -= ba1

        elif do[4:len(do)] == 'balloon' and not coins >= ba1:
            print('You dont have enough money (', coins, '/', ba1, ')')

        if do[4:len(do)] == 'bait2' and coins >= bait2:
            print('15x Bait bought')

            bait += 15
            coins -= bait2

        elif do[4:len(do)] == 'bait2' and not coins >= bait2:
            print('You dont have enough money (', coins, '/', bait2, ')')

        if do[4:len(do)] == 'autoammo' and coins >= am2:
            print('3x Automatic aim ammo bought')

            aumo += 3
            coins -= am2

        elif do[4:len(do)] == 'autoammo' and not coins >= am2:
            print('You dont have enough money (', coins, '/', am2, ')')

    if do == 'pang balloon' or do == 'use balloon':
        if balloon >= 1:
            balloon -= 1
            print('PANG!')
            ran = random.randint(1, 5)
            if ran == 1 or ran == 2:
                print('Empty')
            if ran == 3:
                print('20 coins in a balloon?')
                coins += 20
            if ran == 4:
                print('HAHAHAHAHA! A |BEAR|?')
                bear += 1
            if ran == 5:
                print('Ehh, 3 ammunition?')
                ammo += 3
            if ran == 6:
                print('A BALLOON IN A BALLOON!?')
                balloon += 1

        else:
            print('You dont own that item. Tip: go to the |limited shop| and buy one.')


    if do == 'open mystery box' or do == 'open box' or do == 'search box':
        if mybox >= 1:
            mybox -= 1
            print('Opening mystery box. . .')
            time.sleep(2)
            print('You got:  ')
            time.sleep(1)
            ran = random.randint(0, 3)              # ran = random.randint(1, 10)
            if ran >= 1:
                print(ran, 'x  |Bait|')
                bait += ran
                time.sleep(1)
            ran = random.randint(0, 3)  # ran = random.randint(1, 10)
            if ran >= 1:
                print(ran, 'x  |Fireworks|')
                fiwork += ran
                time.sleep(1)
            ran = random.randint(0, 2)
            if ran >= 1:
                print(ran, 'x  |Rabbits|')
                rabbit += ran
                time.sleep(1)
            ran = random.randint(0, 7)
            if ran >= 1:
                print(ran, 'x  |Ammunition|')
                ammo += ran
                time.sleep(1)
            ran = random.randint(0, 2)
            if ran >= 1:
                print(ran, 'x  |Balloons|')
                balloon += ran
                time.sleep(1)
            ran = random.randint(0, 3)
            if ran == 3:
                ran = random.randint(1, 5)
                print(ran, 'x  |Gold|')
                gold += ran
                time.sleep(1)
            ran = random.randint(0, 3)
            if ran == 5:
                print(ran, 'LEGENDARY MOMENT:\nYou got a |Diamond|')
                dia += 1
                time.sleep(1)
            ran = random.randint(0, 7)
            if ran == 7:
                if fipole == 0:
                    print('WOW! You got a |Fishing pole|!')
                    fipole += 1
                elif huntri == 0:
                    print('EPIC MOMENT:\nYou got a |Hunting rifle| + 200 ammunition')
                    huntri += 1
                    ammo += 200
                    time.sleep(1)
                else:
                    print('JACK POT!\nYou got 1000 |COINS|!')
                    coins += 1000


    if do[0:8] == 'sell max' or do[0:8] == 'sell all':
        coins += rabbit * 25
        rabbit = 0
        coins += fox * 20
        fox = 0
        coins += boar * 55
        boar = 0
        coins += bear * 75
        bear = 0
        coins += duck * 30
        duck = 0

        coins += cofish * 15
        coins += rafish * 25
        coins += epfish * 45

        coins += gold * 150
        gold = 0
        coins += dia * 3000
        dia = 0

    if do[0:15] == 'sell everything':
        coins += rabbit * 25
        rabbit = 0
        coins += fox * 20
        fox = 0
        coins += boar * 55
        boar = 0
        coins += bear * 75
        bear = 0
        coins += duck * 30
        duck = 0
        coins += cofish * 15
        coins += rafish * 25
        coins += epfish * 45
        coins += gold * 150
        gold = 0
        coins += dia * 3000
        dia = 0

        coins += fipole * 75
        fipole = 0
        coins += huntri * 110
        huntri = 0

    if do[0:12] == 'sell animals':
        coins += rabbit * 25
        rabbit = 0
        coins += fox * 20
        fox = 0
        coins += boar * 55
        boar = 0
        coins += bear * 75
        bear = 0
        coins += duck * 30
        duck = 0
        coins += cofish * 15
        coins += rafish * 25
        coins += epfish * 45

    if do[0:11] == 'sell fishes':
        duck = 0
        coins += cofish * 15
        coins += rafish * 25
        coins += epfish * 45

    if do[0:11] == 'sell stones':
        coins += gold * 150
        gold = 0
        coins += dia * 3000
        dia = 0

    #if do[0:5] == 'trash':
