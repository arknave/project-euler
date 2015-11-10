# constants for hand
STRAIGHTFLUSH = 8
FOURKIND = 7
FULLHOUSE = 6
FLUSH = 5
STRAIGHT = 4
THREEKIND = 3
TWOPAIR = 2
ONEPAIR = 1
HIGHCARD = 0

def parse(card):
    # return a tuple of number, then suit
    suits = ['C', 'H', 'D', 'S']
    card_num = ['T', 'J', 'Q', 'K', 'A']
    if card[0] in card_num:
        num = card_num.index(card[0]) + 10
    else:
        num = ord(card[0]) - ord('0')

    return (num, suits.index(card[1]))

def score(hand):
    suit_count = [0] * 4
    for card in hand:
        suit = card[1]
        suit_count[suit] += 1

    flush = False
    for count in suit_count:
        if count == 5:
            flush = True

    num_count = [[], [], [], [], [], []]
    for num in range(14, 1, -1):
        f = 0
        for card in hand:
            if card[0] == num:
                f += 1
        if f > 0:
            num_count[f].append(num)

    straight = False
    if len(num_count[1]) == 5:
        this_straight = True
        for i in range(1, 5):
            this_straight &= num_count[1][i] == num_count[1][i - 1] - 1
        straight |= this_straight

    hand_type = 0
    tiebreaker = []
    # check for all of the different hands in order.
    if straight and flush:
        hand_type = STRAIGHTFLUSH
        tiebreaker.append(num_count[1][0])
    elif len(num_count[4]) != 0:
        hand_type = FOURKIND
        tiebreaker.append(num_count[4][0])
        tiebreaker.append(num_count[1][0])
    elif len(num_count[3]) == 1 and len(num_count[2]) == 1:
        hand_type = FULLHOUSE
        tiebreaker.append(num_count[3][0])
        tiebreaker.append(num_count[2][0])
    elif flush:
        hand_type = FLUSH
        for i in xrange(5):
            tiebreaker.append(num_count[1][i])
    elif straight:
        hand_type = STRAIGHT
        for i in xrange(5):
            tiebreaker.append(num_count[1][i])
    elif len(num_count[3]) == 1:
        hand_type = THREEKIND
        tiebreaker.append(num_count[3][0])
        tiebreaker.append(num_count[1][0])
        tiebreaker.append(num_count[1][1])
    elif len(num_count[2]) == 2:
        hand_type = TWOPAIR
        tiebreaker.append(num_count[2][0])
        tiebreaker.append(num_count[2][1])
        tiebreaker.append(num_count[1][0])
    elif len(num_count[2]) == 1:
        hand_type = ONEPAIR
        tiebreaker.append(num_count[2][0])
        for i in xrange(3):
            tiebreaker.append(num_count[1][i])
    else:
        for card in num_count[1]:
            tiebreaker.append(card)

    return (hand_type, tiebreaker)


def win(hand):
    hand1 = sorted([parse(card) for card in hand[:5]])
    hand2 = sorted([parse(card) for card in hand[5:]])

    t1, t2 = score(hand1), score(hand2)
    return t1 > t2

def main():
    fin = open('../data_files/p054_poker.txt', 'r')
    ans = 0

    for line in fin:
        if win(line.split()):
            ans += 1

    fin.close()
    print ans
if __name__ == '__main__':
    main()
