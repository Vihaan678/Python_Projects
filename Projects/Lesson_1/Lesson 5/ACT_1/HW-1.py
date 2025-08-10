import random
def roll_dice():
    rolls=['one','two','three','four','five','six']
    result =random.choice(rolls)
    prob=rolls.count('red') / len(rolls)
    print('Probability of picking the red ball is:',prob)
    if result == 'six':
        return 'Number Six Was Picked'
    else: return 'Number Six Was not Picked'

res=roll_dice()
print(res)