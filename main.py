import random

NB_DICE_SIDE = 6  # Nb of side of the Dices
SCORING_DICE_VALUE_LIST = [1, 5]  # List of the side values of the dice who trigger a standard score
SCORING_MULTIPLIER_LIST = [100, 50]  # List of multiplier for standard score

THRESHOLD_BONUS = 3  # Threshold of the triggering for bonus in term of occurrence of the same slide value
STD_BONUS_MULTIPLIER = 100  # Standard multiplier for bonus
ACE_BONUS_MULTIPLIER = 1000  # Special multiplier for aces bonus


# return a list of dices value occurrence for a roll of nb_dice_to_roll dices
def roll_dice_set(nb_dice_to_roll):
    dice_value_occurrence_list = [0] * NB_DICE_SIDE
    for n in range(nb_dice_to_roll):
        dice_value = random.randint(1, NB_DICE_SIDE)
        dice_value_occurrence_list[dice_value - 1] += 1

    return dice_value_occurrence_list


print(roll_dice_set(6))


def roll_dice_score_standard(dice_value_occurrence_list):
    dice_score = 0
    for n in range(len(dice_value_occurrence_list)):
        for i in range(len(SCORING_DICE_VALUE_LIST)):
            if dice_value_occurrence_list[n] == SCORING_DICE_VALUE_LIST[i]:
                dice_score += SCORING_MULTIPLIER_LIST[i]

        return dice_score



roll_list =  roll_dice_set(6)
print (roll_list)
print(roll_dice_score_standard(roll_list))