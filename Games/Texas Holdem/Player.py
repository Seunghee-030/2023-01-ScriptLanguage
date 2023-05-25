class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.N = 0
    
    def inHand(self):
        return self.N
    
    def addCard(self, c):
        self.cards.append(c)
        self.N += 1
    
    def reset(self):
        self.N = 0
        self.cards.clear()
    
    def value(self):
        sum = 0
        for i in range(len(self.cards)):
            if self.cards[i].getValue() == 1:
                sum += 11
            else: sum += self.cards[i].getValue()

        return sum
    
    def showCards(self):
        return self.cards