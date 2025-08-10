import random
RED = "\033[91m"
UNDERLINE = "\033[4m"
RESET = "\033[0m"
def roll_dice():
    sides = ['one', 'two', 'three', 'four', 'five', 'six']
    picked = random.choice(sides)
    chance_of_six = sides.count('six') / len(sides)
    display_chance = f"{chance_of_six:.3f}"
    print(f"{RED}Probability of landing on six: {UNDERLINE}{display_chance}{RESET}")
    if picked == 'six':
        return f"{RED}🎉 You got a six!{RESET}"
    else:
        return f"{RED}Nope, not a six this time.{RESET}"
result = roll_dice()
print(result)