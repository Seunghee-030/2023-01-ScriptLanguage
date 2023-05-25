class Card:
    def __init__(self, temp): # 렌덤넘버 0..51 값을 입력받아서 카드 객체 생성
        self.value = temp%13 +1 # 1..13
        self.x = temp//13 #0..3 카드무늬 suit 결정
        
    def getvalue(self):
        if self.value == 1:
            return 14   # Ace
        return self.value
    
    def getsuit(self):  # 카드 무늬 결정
        if self.x == 0:
            self.suit = "Clubs"
        elif self.x == 1:
            self.suit = "Spades"
        elif self.x == 2:
            self.suit = "Hearts"
        else:
            self.suit = "Diamonds"
        return self.suit
    
    def getsuitnum(self):
        return self.x

    def filename(self): # 카드 이미지 파일 이름
        return self.getsuit()+str(self.value)+".png"
