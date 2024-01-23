from random import randint as rand

class die(object):
    def getvalue(self):
        return self.value
    
    def __init__(self):
        self.roll()
    
    def roll(self):
        self.value = rand(1,6)
    
    def __str__(self):
        return("{}".format(self.value))

class hand(object):
    text = {
        "A": "| Ones       | ",
        "B": "| Twos       | ",
        "C": "| Threes     | ",
        "D": "| Fours      | ",
        "E": "| Fives      | ",
        "F": "| Sixes      | ",
        "G": "| 3-Kind     | ",
        "H": "| 4-Kind     | ",
        "I": "| FullHouse  | ",
        "J": "| Short      | ",
        "K": "| Long       | ",
        "L": "| Yahtzee    | ",
        "M": "| Chance     | ",
        "N": "| Upper      | ",
        "O": "| Bonus      | ",
        "P": "| Lower      | ",
        "Q": "| Total      | "
    }

    def __init__(self):
        self.card = {
            "A": 0,
            "B": 0,
            "C": 0,
            "D": 0,
            "E": 0,
            "F": 0,
            "G": 0,
            "H": 0,
            "I": 0,
            "J": 0,
            "K": 0,
            "L": 0,
            "M": 0
        }
        self.newround()

    def newround(self):
        self.turn = 1
        self.dice = [ die(), die(), die(), die(), die() ]
        self.hold = [ False, False, False, False, False ]

    def matchcount(self):
        maxcount = 0
        for i in range(6):
            n = self.countvalue(i+1)
            if n > maxcount:
                maxcount = n
        return maxcount

    def hasvalue(self,v):
        for d in self.dice:
            if d.value == int(v):
                return True
        return False

    def countvalue(self,v):
        qty = 0
        for d in self.dice:
            if d.value == int(v):
                qty += 1
        return qty

    def hasshort(self):
        shorts = [ "1234", "2345", "3456" ]
        for short in shorts:
            fourinarow = True
            for V in short:
                if not self.hasvalue(V):
                    fourinarow = False
                    break
            if fourinarow: return fourinarow
        return False

    def haslong(self):
        longs = [ "12345", "23456" ]
        for long in longs:
            fiveinarow = True
            for V in long:
                if not self.hasvalue(V):
                    fiveinarow = False
                    break
            if fiveinarow: return fiveinarow
        return False
    
    def hasfullhouse(self):
        for A in "123456":
            for B in "123456":
                if ( self.countvalue(A) == 2 and self.countvalue(B) == 3 ) or (self.countvalue(A) == 5):
                    return True
        return False

    def score(self,field):
        if self.card[field] != 0: return
        upperhalf = "ABCDEF"
        if field in upperhalf:
            for i in range(len(upperhalf)):
                if field == upperhalf[i]:
                    thescore = 0
                    tgtval = i+1
                    for d in self.dice:
                        if d.value == tgtval: thescore += d.value
                    if thescore == 0: thescore = "-0"
                    self.card[field] = thescore
        elif field in "GHM":
            thescore = 0
            for d in self.dice:
                thescore += d.value
            if ( field == "G" and self.matchcount() >= 3 ) or (field == "H" and self.matchcount() >= 4) or (field == "M"):
                self.card[field] = thescore
            else:
                self.card[field] = "-0"
        elif field == "I":
            if self.hasfullhouse():
                self.card[field] = 25
            else:
                self.card[field] = "-0"
        elif field == "J":
            if self.hasshort():
                self.card[field] = 30
            else:
                self.card[field] = "-0"
        elif field == "K":
            if self.haslong():
                self.card[field] = 40
            else:
                self.card[field] = "-0"
        elif field == "L":
            if self.matchcount() >= 5:
                self.card[field] = 40
            else:
                self.card[field] = "-0"
        self.showcard()
        self.newround()

    def showcard(self):
        tophalf = 0
        for top in "ABCDEF":
            header = top
            if self.card[top] != 0: header = "-"
            print("{} {} {}".format(header, self.text[top],self.card[top]))
            tophalf += self.card[top]
        print("# {} {}".format(self.text["N"],tophalf))
        bonus = 0
        if tophalf >= 63: bonus = 35
        print("# {} {}".format(self.text["O"],bonus))
        bothalf = 0
        for bot in "GHIJKLM":
            header = bot
            if self.card[bot] != 0: header = "-"
            print("{} {} {}".format(header, self.text[bot],self.card[bot]))
            bothalf += int(self.card[bot])
        print("# {} {}".format(self.text["P"],bothalf))
        print("# {} {}".format(self.text["Q"],tophalf+bonus+bothalf))

    def toggle(self,slot):
        self.hold[slot] = self.hold[slot] == False
    
    def roll(self):
        for i in range(len(self.dice)):
            if not self.hold[i]:
                self.dice[i].roll()
        self.turn += 1
        if self.turn > 3: self.newround()
        if self.turn == 3:
            self.hold = [ False, False, False, False, False ]
    
    def complete(self):
        for field in self.card:
            if self.card[field] == 0: return False
        return True

    def __str__(self):
        ret = ""
        for i in range(len(self.dice)):
            if self.hold[i]:
                if i == 0:
                    ret = "Turn: {} | [{}]".format(self.turn, self.dice[i])
                else:
                    ret = "{} [{}]".format(ret, self.dice[i])
            else:
                if i == 0:
                    ret = "Turn: {} | .{}.".format(self.turn, self.dice[i])
                else:
                    ret = "{} .{}.".format(ret, self.dice[i])
        return(ret)
    
class yahtzee(object):
    def __init__(self):
        P1 = hand()
        while (not P1.complete()):
            print("P1: {}".format(P1))
            for cmd in input("> "):
                n = yahtzee.GetCmdNumber(cmd)
                a = yahtzee.GetCmdLetter(cmd)
                if ( n != 0 ): P1.toggle(n-1)
                elif ( a != 0 ): P1.score(a)
                elif cmd == "q": self.running = False
                elif cmd == "r": P1.roll()
                elif cmd == "v": P1.showcard()
                elif cmd == " ": pass
                else:
                    print("### INSTRUCTIONS ###")
                    print("q to quit")
                    print("v to view the scorecard")
                    print("r to roll free dice    | .#.")
                    print("1..5 to hold that die  | [#]")
                    print("A..M score dice in that slot (view card to see slot IDs)")

    def GetCmdNumber(cmd):
        if cmd in "12345":
            return int(cmd)
        return 0

    def GetCmdLetter(cmd):
        if cmd in "ABCDEFGHIJKLM":
            return cmd
        return 0

if __name__ == "__main__":
    yahtzee()