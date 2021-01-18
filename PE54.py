alphabet = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

HIGH_CARD = 0
ONE_PAIR = 1
TWO_PAIRS = 2
THREE_OF_A_KIND = 3
STRAIGHT = 4
FLUSH = 5
FULL_HOUSE = 6
FOUR_OF_A_KIND = 7
STRAIGHT_FLUSH = 8
ROYAL_FLUSH = 9


def getFrequencies(hand):
    frequencies = {}
    for card in hand:
        num = card[0]
        if num not in frequencies:
            frequencies[num] = 1
        else:
            frequencies[num] += 1
    return frequencies


# High Card: Highest value card.
# One Pair: Two cards of the same value. - Done
# Two Pairs: Two different pairs. - Done
# Three of a Kind: Three cards of the same value. - Done
# Straight: All cards are consecutive values. - Done
# Flush: All cards of the same suit. - Done
# Full House: Three of a kind and a pair. - Done
# Four of a Kind: Four cards of the same value. - Done
# Straight Flush: All cards are consecutive values of same suit. - Done
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
def getType(hand):
    hand = sortCards(hand)
    frequencies = getFrequencies(hand)
    print(frequencies)

    # get pairs
    numberOfPairs = 0
    hasThreeOfAKind = False
    hasFourOfAKind = False

    pairValue = 0
    threeValue = 0
    fourValue = 0

    for k, frequency in frequencies.items():
        if frequency == 2:
            numberOfPairs += 1
            if alphabet.index(k[0]) > pairValue:
                pairValue = alphabet.index(k[0])
        elif frequency == 3:
            hasThreeOfAKind = True
            threeValue = alphabet.index(k[0])
        elif frequency == 4:
            hasFourOfAKind = True
            fourValue = alphabet.index(k[0])

    hasAPair = numberOfPairs >= 1
    hasTwoPairs = numberOfPairs == 2

    # straight
    isStraight = True
    lastVal = hand[0][0]
    for index in range(1, len(hand)):
        if alphabet.index(hand[index][0]) - alphabet.index(lastVal) != 1:
            isStraight = False
            break
        lastVal = hand[index][0]

    # Flush
    isFlush = True
    suit = hand[0][1]
    for index in range(1, len(hand)):
        if hand[index][1] != suit:
            isFlush = False
            break

    isFullHouse = numberOfPairs == 1 and hasThreeOfAKind
    isStraightFlush = isStraight and isFlush
    isRoyalFlush = isStraightFlush and hand[0][0] == "T"

    type = 0
    value = None
    if isRoyalFlush:
        type = ROYAL_FLUSH
    elif isStraightFlush:
        type = STRAIGHT_FLUSH
        value = alphabet.index(hand[-1][0])
    elif hasFourOfAKind:
        type = FOUR_OF_A_KIND
        value = fourValue
    elif isFullHouse:
        type = FULL_HOUSE
        value = threeValue
    elif isFlush:
        type = FLUSH
        value = alphabet.index(hand[-1][0])
    elif isStraight:
        type = STRAIGHT
        value = alphabet.index(hand[-1][0])
    elif hasThreeOfAKind:
        type = THREE_OF_A_KIND
        value = threeValue
    elif hasTwoPairs:
        type = TWO_PAIRS
        value = pairValue
    elif hasAPair:
        type = ONE_PAIR
        value = pairValue
    else:
        type = HIGH_CARD
        value = alphabet.index(hand[-1][0])
    return type, value


def sortCards(hand):
    return sorted(hand, key=lambda x: alphabet.index(x[0]))


# 376
if __name__ == '__main__':
    with open("p054_poker.txt", "r") as f:
        lines = f.readlines()

    games = []
    for line in lines:
        cards = line.split(" ")
        game = [[], []]
        for card in cards[:5]:
            game[0].append(card)
        for card in cards[5:]:
            game[1].append(card.replace("\n", ""))

        games.append(game)

    counter = 0

    for game in games:
        hand1 = sortCards(game[0])
        hand2 = sortCards(game[1])

        hand1Type, value1 = getType(hand1)
        hand2Type, value2 = getType(hand2)

        if hand1Type > hand2Type:
            counter += 1
        elif hand1Type == hand2Type:
            if value1 > value2:
                counter += 1
            elif value1 == value2:
                for index in range(len(hand1))[::-1]:
                    value1 = alphabet.index(hand1[index][0])
                    value2 = alphabet.index(hand2[index][0])

                    if value1 > value2:
                        counter += 1
                        break
                    elif value2 > value1:
                        break
    print(counter)
