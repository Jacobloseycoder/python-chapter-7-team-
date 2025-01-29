import random as r

def main():
    # accepts no arguments
    # Calls all functions to play a number of games
    dice = first_roll()
    output_dice(dice)
    mode = find_mode(dice)
    list_unmatched_dice(dice, mode)
    reroll_many(dice, mode)
def output_dice(dice):
    #accepts no arguments
    #outputs each die in the list
    print(dice)
    
def roll_die():
    #accepts no arguments
    #Returns a random integer from 1 to 6
    number = r.randint(1, 6)
    return number
    
def first_roll():
    dice = []
    bb = 1
    while bb <= 12:
        gg = roll_die()
        dice.append(gg)
        bb = bb + 1
    return dice

def count_frequency(dice):
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    s5 = 0
    s6 = 0
    for dice_roll in dice:
        if dice_roll == 1:
            s1 += 1
        if dice_roll == 2:
            s2 += 1
        if dice_roll == 3:
            s3 += 1
        if dice_roll == 4:
            s4 += 1
        if dice_roll == 5:
            s5 += 1
        if dice_roll == 6:
            s6 += 1
    bing = [s1, s2, s3, s4, s5, s6]
    return bing
    
def find_mode(dice):
    bing = count_frequency(dice)
    maxx = max(bing)
    mode = bing.index(maxx)
    mode = mode + 1
    #print(mode)
    return mode
    
def list_unmatched_dice(dice, mode):
    index = []
    tii = -1
    for indec in dice:
        tii = tii + 1
        if indec != mode:
            index.append(tii)
    #print(index)
    return(index)

def reroll_one(dice, index):
    for indec in index:
        bill = roll_die()
        del dice[indec]
        dice.insert(indec, bill)
        
def reroll_many(dice, mode):
    rere = 'false'
    times = 0
    index = []
    while rere == 'false':
        times = times + 1
        if dice[0] != mode:
            index = list_unmatched_dice(dice, mode)
            reroll_one(dice, index)
            print('roll', times)
            print(dice)
        else:
            if dice[1] != mode:
                index = list_unmatched_dice(dice, mode)
                reroll_one(dice, index)
                print('roll', times)
                print(dice)
            else:
                if dice[2] != mode:
                    index = list_unmatched_dice(dice, mode)
                    reroll_one(dice, index)
                    print('roll', times)
                    print(dice)
                else:
                    if dice[3] != mode:
                        index = list_unmatched_dice(dice, mode)
                        reroll_one(dice, index)
                        print('roll', times)
                        print(dice)
                    else:
                        if dice[4] != mode:
                            index = list_unmatched_dice(dice, mode)
                            reroll_one(dice, index)
                            print('roll', times)
                            print(dice)
                        else:
                            if dice[5] != mode:
                                index = list_unmatched_dice(dice, mode)
                                reroll_one(dice, index)
                                print('roll', times)
                                print(dice)
                            else:
                                if dice[6] != mode:
                                    index = list_unmatched_dice(dice, mode)
                                    reroll_one(dice, index)
                                    print('roll', times)
                                    print(dice)
                                else:
                                    if dice[7] != mode:
                                        index = list_unmatched_dice(dice, mode)
                                        reroll_one(dice, index)
                                        print('roll', times)
                                        print(dice)
                                    else:
                                        if dice[8] != mode:
                                            index = list_unmatched_dice(dice, mode)
                                            reroll_one(dice, index)
                                            print('roll', times)
                                            print(dice)
                                        else:
                                            if dice[9] != mode:
                                                index = list_unmatched_dice(dice, mode)
                                                reroll_one(dice, index)
                                                print('roll', times)
                                                print(dice)
                                            else:
                                                if dice[10] != mode:
                                                    index = list_unmatched_dice(dice, mode)
                                                    reroll_one(dice, index)
                                                    print('roll', times)
                                                    print(dice)
                                                else:
                                                    if dice[11] != mode:
                                                        index = list_unmatched_dice(dice, mode)
                                                        reroll_one(dice, index)
                                                        print('roll', times)
                                                        print(dice)
                                                        if dice[11] == mode:
                                                            rere = 'true'
