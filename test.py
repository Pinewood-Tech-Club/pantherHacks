import random
x = random.randint(1, 2)
count = 0
pleaseHelp = False
for i in range(x):
    while not pleaseHelp:
        print('I DONT KNOW WHAT TO DO')
        count = random.randint(1, 10)
        if count >= 5:
            pleaseHelp = True
    if x == 2:
        print('Repeat')
    else:
        print('whoops')

