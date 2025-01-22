import random as r
def main():
    # accepts no arguments
    # Calls all functions to play a number of games
    games = input("How many games: ")
    dice = [1, 2, 3, 4, 5, 6]
    #count_frequency()
    
def output_dice(dice):
    #accepts no arguments
    #outputs each die in the list
    for number in dice:
        print (number)
        
def roll_die():
    #accepts no arguments
    #Returns a random integer from 1 to 6
    dice_roll = r.randint(1, 6)
    
def first_roll():
    pass
def count_frequency(dice, number):
    pass
def find_mode(dice):
    pass
def list_unmatched_dice(dice, mode):
    index = []
    for indec in dice:
        if indec != mode:
            index.append(indec)
    return(index)
def reroll_one(dice, index):
    for indec in index:
        bill = roll_die()
        del dice[indec]
        dice.insert(indec, bill)
def reroll_many(dice, mode):
    rere = 'false'
    index = []
    while rere == 'false':
        if dice[0] != mode:
            index = list_unmatched_dice(dice, mode)
            reroll_one(dice, index)
        else:
            if dice[1] != mode:
                index = list_unmatched_dice(dice, mode)
                reroll_one(dice, index)
            else:
                if dice[2] != mode:
                    index = list_unmatched_dice(dice, mode)
                    reroll_one(dice, index)
                else:
                    if dice[3] != mode:
                        index = list_unmatched_dice(dice, mode)
                        reroll_one(dice, index)
                    else:
                        if dice[4] != mode:
                            index = list_unmatched_dice(dice, mode)
                            reroll_one(dice, index)
                        else:
                            if dice[5] != mode:
                                index = list_unmatched_dice(dice, mode)
                                reroll_one(dice, index)
                            else:
                                if dice[6] != mode:
                                    index = list_unmatched_dice(dice, mode)
                                    reroll_one(dice, index)
                                else:
                                    if dice[7] != mode:
                                        index = list_unmatched_dice(dice, mode)
                                        reroll_one(dice, index)
                                    else:
                                        if dice[8] != mode:
                                            index = list_unmatched_dice(dice, mode)
                                            reroll_one(dice, index)
                                        else:
                                            if dice[9] != mode:
                                                index = list_unmatched_dice(dice, mode)
                                                reroll_one(dice, index)
                                            else:
