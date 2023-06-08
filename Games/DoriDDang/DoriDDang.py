from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import *
from Configuration import *
import random

class DoriDDang:
    def __init__(self):
        self.window = Tk()
        self.window.title("도리짓고땡")
        self.window.geometry("800x600")

        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='맑은 고딕')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='맑은 고딕')
        self.fontstyle3 = font.Font(self.window, size=12, weight='bold', family='맑은 고딕')
        self.setupButton()
        self.setupLabel()

        self.player1 = Player("player1")
        self.player2 = Player("player2")
        self.player3 = Player("player3")
        self.dealer = Player("dealer")
        
        self.betMoney1 = 0
        self.betMoney2 = 0
        self.betMoney3 = 0
        self.playerMoney = 1000
        self.nCardsDealer = 0   # 카드가 놓일 인덱스의 위치
        self.nCardsPlayer1 = 0
        self.nCardsPlayer2 = 0
        self.nCardsPlayer3 = 0
        self.LcardsPlayer1 = []  # 라벨, 카드 이미지 리스트
        self.LcardsPlayer2 = []
        self.LcardsPlayer3 = []
        self.LcardsDealer = []
        
        self.deckN = 0  # 섞은 카드의 인덱스 0번 카드부터 카드를 나눈다.
        self.BetCount = 0
        self.DealCount = 0

        self.window.mainloop()
    
    def setupButton(self):
        self.Bet5_1 = Button(self.window,text="5만", width=4,height=1, font=self.fontstyle2, command=self.pressedBet5_1)
        self.Bet5_1.place(x=30,y=530)
        self.Bet1_1 = Button(self.window,text="1만", width=4,height=1, font=self.fontstyle2, command=self.pressedBet1_1)
        self.Bet1_1.place(x=110,y=530)

        self.Bet5_2 = Button(self.window,text="5만", width=4,height=1, font=self.fontstyle2, command=self.pressedBet5_2)
        self.Bet5_2.place(x=230,y=530)
        self.Bet1_2 = Button(self.window,text="1만", width=4,height=1, font=self.fontstyle2, command=self.pressedBet1_2)
        self.Bet1_2.place(x=310,y=530)
        
        self.Bet5_3 = Button(self.window,text="5만", width=4,height=1, font=self.fontstyle2, command=self.pressedBet5_3)
        self.Bet5_3.place(x=430,y=530)
        self.Bet1_3 = Button(self.window,text="1만", width=4,height=1, font=self.fontstyle2, command=self.pressedBet1_3)
        self.Bet1_3.place(x=510,y=530)

        self.Deal = Button(self.window,text="Deal", width=5,height=1, font=self.fontstyle2,command=self.pressedDeal)
        self.Deal.place(x=610,y=530)
        self.Again = Button(self.window,text="Again", width=5,height=1, font=self.fontstyle2,command=self.pressedAgain)
        self.Again.place(x=710, y=530)

        self.Bet5_1['state'] = 'disabled'
        self.Bet5_1['bg'] = 'gray'
        self.Bet1_1['state'] = 'disabled'
        self.Bet1_1['bg'] = 'gray'

        self.Bet5_2['state'] = 'disabled'
        self.Bet5_2['bg'] = 'gray'
        self.Bet1_2['state'] = 'disabled'
        self.Bet1_2['bg'] = 'gray'

        self.Bet5_3['state'] = 'disabled'
        self.Bet5_3['bg'] = 'gray'
        self.Bet1_3['state'] = 'disabled'
        self.Bet1_3['bg'] = 'gray'

        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'
    
    def setupLabel(self):
        self.LbetMoney1 = Label(text="0만",width=4,height=1,font=self.fontstyle,bg="green",fg="cyan")
        self.LbetMoney1.place(x=70,y=470)
        self.LbetMoney2 = Label(text="0만",width=4,height=1,font=self.fontstyle,bg="green",fg="cyan")
        self.LbetMoney2.place(x=270,y=470)
        self.LbetMoney3 = Label(text="0만",width=4,height=1,font=self.fontstyle,bg="green",fg="cyan")
        self.LbetMoney3.place(x=470,y=470)

        self.LplayerMoney = Label(text="1000만",width=15,height=1,font=self.fontstyle,bg="green",fg="blue")
        self.LplayerMoney.place(x=560,y=470)

        self.LPlayer1Hands = Label(text="", width=20, height=1, font=self.fontstyle3, bg="green", fg="cyan")
        self.LPlayer1Hands.place(x=40, y=265)
        self.LPlayer2Hands = Label(text="", width=20, height=1, font=self.fontstyle3, bg="green", fg="cyan")
        self.LPlayer2Hands.place(x=240, y=265)
        self.LPlayer3Hands = Label(text="", width=20, height=1, font=self.fontstyle3, bg="green", fg="cyan")
        self.LPlayer3Hands.place(x=440, y=265)

        self.LDealerHands = Label(text="", width=20, height=1, font=self.fontstyle3, bg="green", fg="cyan")
        self.LDealerHands.place(x=240, y=20)
        
        self.Lstatus1 = Label(text="",width=15,height=1,font=self.fontstyle2,bg="green",fg="red")
        self.Lstatus1.place(x=40,y=225)
        self.Lstatus2 = Label(text="",width=15,height=1,font=self.fontstyle2,bg="green",fg="red")
        self.Lstatus2.place(x=240,y=225)
        self.Lstatus3 = Label(text="",width=15,height=1,font=self.fontstyle2,bg="green",fg="red")
        self.Lstatus3.place(x=440,y=225)

        self.LcardsNumPlayer1 = []
        self.LcardsNumPlayer2 = []
        self.LcardsNumPlayer3 = []
        self.LcardsNumDealer = []

        for _ in range(5):  # 카드 value 출력할 라벨
            self.LcardsNumPlayer1.append(Label(text="", width=2, height=1, font=self.fontstyle3, bg="green", fg="white"))
            self.LcardsNumPlayer2.append(Label(text="", width=2, height=1, font=self.fontstyle3, bg="green", fg="white"))
            self.LcardsNumPlayer3.append(Label(text="", width=2, height=1, font=self.fontstyle3, bg="green", fg="white"))
            self.LcardsNumDealer.append(Label(text="", width=2, height=1, font=self.fontstyle3, bg="green", fg="white"))
           
    def pressedBet5_1(self):
        self.betMoney1 += 5
        if self.betMoney1 <= self.playerMoney:
            self.LbetMoney1.configure(text=str(self.betMoney1)+'만')
            self.playerMoney -= self.betMoney1
            self.LplayerMoney.configure(text=str(self.playerMoney)+'만')

            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney1 -= 5
        
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'
    
    def pressedBet1_1(self):
        self.betMoney1 += 1
        if self.betMoney1 <= self.playerMoney:
            self.LbetMoney1.configure(text=str(self.betMoney1)+'만')
            self.playerMoney -= self.betMoney1
            self.LplayerMoney.configure(text=str(self.playerMoney)+'만')

            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney1 -= 1
        
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'

    def pressedBet5_2(self):
        self.betMoney2 += 5
        if self.betMoney2 <= self.playerMoney:
            self.LbetMoney2.configure(text=str(self.betMoney2)+'만')
            self.playerMoney -= self.betMoney2
            self.LplayerMoney.configure(text=str(self.playerMoney)+'만')

            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney2 -= 5
        
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'
    
    def pressedBet1_2(self):
        self.betMoney2 += 1
        if self.betMoney2 <= self.playerMoney:
            self.LbetMoney2.configure(text=str(self.betMoney2)+'만')
            self.playerMoney -= self.betMoney2
            self.LplayerMoney.configure(text=str(self.playerMoney)+'만')

            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney2 -= 1
        
        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'
    
    def pressedBet5_3(self):
        self.betMoney3 += 5
        if self.betMoney3 <= self.playerMoney:
            self.LbetMoney3.configure(text=str(self.betMoney3)+'만')
            self.playerMoney -= self.betMoney3
            self.LplayerMoney.configure(text=str(self.playerMoney)+'만')

            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney3 -= 5

        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'
    
    def pressedBet1_3(self):
        self.betMoney3 += 1
        if self.betMoney3 <= self.playerMoney:
            self.LbetMoney3.configure(text=str(self.betMoney3)+'만')
            self.playerMoney -= self.betMoney3
            self.LplayerMoney.configure(text=str(self.playerMoney)+'만')

            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney3 -= 1

        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'

    def pressedDeal(self):
        if self.DealCount < 5:
            self.deal()

    def pressedAgain(self): # 판에 있는 label clear
        self.betMoney1 = 0
        self.LbetMoney1.config(text="0만")
        self.betMoney2 = 0
        self.LbetMoney2.config(text="0만")
        self.betMoney3 = 0
        self.LbetMoney3.config(text="0만")

        self.LplayerMoney.config(text=str(self.playerMoney)+'만')

        self.Lstatus1.config(text="")
        self.Lstatus2.config(text="")
        self.Lstatus3.config(text="")

        for i in range(len(self.LcardsPlayer1)):
            self.LcardsPlayer1[i].config(image='', bg='green')
        for i in range(len(self.LcardsPlayer2)):
            self.LcardsPlayer2[i].config(image='', bg='green')
        for i in range(len(self.LcardsPlayer3)):
            self.LcardsPlayer3[i].config(image='', bg='green')

        for i in range(len(self.LcardsDealer)):
            self.LcardsDealer[i].config(image='', bg='green')

        self.LcardsPlayer1.clear()
        self.LcardsPlayer2.clear()
        self.LcardsPlayer3.clear()
        self.LcardsDealer.clear()

        self.DealCount = 0

        self.LPlayer1Hands['text'] = ""
        self.LPlayer2Hands['text'] = ""
        self.LPlayer3Hands['text'] = ""
        self.LDealerHands['text'] = ""

        for i in range(5):
            self.LcardsNumPlayer1[i]['text'] = ""
            self.LcardsNumPlayer1[i]['fg'] = 'white'
            self.LcardsNumPlayer2[i]['text'] = ""
            self.LcardsNumPlayer2[i]['fg'] = 'white'
            self.LcardsNumPlayer3[i]['text'] = ""
            self.LcardsNumPlayer3[i]['fg'] = 'white'
            self.LcardsNumDealer[i]['text'] = ""
            self.LcardsNumDealer[i]['fg'] = 'white'
        
        self.Bet5_1['state'] = 'disabled'
        self.Bet5_1['bg'] = 'gray'
        self.Bet1_1['state'] = 'disabled'
        self.Bet1_1['bg'] = 'gray'

        self.Bet5_2['state'] = 'disabled'
        self.Bet5_2['bg'] = 'gray'
        self.Bet1_2['state'] = 'disabled'
        self.Bet1_2['bg'] = 'gray'

        self.Bet5_3['state'] = 'disabled'
        self.Bet5_3['bg'] = 'gray'
        self.Bet1_3['state'] = 'disabled'
        self.Bet1_3['bg'] = 'gray'

        self.Deal['state'] = 'active'
        self.Deal['bg'] = 'white'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def deal(self):
        if self.DealCount == 0:
            self.player1.reset()
            self.player2.reset()
            self.player3.reset()
            self.dealer.reset()

            # 카드 덱 40장 셔플링 0, 1,, .39
            self.cardDeck = [i for i in range(40)]
            random.shuffle(self.cardDeck)
            self.deckN = 0
            self.hitPlayer(0)   # 0번 위치에 카드 한 장
            self.hitDealer(0)

            self.DealCount += 1
        elif self.DealCount == 1:   
            for i in range(1, 4):
                self.hitPlayer(i)
                self.hitDealer(i)
                self.DealCount += 1
        elif self.DealCount == 4:
            self.hitPlayer(self.DealCount)
            self.hitDealer(self.DealCount)
            self.DealCount += 1

            self.checkWinner()
        
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)
        self.Bet5_1['state'] = 'active'
        self.Bet5_1['bg'] = 'white'
        self.Bet1_1['state'] = 'active'
        self.Bet1_1['bg'] = 'white'

        self.Bet5_2['state'] = 'active'
        self.Bet5_2['bg'] = 'white'
        self.Bet1_2['state'] = 'active'
        self.Bet1_2['bg'] = 'white'

        self.Bet5_3['state'] = 'active'
        self.Bet5_3['bg'] = 'white'
        self.Bet1_3['state'] = 'active'
        self.Bet1_3['bg'] = 'white'

        self.Deal['state'] = 'disable'
        self.Deal['bg'] = 'gray'
    
    def hitPlayer(self, n): # 카드 추가
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player1.addCard(newCard)
        p = PhotoImage(file="GodoriCards/"+newCard.filename())
        self.LcardsPlayer1.append(Label(self.window,image=p))
        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer1[self.player1.inHand() - 1].image = p
        self.LcardsPlayer1[self.player1.inHand() - 1].place(x=30+n*30,y=350)
        self.LcardsNumPlayer1[self.player1.inHand() - 1]['text'] = newCard.getsuit()
        self.LcardsNumPlayer1[self.player1.inHand() - 1].place(x=50+n*30, y=320)

        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player2.addCard(newCard)
        p = PhotoImage(file="GodoriCards/"+newCard.filename())
        self.LcardsPlayer2.append(Label(self.window,image=p))
        self.LcardsPlayer2[self.player2.inHand() - 1].image = p
        self.LcardsPlayer2[self.player2.inHand() - 1].place(x=230+n*30,y=350)
        self.LcardsNumPlayer2[self.player2.inHand() - 1]['text'] = newCard.getsuit()
        self.LcardsNumPlayer2[self.player2.inHand() - 1].place(x=250+n*30, y=320)

        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player3.addCard(newCard)
        p = PhotoImage(file="GodoriCards/"+newCard.filename())
        self.LcardsPlayer3.append(Label(self.window,image=p))
        self.LcardsPlayer3[self.player3.inHand() - 1].image = p
        self.LcardsPlayer3[self.player3.inHand() - 1].place(x=430+n*30,y=350)
        self.LcardsNumPlayer3[self.player3.inHand() - 1]['text'] = newCard.getsuit()
        self.LcardsNumPlayer3[self.player3.inHand() - 1].place(x=450+n*30, y=320)
    
    def hitDealer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file="GodoriCards/cardback.gif")
        self.LcardsDealer.append(Label(self.window,image=p))
        self.LcardsDealer[self.player1.inHand() - 1].image = p
        self.LcardsDealer[self.player1.inHand() - 1].place(x=230+n*30,y=100)

    def checkWinner(self):
        # 뒤집힌 카드를 다시 그린다.
        for i in range(5):
            p = PhotoImage(file="GodoriCards/"+self.dealer.cards[i].filename())
            self.LcardsDealer[i].configure(image = p)   # 이미지 레퍼런스 변경
            self.LcardsDealer[i].image=p    # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
            self.LcardsNumDealer[i]['text'] = self.dealer.cards[i].getsuit()
            self.LcardsNumDealer[i].place(x=250+i*30, y=70)

        Player1Cards = self.player1.showCards()
        Player2Cards = self.player2.showCards()
        Player3Cards = self.player3.showCards()
        DealerCards = self.dealer.showCards()

        resultStrs = []    # 0: 1번 플레이어, 1: 2번 플레이어, 2: 3번 플레이어, 3: 딜러
        resultScores = []    # 0: 1번 플레이어, 1: 2번 플레이어, 2: 3번 플레이어, 3: 딜러
        resultMadeIndex = []

        player1result = Configuration.result(Player1Cards)
        player2result = Configuration.result(Player2Cards)
        player3result = Configuration.result(Player3Cards)
        dealerresult = Configuration.result(DealerCards)

        resultStrs.append(player1result[0])
        resultStrs.append(player2result[0])
        resultStrs.append(player3result[0])
        resultStrs.append(dealerresult[0])

        resultScores.append(player1result[1])
        resultScores.append(player2result[1])
        resultScores.append(player3result[1])
        resultScores.append(dealerresult[1])

        resultMadeIndex.append(player1result[2])
        resultMadeIndex.append(player2result[2])
        resultMadeIndex.append(player3result[2])
        resultMadeIndex.append(dealerresult[2])

        self.LPlayer1Hands['text'] = resultStrs[0]
        self.LPlayer2Hands['text'] = resultStrs[1]
        self.LPlayer3Hands['text'] = resultStrs[2]
        self.LDealerHands['text'] = resultStrs[3]

        print(resultScores)

        for i in range(5):
            if i in resultMadeIndex[0]:
                self.LcardsPlayer1[i].place(x=30 + i * 30, y=340)
                self.LcardsNumPlayer1[i].place(x=50+i*30, y=310)
                self.LcardsNumPlayer1[i]['fg'] = 'orange'
            else:
                self.LcardsPlayer1[i].place(x=30 + i * 30, y=350)
                self.LcardsNumPlayer1[i].place(x=50+i*30, y=320)

        for i in range(5):
            if i in resultMadeIndex[1]:
                self.LcardsPlayer2[i].place(x=230 + i * 30, y=340)
                self.LcardsNumPlayer2[i].place(x=250+i*30, y=310)
                self.LcardsNumPlayer2[i]['fg'] = 'orange'
            else:
                self.LcardsPlayer2[i].place(x=230 + i * 30, y=350)
                self.LcardsNumPlayer2[i].place(x=250+i*30, y=320)

        for i in range(5):
            if i in resultMadeIndex[2]:
                self.LcardsPlayer3[i].place(x=430 + i * 30, y=340)
                self.LcardsNumPlayer3[i].place(x=450+i*30, y=310)
                self.LcardsNumPlayer3[i]['fg'] = 'orange'
            else:
                self.LcardsPlayer3[i].place(x=430 + i * 30, y=350)
                self.LcardsNumPlayer3[i].place(x=450+i*30, y=320)

        for i in range(5):
            if i in resultMadeIndex[3]:
                self.LcardsDealer[i].place(x=230+i*30, y=90)
                self.LcardsNumDealer[i].place(x=250+i*30, y=60)
                self.LcardsNumDealer[i]['fg'] = 'orange'
            else:
                self.LcardsDealer[i].place(x=230+i*30, y=100)
                self.LcardsNumDealer[i].place(x=250+i*30, y=70)

        if resultScores[0] > resultScores[3]:
            self.Lstatus1['text'] = '승'
            self.playerMoney += self.betMoney1*2
        else:
            self.Lstatus1['text'] = '패'
        
        if resultScores[1] > resultScores[3]:
            self.Lstatus2['text'] = '승'
            self.playerMoney += self.betMoney2*2
        else:
            self.Lstatus2['text'] = '패'
        
        if resultScores[2] > resultScores[3]:
            self.Lstatus3['text'] = '승'
            self.playerMoney += self.betMoney3*2
        else:
            self.Lstatus3['text'] = '패'

        if resultScores[3] == max(resultScores):
            PlaySound('sounds/wrong.wav', SND_FILENAME)
        else:
            PlaySound('sounds/win.wav', SND_FILENAME)

        self.betMoney1= 0
        self.betMoney2= 0
        self.betMoney3= 0
        self.LplayerMoney.configure(text=str(self.playerMoney)+'만')
        self.LbetMoney1.configure(text=str(self.betMoney1)+'만')
        self.LbetMoney2.configure(text=str(self.betMoney2)+'만')
        self.LbetMoney3.configure(text=str(self.betMoney3)+'만')

        self.Bet5_1['state'] = 'disabled'
        self.Bet5_1['bg'] = 'gray'
        self.Bet1_1['state'] = 'disabled'
        self.Bet1_1['bg'] = 'gray'

        self.Bet5_2['state'] = 'disabled'
        self.Bet5_2['bg'] = 'gray'
        self.Bet1_2['state'] = 'disabled'
        self.Bet1_2['bg'] = 'gray'

        self.Bet5_3['state'] = 'disabled'
        self.Bet5_3['bg'] = 'gray'
        self.Bet1_3['state'] = 'disabled'
        self.Bet1_3['bg'] = 'gray'
        
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'

DoriDDang()