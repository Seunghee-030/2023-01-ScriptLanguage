class Card:
    def __init__(self, temp): # 렌덤넘버 0..40 값을 입력받아서 카드 객체 생성
        self.value = temp % 4 + 1 # 1..4
        self.x = temp // 4 + 1 #1..10 suit 결정
        
    def getvalue(self):
        return self.value
    
    def getsuit(self):  # 카드 무늬 결정
        return self.x

    def filename(self): # 카드 이미지 파일 이름
        return str(self.x)+'.'+str(self.value)+".gif"