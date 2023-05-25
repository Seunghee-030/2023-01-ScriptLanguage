from Card import *

ROYAL_STRAIGHT_FLUSH = 50000
BACK_STRAIGHT_FLUSH = 40000
STRAIGHT_FLUSH = 30000
FOUR_CARD = 20000
FULLHOUSE = 10000
FLUSH = 8000
MOUNTAIN = 7000
BACK_STRAIGHT = 6000
STRAIGHT = 5000
TRIPLE = 3000
TWO_PAIR = 2000
ONE_PAIR = 1000
NO_PAIR = 0

class Configuration:
    def Result(c):
        if Configuration.is_RoyalStraightFlush(c):
            return ROYAL_STRAIGHT_FLUSH
        
        if Configuration.is_BackStraightFlush(c):
            return BACK_STRAIGHT_FLUSH
        
        if Configuration.is_StraightFlush(c):
            return STRAIGHT_FLUSH
        
        FourcardScore = Configuration.is_FourCard(c)
        if FourcardScore:
            return FOUR_CARD + FourcardScore
        
        if Configuration.is_Fullhouse(c):
            return FULLHOUSE
        
        if len(Configuration.is_Flush(c)) == 5:
            return FLUSH
        
        if Configuration.is_Mountain(c):
            return MOUNTAIN
        
        if Configuration.is_BackStraight(c):
            return BACK_STRAIGHT

        if Configuration.is_Straight(c):
            return STRAIGHT
        
        TripleScore = Configuration.is_Triple(c)
        if TripleScore:
            return TRIPLE + TripleScore

        TwoPairScore = Configuration.is_TwoPair(c)
        if TwoPairScore:
            return TWO_PAIR + TwoPairScore
        
        OnePairScore = Configuration.is_OnePair(c)
        if OnePairScore:
            return ONE_PAIR + OnePairScore
        
        return NO_PAIR + max(c, key=lambda i : i.getvalue()).getvalue()

    def is_RoyalStraightFlush(c):
        FlushCards = Configuration.is_Flush(c)
        if len(FlushCards) >= 5:
            if Configuration.is_Mountain(FlushCards):
                return True
        return False

    def is_BackStraightFlush(c):
        FlushCards = Configuration.is_Flush(c)
        if len(FlushCards) >= 5:
            if Configuration.is_BackStraight(FlushCards):
                return True
        return False

    def is_StraightFlush(c):
        FlushCards = Configuration.is_Flush(c)
        if len(FlushCards) >= 5:
            if Configuration.is_Straight(FlushCards):
                return True
        return False
    
    def is_FourCard(c):
        for i in range(len(c)-3):
            if c[i].getvalue() == c[i+1].getvalue() and c[i].getvalue() == c[i+2].getvalue() and c[i].getvalue() == c[i+3].getvalue():
                return c[i].getvalue()
        return False

    def is_Fullhouse(c):
        countCard = []
        for i in range(2, 15, 1):
            countCard.append(len(list(filter(lambda x : c[x].getvalue() == i, range(len(c))))))
        
        if countCard.count(2) == 1 and countCard.count(3) == 1:
            FHList = list(filter(lambda x : countCard[x] == 2, range(len(countCard))))
            return max(FHList) + 2
        return False

    def is_Flush(c):
        FlushCards = []
        for i in range(4):
            if len(list(filter(lambda x : c[x].getsuitnum() == i, range(len(c))))) >= 5:
                sameSuit = list(filter(lambda x : c[x].getsuitnum() == i, range(len(c))))
                print(len(sameSuit))
                for j in range(len(sameSuit)):
                    FlushCards.append(c[sameSuit[j]])
                return FlushCards
        return FlushCards

    def is_Mountain(c):
        times = 0
        if c[len(c)-1].getvalue() == 14:
            for i in range(10, 14, 1):
                if len(list(filter(lambda x : c[x].getvalue() == i, range(len(c))))) >= 1:
                    times += 1
        if times >= 4:
            return True
        return False

    def is_BackStraight(c):
        times = 0
        if c[len(c)-1].getvalue() == 14:
            for i in range(0, 4, 1):
                if len(list(filter(lambda x : c[x].getvalue() == i + 2, range(len(c))))) >= 1:
                    times += 1
        if times >= 4:
            return True
        return False
    
    def is_Straight(c):
        cardsNum = []
        for i in range(len(c)):
            if c[i].getvalue() == 14:
                cardsNum.append(1)
            else:
                cardsNum.append(c[i].getvalue())
        cardsNum.sort()
        times = 0
        for i in range(len(cardsNum) - 1):
            if cardsNum[i] + 1 == cardsNum[i + 1]:
                times += 1
            elif cardsNum[i] == cardsNum[i + 1]:
                continue
            else:
                times = 0
            
            if times >= 4:
                return True

        return False

    def is_Triple(c):
        for i in range(len(c)-2):
            if c[i].getvalue() == c[i+1].getvalue() and c[i].getvalue() == c[i+2].getvalue():
                return c[i].getvalue()
        return False

    def is_TwoPair(c):
        countCard = []
        for i in range(2, 15, 1):
            countCard.append(len(list(filter(lambda x : c[x].getvalue() == i, range(len(c))))))
        
        if countCard.count(2) >= 2:
            twoList = list(filter(lambda x : countCard[x] == 2, range(len(countCard))))
            return max(twoList) + 2
        return False

    def is_OnePair(c):
        for i in range(len(c)-1):
            if c[i].getvalue() == c[i+1].getvalue():
                return c[i].getvalue()
        return False 