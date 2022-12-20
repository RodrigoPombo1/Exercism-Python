# Score categories.
# Change the values as you see fit.
YACHT = lambda dice: 50 if len(list(filter(lambda x: x==dice[0], dice))) == 5 else 0
ONES = lambda dice: 1 * len(list(filter(lambda x: x==1, dice)))
TWOS = lambda dice: 2 * len(list(filter(lambda x: x==2, dice)))
THREES = lambda dice: 3 * len(list(filter(lambda x: x==3, dice)))
FOURS = lambda dice: 4 * len(list(filter(lambda x: x==4, dice)))
FIVES = lambda dice: 5 * len(list(filter(lambda x: x==5, dice)))
SIXES = lambda dice: 6 * len(list(filter(lambda x: x==6, dice)))
FULL_HOUSE = lambda dice: dice[0] + dice[1] + dice[2] + dice[3] + dice[4] if (dice[:2] == [dice[0] for _ in range(2)] and dice[2:5] == [dice[3] for _ in range(3)] and dice[0] != dice[3]) or (dice[:3] == [dice[0] for _ in range(3)] and dice[3:5] == [dice[4] for _ in range(2)] and dice[0] != dice[3]) else 0
FOUR_OF_A_KIND = lambda dice: dice[0] * 4 if dice[:4] == [dice[0] for _ in range(4)] else dice[1] * 4 if dice[1:] == [dice[1] for _ in range(4)] else 0
LITTLE_STRAIGHT = lambda dice: 30 if [1,2,3,4,5] == dice else 0
BIG_STRAIGHT = lambda dice: 30 if [2,3,4,5,6] == dice else 0
CHOICE = lambda dice: dice[0] + dice[1] + dice[2] + dice[3] + dice[4]


def score(dice, category):
    dice.sort()
    return category(dice)
