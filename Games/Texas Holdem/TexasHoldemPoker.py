from tkinter import *
from tkinter import font
from winsound import *
from Card import *
from Player import *
from Configuration import *
import random

class TexasHoldemPoker:
    def __init__(self):
        self.window = Tk()
        self.window.title("Texas Holdem Poker")
        self.window.geometry("800x600")

        self.window.configure(bg="green")
        self.fontstyle = font.Font(self.window, size=24, weight='bold', family='Consolas')
        self.fontstyle2 = font.Font(self.window, size=16, weight='bold', family='Consolas')
        self.setupButton()
        self.setupLabel()

        self.player = Player("player")
        self.dealer = Player("dealer")
        self.community = Player("community")
        self.betMoney = 10
        self.playerMoney = 990
        self.nCardsDealer = 0   # 카드가 놓일 인덱스의 위치
        self.nCardsPlayer = 0
        self.LcardsPlayer = []  # 라벨, 카드 이미지 리스트
        self.LcardsDealer = []
        self.LcardsCommunity = []
        self.deckN = 0  # 섞은 카드의 인덱스 0번 카드부터 카드를 나눈다.
        self.BetCount = 0
        self.DealCount = 0

        self.suitOrder = ['Clubs', 'Hearts', 'Diamonds', 'Spades']

        self.window.mainloop()
    
    def setupButton(self):
        self.Check = Button(self.window,text="Check", width=6,height=1, font=self.fontstyle2,command=self.pressedCheck)
        self.Check.place(x=50,y=500)
        self.Betx1 = Button(self.window,text="Bet x1", width=6,height=1, font=self.fontstyle2,command=self.pressedBetx1)
        self.Betx1.place(x=150,y=500)
        self.Betx2 = Button(self.window,text="Bet x2", width=6,height=1, font=self.fontstyle2,command=self.pressedBx2)
        self.Betx2.place(x=250,y=500)
        
        self.Deal = Button(self.window,text="Deal", width=6,height=1, font=self.fontstyle2,command=self.pressedDeal)
        self.Deal.place(x=600,y=500)
        self.Again = Button(self.window,text="Again", width=6,height=1, font=self.fontstyle2,command=self.pressedAgain)
        self.Again.place(x=700, y=500)

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'
    
    def setupLabel(self):
        self.LbetMoney = Label(text="$10",width=4,height=1,font=self.fontstyle,bg="green",fg="orange")
        self.LbetMoney.place(x=200,y=450)
        self.LplayerMoney = Label(text="You have $990",width=15,height=1,font=self.fontstyle,bg="green",fg="orange")
        self.LplayerMoney.place(x=500,y=450)

        self.LPlayerHands = Label(text="", width=20, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LPlayerHands.place(x=250, y=380)
        self.LDealerHands = Label(text="", width=20, height=1, font=self.fontstyle, bg="green", fg="cyan")
        self.LDealerHands.place(x=250, y=100)
        
        self.Lstatus = Label(text="",width=15,height=1,font=self.fontstyle,bg="green",fg="red")
        self.Lstatus.place(x=500,y=300)
    
    def pressedCheck(self):
        self.checkWinner()
    
    def pressedBetx1(self):
        self.BetCount += 1
        self.betMoney *= 2
        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$"+str(self.betMoney))
            self.playerMoney -= (self.betMoney // 2)
            self.LplayerMoney.configure(text="You have $"+str(self.playerMoney))
            if self.community.inHand() < 5:
                self.Deal["state"] = "active"
                self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 10
    
    def pressedBx2(self):
        self.BetCount += 2
        self.betMoney *= 3
        if self.betMoney <= self.playerMoney:
            self.LbetMoney.configure(text="$"+str(self.betMoney))
            self.playerMoney -= (self.betMoney * 2 // 3)
            self.LplayerMoney.configure(text="You have $"+str(self.playerMoney))
            if self.community.inHand() < 5:
                self.Deal["state"] = "active"
                self.Deal["bg"] = "white"
            PlaySound('sounds/chip.wav', SND_FILENAME)
        else:
            self.betMoney -= 1

    def pressedDeal(self):
        if self.community.inHand() < 5:
            self.deal()
            self.Deal['state'] = 'disable'
            self.Deal['bg'] = 'gray'

    def pressedAgain(self): # 판에 있는 label clear
        self.betMoney = 10
        self.LbetMoney.config(text="$10")
        self.LplayerMoney.config(text="You have $"+str(self.playerMoney-10))
        self.Lstatus.config(text="")

        for i in range(len(self.LcardsPlayer)):
            self.LcardsPlayer[i].config(image='', bg='green')
        for i in range(len(self.LcardsDealer)):
            self.LcardsDealer[i].config(image='', bg='green')
        for i in range(len(self.LcardsCommunity)):
            self.LcardsCommunity[i].config(image='', bg='green')

        self.LcardsPlayer.clear()
        self.LcardsDealer.clear()
        self.LcardsCommunity.clear()

        self.community.reset()
        self.BetCount = 0
        self.DealCount = 0

        self.LPlayerHands['text'] = ""
        self.LDealerHands['text'] = ""
        
        self.Check['state'] = 'disabled'
        self.Check['bg'] = 'gray'
        self.Betx1['state'] = 'active'
        self.Betx1['bg'] = 'white'

        self.Betx2['state'] = 'active'
        self.Betx2['bg'] = 'white'

        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'disabled'
        self.Again['bg'] = 'gray'

    def deal(self):
        if self.DealCount == 0:
            self.player.reset()
            self.dealer.reset()

            # 카드 덱 52장 셔플링 0, 1,, .51
            self.cardDeck = [i for i in range(52)]
            random.shuffle(self.cardDeck)
            self.deckN = 0
            self.hitPlayer(0)   # 0번 위치에 카드 한 장
            self.hitDealer(0)
            self.hitPlayer(1)   # 1번 위치에 카드 한 장
            self.hitDealer(1)

            self.nCardsPlayer = 1
            self.nCardsDealer = 1
            self.DealCount += 1
        elif self.DealCount == 1:   
            for i in range(3):
                self.hitCommunity(i)
                self.DealCount += 1
        else:
            self.hitCommunity(self.deckN-4)
        
        PlaySound('sounds/cardFlip1.wav', SND_FILENAME)
        self.Check['state'] = 'active'
        self.Check['bg'] = 'white'
        self.Betx1['state'] = 'active'
        self.Betx1['bg'] = 'white'
        self.Betx2['state'] = 'active'
        self.Betx2['bg'] = 'white'
    
    def hitCommunity(self, n):
            newCard = Card(self.cardDeck[self.deckN])
            self.deckN += 1
            self.community.addCard(newCard)
            p = PhotoImage(file="cards/"+newCard.filename())
            self.LcardsCommunity.append(Label(self.window, image=p))
            self.LcardsCommunity[self.community.inHand() - 1].image = p
            self.LcardsCommunity[self.community.inHand() - 1].place(x=150+n*80, y=200)
    
    def hitPlayer(self, n): # 카드 추가
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.player.addCard(newCard)
        p = PhotoImage(file="cards/"+newCard.filename())
        self.LcardsPlayer.append(Label(self.window,image=p))
        # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임
        self.LcardsPlayer[self.player.inHand() - 1].image = p
        self.LcardsPlayer[self.player.inHand() - 1].place(x=50+n*80,y=350)
    
    def hitDealer(self, n):
        newCard = Card(self.cardDeck[self.deckN])
        self.deckN += 1
        self.dealer.addCard(newCard)
        p = PhotoImage(file="../../../../Desktop/cards/b2fv.png")
        self.LcardsDealer.append(Label(self.window,image=p))
        self.LcardsDealer[self.player.inHand() - 1].image = p
        self.LcardsDealer[self.player.inHand() - 1].place(x=50+n*80,y=50)

    def checkWinner(self):
        # 뒤집힌 카드를 다시 그린다.
        p = PhotoImage(file="cards/"+self.dealer.cards[0].filename())
        self.LcardsDealer[0].configure(image = p)   # 이미지 레퍼런스 변경
        self.LcardsDealer[0].image=p    # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임

        p = PhotoImage(file="cards/"+self.dealer.cards[1].filename())
        self.LcardsDealer[1].configure(image = p)   # 이미지 레퍼런스 변경
        self.LcardsDealer[1].image=p    # 파이썬은 라벨 이미지 레퍼런스를 갖고 있어야 이미지가 보임

        PlayerCards = self.player.showCards() + self.community.showCards()
        DealerCards = self.dealer.showCards() + self.community.showCards()

        # 족보 계산
        PlayerCards.sort(key=lambda i : i.getvalue())
        DealerCards.sort(key=lambda i : i.getvalue())

        PlayerResult = Configuration.Result(PlayerCards)
        DealerResult = Configuration.Result(DealerCards)

        if(PlayerResult >= ROYAL_STRAIGHT_FLUSH):
            self.LPlayerHands['text'] = 'Royal Straight Flush'
        elif(PlayerResult >= BACK_STRAIGHT_FLUSH):
            self.LPlayerHands['text'] = 'Back Straight Flush'
        elif(PlayerResult >= STRAIGHT_FLUSH):
            self.LPlayerHands['text'] = 'Straight Flush'
        elif(PlayerResult >= FOUR_CARD):
            if PlayerResult - FOUR_CARD == 14:
                self.LPlayerHands['text'] = 'Four card' + '1'
            else:
                self.LPlayerHands['text'] = 'Four card' + str(PlayerResult - FOUR_CARD)
        elif(PlayerResult >= FULLHOUSE):
            self.LPlayerHands['text'] = 'Full House'
        elif(PlayerResult >= FLUSH):
            self.LPlayerHands['text'] = 'Flush'
        elif(PlayerResult >= MOUNTAIN):
            self.LPlayerHands['text'] = 'Mountain'
        elif(PlayerResult >= BACK_STRAIGHT):
            self.LPlayerHands['text'] = 'Back Straight'
        elif(PlayerResult >= STRAIGHT):
            self.LPlayerHands['text'] = 'Straight'
        elif(PlayerResult >= TRIPLE):
            if PlayerResult - TRIPLE == 14:
                self.LPlayerHands['text'] = 'Triple' + '1'
            else:
                self.LPlayerHands['text'] = 'Triple' + str(PlayerResult - TRIPLE)
        elif(PlayerResult >= TWO_PAIR):
            if PlayerResult - TWO_PAIR == 14:
                self.LPlayerHands['text'] = 'Two Pair' + '1'
            else:
                self.LPlayerHands['text'] = 'Two Pair' + str(PlayerResult - TWO_PAIR)
        elif(PlayerResult >= ONE_PAIR):
            if PlayerResult - ONE_PAIR == 14:
                self.LPlayerHands['text'] = 'One Pair' + '1'
            else:
                self.LPlayerHands['text'] = 'One Pair' + str(PlayerResult - ONE_PAIR)
        else:
            if PlayerResult == 14:
                self.LPlayerHands['text'] = 'No Pair' + '1'
            else:
                self.LPlayerHands['text'] = 'No Pair' + str(PlayerResult)

        if(DealerResult >= ROYAL_STRAIGHT_FLUSH):
            self.LDealerHands['text'] = 'Royal Straight Flush'
        elif(DealerResult >= BACK_STRAIGHT_FLUSH):
            self.LDealerHands['text'] = 'Back Straight Flush'
        elif(DealerResult >= STRAIGHT_FLUSH):
            self.LDealerHands['text'] = 'Straight Flush'
        elif(DealerResult >= FOUR_CARD):
            if DealerResult - FOUR_CARD == 14:
                self.LDealerHands['text'] = 'Four card' + '1'
            else:
                self.LDealerHands['text'] = 'Four card' + str(DealerResult - FOUR_CARD)
        elif(DealerResult >= FULLHOUSE):
            self.LDealerHands['text'] = 'Full House'
        elif(DealerResult >= FLUSH):
            self.LDealerHands['text'] = 'Flush'
        elif(DealerResult >= MOUNTAIN):
            self.LDealerHands['text'] = 'Mountain'
        elif(DealerResult >= BACK_STRAIGHT):
            self.LDealerHands['text'] = 'Back Straight'
        elif(DealerResult >= STRAIGHT):
            self.LDealerHands['text'] = 'Straight'
        elif(DealerResult >= TRIPLE):
            if DealerResult - TRIPLE == 14:
                self.LDealerHands['text'] = 'Triple' + '1'
            else:
                self.LDealerHands['text'] = 'Triple' + str(DealerResult - TRIPLE)
        elif(DealerResult >= TWO_PAIR):
            if DealerResult - TWO_PAIR == 14:
                self.LDealerHands['text'] = 'Two Pair' + '1'
            else:
                self.LDealerHands['text'] = 'Two Pair' + str(DealerResult - TWO_PAIR)
        elif(DealerResult >= ONE_PAIR):
            if DealerResult - ONE_PAIR == 14:
                self.LDealerHands['text'] = 'One Pair' + '1'
            else:
                self.LDealerHands['text'] = 'One Pair' + str(DealerResult - ONE_PAIR)
        else:
            if DealerResult == 14:
                self.LDealerHands['text'] = 'No Pair' + '1'
            else:
                self.LDealerHands['text'] = 'No Pair' + str(DealerResult)
        
        print('PlayerResult: ', PlayerResult)
        print('DealerResult: ', DealerResult)

        for i in range(len(PlayerCards)):
            print(PlayerCards[i].getvalue(), end=' ')
        print()
        for i in range(len(DealerCards)):
            print(DealerCards[i].getvalue(), end=' ')
        print()

        if PlayerResult > DealerResult:
            self.Lstatus['text'] = 'Win'
            self.playerMoney += self.betMoney*(self.BetCount-1)
        elif PlayerResult == DealerResult:
            self.Lstatus['text'] = 'Push'
            self.playerMoney += self.betMoney
        else:
            self.Lstatus['text'] = 'Lose'

        self.betMoney= 0
        self.LplayerMoney.configure(text="Youhave$"+str(self.playerMoney))
        self.LbetMoney.configure(text="$"+str(self.betMoney))

        self.Check['state'] = 'disabled'
        self.Check['bg'] = 'gray'
        self.Betx1['state'] = 'disabled'
        self.Betx1['bg'] = 'gray'
        self.Betx2['state'] = 'disabled'
        self.Betx2['bg'] = 'gray'
        
        self.Deal['state'] = 'disabled'
        self.Deal['bg'] = 'gray'
        self.Again['state'] = 'active'
        self.Again['bg'] = 'white'

TexasHoldemPoker()