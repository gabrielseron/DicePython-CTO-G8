print("test")
import random
NB_DICE_SIDE = 6
def roll_dice_set(nb_dice_to_roll):
    dice_value_occurence_list = [0] * NB_DICE_SIDE
    for n in range(nb_dice_to_roll):
        dice_value = random.randint(1, NB_DICE_SIDE)
        dice_value_occurence_list[dice_value - 1] += 1
    return dice_value_occurence_list

print(roll_dice_set(100))