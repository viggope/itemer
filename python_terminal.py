import time
import random



inputer = '>>>'
rowmore = inputer + '\n'
standard = inputer + ''
users = inputer   # >>>
space = inputer + ' '
rowmoreint = 0
spaceint = 0
inpint = 0
inputs = ['>>>', '⁄⁄⁄', '- - -', '≥≥≥', '» » »', ' » ', '»»»', '›››', 'ı Ω', '|§|', '#!', '#', ' ± ',
          '%', '%/', '$', '*!', ' * ', ' •', '^', '___', ': :', '= ', 'R', 'V', '/R', '/V', standard, rowmore, space, users]

def error(error):
    if error == '1' or error == 'To high number error':
        err = 'To high number enrolled'
        errortype = 1
    print('ERROR', errortype, ' ', err)


print('Python terminal 2021   ∑∆◊∆⁄')
while 1 < 2 > 1:
    enter = input(inputer)
    #print(enter)
    #print(len(enter))
    #print(len('change input'))
    #print('change input')
    #print(enter[13])
    #a = 'change input 5'
    #print(a[13])
    #print('change input' in enter and enter[13:len(enter)].isnumeric())
    #print(int(enter[13:len(enter)]) <= len(inputs))
    enter = enter.lower()
    if 'change input' in enter: #or enter[0:9] == 'change inputer' and or enter[0:9] == 'change input':
        if 'change input' in enter and enter[13:len(enter)].isnumeric():
            if int(enter[13:len(enter)]) <= len(inputs):
                if int(enter[13:len(enter)]) >= 0:
                    inputer = inputs[int(enter[13:len(enter) + 1])]
                    print('Input changed to', inputer)
                    inpint = enter[13:len(enter)]
                else:
                    print('ERROR 2_  To low number enrolled')
            else:
                print('ERROR 1_  To high number enrolled')
        else:
            if 'change input rowmore' == enter:
                inputer = inputer + '\n'
                rowmoreint += 1
            if 'change input space' == enter:
                inputer = inputer + ' '
                spaceint += 1
            if 'change input standard' == enter:
                inputer = '>>>'
                spaceint = 0
                rowmoreint = 0
            if 'change input users' == enter:
                inputer = input('Type your inputer')
                spaceint = 0
                rowmoreint = 0
            if 'change input reset' == enter or 'reset inputer' == enter:
                spaceint = 0
                rowmoreint = 0
                print('reseted input to', inputs[int(inpint)])
                inputer = inputs[int(inpint)]

    if enter[0:5] == 'print' or enter[0:4] == 'show':
        if enter[6:len(enter)] == 'len inputs' or enter[6:len(enter)] == 'lenght of inputs' or enter[6:len(enter)] == 'len of inputs':
            print(len(inputs) - 1)
        if enter[6:len(enter)] == 'len inputer':
            print(len(inputer))
        if enter[6:len(enter)] == 'inputs':
            print(inputs)