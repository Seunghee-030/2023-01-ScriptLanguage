from Card import *

DAN1 = 90000
DAN2 = 80000
DAN3 = 70000
DAN4 = 60000
DAN5 = 50000
DAN6 = 40000
DAN7 = 30000
DAN8 = 20000
DAN9 = 10000
NO_MADE = 0

GDD38 = 9000
GDD = 8000
DD10 = 1000
DD9 = 900
DD8 = 800
DD7 = 700
DD6 = 600
DD5 = 500
DD4 = 400
DD3 = 300
DD2 = 200
DD1 = 100

MANGTONG = 0

class Configuration:
    def result(c):
        rStr = ''
        rScore = 0

        CardSuitList = []   # 1~10
        madeNum = []
        madeNumIndex = []
        rList = []

        JaturiCardList = CardSuitList

        for i in range(5):
            CardSuitList.append(c[i].getsuit())

        if CardSuitList.count(1) >= 2 and CardSuitList.count(8) >= 1:
            for i in range(CardSuitList.count(1)):
                madeNumIndex.append(CardSuitList.index(1, i))
            madeNumIndex.append(CardSuitList.index(8))
            madeNum.extend([1, 1, 8])
            rStr += '콩콩팔 (1 1 8)'
            rScore += DAN1
        elif CardSuitList.count(1) >= 1 and CardSuitList.count(2) >= 1 and CardSuitList.count(7) >= 1:
            madeNumIndex.append(CardSuitList.index(1))
            madeNumIndex.append(CardSuitList.index(2))
            madeNumIndex.append(CardSuitList.index(7))
            madeNum.extend([1, 2, 7])
            rStr += '삐리칠 (1 2 7)'
            rScore += DAN1
        elif CardSuitList.count(1) >= 1 and CardSuitList.count(3) >= 1 and CardSuitList.count(6) >= 1:
            madeNumIndex.append(CardSuitList.index(1))
            madeNumIndex.append(CardSuitList.index(3))
            madeNumIndex.append(CardSuitList.index(6))
            madeNum.extend([1, 3, 6])
            rStr += '물삼육 (1 3 6)'
            rScore += DAN1
        elif CardSuitList.count(1) >= 1 and CardSuitList.count(4) >= 1 and CardSuitList.count(5) >= 1:
            madeNumIndex.append(CardSuitList.index(1))
            madeNumIndex.append(CardSuitList.index(4))
            madeNumIndex.append(CardSuitList.index(5))
            madeNum.extend([1, 4, 5])
            rStr += '빽새오 (1 4 5)'
            rScore += DAN1
        elif CardSuitList.count(1) >= 1 and CardSuitList.count(9) >= 1 and CardSuitList.count(10) >= 1:
            madeNumIndex.append(CardSuitList.index(1))
            madeNumIndex.append(CardSuitList.index(9))
            madeNumIndex.append(CardSuitList.index(10))
            madeNum.extend([1, 9, 10])
            rStr += '삥구장 (1 9 10)'
            rScore += DAN1
        elif CardSuitList.count(2) >= 2 and CardSuitList.count(6) >= 1:
            for i in range(CardSuitList.count(1)):
                madeNumIndex.append(CardSuitList.index(2, i))
            madeNumIndex.append(CardSuitList.index(6))
            madeNum.extend([2, 2, 6])
            rStr += '니니육 (2 2 6)'
            rScore += DAN2
        elif CardSuitList.count(2) >= 1 and CardSuitList.count(3) >= 1 and CardSuitList.count(5) >= 1:
            madeNumIndex.append(CardSuitList.index(2))
            madeNumIndex.append(CardSuitList.index(3))
            madeNumIndex.append(CardSuitList.index(5))
            madeNum.extend([2, 3, 5])
            rStr += '이삼오 (2 3 5)'
            rScore += DAN2
        elif CardSuitList.count(2) >= 1 and CardSuitList.count(8) >= 1 and CardSuitList.count(10) >= 1:
            madeNumIndex.append(CardSuitList.index(2))
            madeNumIndex.append(CardSuitList.index(8))
            madeNumIndex.append(CardSuitList.index(10))
            madeNum.extend([2, 8, 10])
            rStr += '이판장 (2 8 10)'
            rScore += DAN2
        elif CardSuitList.count(3) >= 3 and CardSuitList.count(4) >= 1:
            for i in range(CardSuitList.count(1)):
                madeNumIndex.append(CardSuitList.index(3, i))
            madeNumIndex.append(CardSuitList.index(4))
            madeNum.extend([3, 3, 4])
            rStr += '심심새 (3 3 4)'
            rScore += DAN3
        elif CardSuitList.count(3) >= 1 and CardSuitList.count(7) >= 1 and CardSuitList.count(10) >= 1:
            madeNumIndex.append(CardSuitList.index(3))
            madeNumIndex.append(CardSuitList.index(7))
            madeNumIndex.append(CardSuitList.index(10))
            madeNum.extend([3, 7, 10])
            rStr += '삼칠장 (3 7 10)'
            rScore += DAN3
        elif CardSuitList.count(3) >= 1 and CardSuitList.count(8) >= 1 and CardSuitList.count(9) >= 1:
            madeNumIndex.append(CardSuitList.index(3))
            madeNumIndex.append(CardSuitList.index(8))
            madeNumIndex.append(CardSuitList.index(9))
            madeNum.extend([3, 8, 9])
            rStr += '삼빡구 (3 8 9)'
            rScore += DAN3
        elif CardSuitList.count(4) >= 4 and CardSuitList.count(2) >= 1:
            for i in range(CardSuitList.count(1)):
                madeNumIndex.append(CardSuitList.index(4, i))
            madeNumIndex.append(CardSuitList.index(2))
            madeNum.extend([4, 4, 2])
            rStr += '살살이 (4 4 2)'
            rScore += DAN4
        elif CardSuitList.count(4) >= 1 and CardSuitList.count(6) >= 1 and CardSuitList.count(10) >= 1:
            madeNumIndex.append(CardSuitList.index(4))
            madeNumIndex.append(CardSuitList.index(6))
            madeNumIndex.append(CardSuitList.index(10))
            madeNum.extend([4, 6, 10])
            rStr += '사륙장 (4 6 10)'
            rScore += DAN4
        elif CardSuitList.count(4) >= 1 and CardSuitList.count(7) >= 1 and CardSuitList.count(9) >= 1:
            madeNumIndex.append(CardSuitList.index(4))
            madeNumIndex.append(CardSuitList.index(7))
            madeNumIndex.append(CardSuitList.index(9))
            madeNum.extend([4, 7, 9])
            rStr += '사칠구 (4 7 9)'
            rScore += DAN4
        elif CardSuitList.count(5) >= 5 and CardSuitList.count(10) >= 1:
            for i in range(CardSuitList.count(1)):
                madeNumIndex.append(CardSuitList.index(5, i))
            madeNumIndex.append(CardSuitList.index(10))
            madeNum.extend([5, 5, 10])
            rStr += '꼬꼬장 (5 5 10)'
            rScore += DAN5
        elif CardSuitList.count(5) >= 1 and CardSuitList.count(6) >= 1 and CardSuitList.count(9) >= 1:
            madeNumIndex.append(CardSuitList.index(5))
            madeNumIndex.append(CardSuitList.index(6))
            madeNumIndex.append(CardSuitList.index(9))
            madeNum.extend([5, 6, 9])
            rStr += '오륙구 (5 6 9)'
            rScore += DAN5
        elif CardSuitList.count(5) >= 1 and CardSuitList.count(7) >= 1 and CardSuitList.count(8) >= 1:
            madeNumIndex.append(CardSuitList.index(5))
            madeNumIndex.append(CardSuitList.index(7))
            madeNumIndex.append(CardSuitList.index(8))
            madeNum.extend([5, 7, 8])
            rStr += '오리발 (5 7 8)'
            rScore += DAN5
        elif CardSuitList.count(6) >= 6 and CardSuitList.count(8) >= 1:
            for i in range(CardSuitList.count(1)):
                madeNumIndex.append(CardSuitList.index(6, i))
            madeNumIndex.append(CardSuitList.index(8))
            madeNum.extend([6, 6, 8])
            rStr += '쭉쭉팔 (6 6 8)'
            rScore += DAN6
        elif CardSuitList.count(7) >= 7 and CardSuitList.count(6) >= 1:
            for i in range(CardSuitList.count(1)):
                madeNumIndex.append(CardSuitList.index(7, i))
            madeNumIndex.append(CardSuitList.index(6))
            madeNum.extend([7, 7, 6])
            rStr += '철철육 (7 7 6)'
            rScore += DAN7
        elif CardSuitList.count(8) >= 8 and CardSuitList.count(4) >= 1:
            for i in range(CardSuitList.count(1)):
                madeNumIndex.append(CardSuitList.index(8, i))
            madeNumIndex.append(CardSuitList.index(4))
            madeNum.extend([8, 8, 4])
            rStr += '팍팍싸 (8 8 4)'
            rScore += DAN8
        elif CardSuitList.count(9) >= 9 and CardSuitList.count(2) >= 1:
            for i in range(CardSuitList.count(1)):
                madeNumIndex.append(CardSuitList.index(9, i))
            madeNumIndex.append(CardSuitList.index(2))
            madeNum.extend([9, 9, 2])
            rStr += '구구리 (9 9 2)'
            rScore += DAN9
        else:
            rStr += '노메이드'
            rScore += NO_MADE
            # 노메이드면 바로 리턴
            rList.extend([rStr, rScore, madeNumIndex])
            return rList


        for i in range(len(madeNum)):
            JaturiCardList.remove(madeNum[i])
        
        if JaturiCardList.count(3) >= 1 and JaturiCardList.count(8) >= 1:
            rStr += ' 38광땡'
            rScore += GDD38
        elif JaturiCardList.count(1) >= 1 and JaturiCardList.count(8) >= 1\
            or JaturiCardList.count(1) >= 1 and JaturiCardList.count(3) >= 1:
            rStr += ' 광땡'
            rScore += GDD
        elif JaturiCardList.count(1) >= 2:
            rStr += ' 삥땡'
            rScore += DD1
        elif JaturiCardList.count(2) >= 2:
            rStr += ' 2땡'
            rScore += DD2
        elif JaturiCardList.count(2) >= 2:
            rStr += ' 2땡'
            rScore += DD2
        elif JaturiCardList.count(3) >= 3:
            rStr += ' 3땡'
            rScore += DD3
        elif JaturiCardList.count(4) >= 4:
            rStr += ' 4땡'
            rScore += DD4
        elif JaturiCardList.count(5) >= 5:
            rStr += ' 5땡'
            rScore += DD5
        elif JaturiCardList.count(6) >= 6:
            rStr += ' 6땡'
            rScore += DD6
        elif JaturiCardList.count(7) >= 7:
            rStr += ' 7땡'
            rScore += DD7
        elif JaturiCardList.count(8) >= 8:
            rStr += ' 8땡'
            rScore += DD8
        elif JaturiCardList.count(9) >= 9:
            rStr += ' 9땡'
            rScore += DD9
        elif JaturiCardList.count(10) >= 2:
            rStr += ' 장땡'
            rScore += DD10
        elif JaturiCardList.count(2) >= 1 and JaturiCardList.count(8) >= 1\
            or JaturiCardList.count(3) >= 1 and JaturiCardList.count(7) >= 1:
            rStr += ' 망통'
            rScore += MANGTONG
        else:
            ggeut = JaturiCardList[0]+JaturiCardList[1]
            if ggeut > 10:
                ggeut -= 10
            rStr += ' ' + str(ggeut) + '끗'
            rScore += ggeut
        
        rList.extend([rStr, rScore, madeNumIndex])
        return rList