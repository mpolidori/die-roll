#!/bin/env python

import sys
import random


args = sys.argv
valid_dice = [4, 6, 8, 10, 12, 20, 100]

if len(args) > 2:
    print('\n Too many arguments\n')
    quit()

if len(args) == 1:
    print('\n You need to provide a die to roll (e.g. roll d8)\n')
    quit()

dice = args[1]

if 'd' not in dice:
    print('\n You must provide "d" in the die input (e.g. roll 2d20)\n')
    quit()

if dice[-1] == 'd':
    print('\n "d" must be followed by which die to roll (e.g. roll d6)\n')

dice = dice.split('d') if dice[0] != 'd' else [1, dice[1:]]
dice = [int(i) for i in dice]

if dice[1] not in valid_dice:
    dice = ", ".join(
        [str(c) for c in valid_dice[:-1]]) + f', and {valid_dice[-1]}'
    print(f'\n You didn\'t give a valid die. You can only roll {dice}\n')
    quit()

hundred_check = True if dice[1] == 100 else False
total = 0
print('')

try:
    for i in range(int(dice[0])):
        roll = random.randrange(1, int(dice[1]) + 1)
        total += roll

        print(f' {roll}')

    print(f'\n Total: {total}\n')

except KeyboardInterrupt:
    print('\n What are you doing?! I think you tried to roll too many dice...\n')
