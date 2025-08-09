import random
def pick_ball():
    balls=['blue','red','green']
    result =random.choice(balls)
    prob=balls.count('red') / len(balls)
    print('Probability of picking the red ball is:',prob)
    if result == 'red':
        return 'Red ball was picked'
    else: return 'Red ball was not picked'

res=pick_ball()
print(res)