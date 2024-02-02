from random import randint as rand
from sys import argv as argv

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

    def __init__(self,name="P0"):
        self.name = name
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
        self.dice = []
        self.hold = []
        for i in range(5):
            self.dice.append(die())
            self.hold.append(False)

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
        print("scorecard: {}".format(self.name))
        print("=====================")
        tophalf = 0
        for top in "ABCDEF":
            header = top
            if self.card[top] != 0: header = "-"
            if self.card[top] == "-0":
                print("{} {}  -0".format(header, self.text[top]))
            else:
                print("{} {} {: 3}".format(header, self.text[top],self.card[top]))
            tophalf += int(self.card[top])
        print("--|------------|-----")
        print("= {}{: 4}".format(self.text["N"],tophalf))
        bonus = 0
        if tophalf >= 63: bonus = 35
        print("+ {}{: 4}".format(self.text["O"],bonus))
        print("--|------------|-----")
        bothalf = 0
        for bot in "GHIJKLM":
            header = bot
            if self.card[bot] != 0: header = "-"
            if self.card[bot] == "-0":
                print("{} {}  -0".format(header, self.text[bot]))
            else:
                print("{} {} {: 3}".format(header, self.text[bot],self.card[bot]))
            bothalf += int(self.card[bot])
        print("--|------------|-----")
        print("= {}{: 4}".format(self.text["P"],bothalf))
        print("--|------------|-----")
        print("=={}{: 4}".format(self.text["Q"],tophalf+bonus+bothalf))
        print("=====================")

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
        rollname = [ "unused", "1st", "2nd", "3rd" ]
        for i in range(len(self.dice)):
            if self.hold[i]:
                if i == 0:
                    ret = "{}: {} roll | [{}]".format(self.name, rollname[self.turn], self.dice[i])
                else:
                    ret = "{} [{}]".format(ret, self.dice[i])
            else:
                if i == 0:
                    ret = "{}: {} roll | .{}.".format(self.name, rollname[self.turn], self.dice[i])
                else:
                    ret = "{} .{}.".format(ret, self.dice[i])
        return(ret)
    
    def getcmds(self):
        cmds = " "
        try:
            cmds = input("{} > ".format(self))
        except KeyboardInterrupt as e:
            cmds = "q"
        except EOFError as e:
            cmds = "q"
        return cmds
    
    def doturn(self):
        self.showcard()
        if self.complete(): return
        EndTurn = False
        while not EndTurn:
            words = self.getcmds().split()
            # TODO: more input sanitation.
            for word in words:
                if word.lower() == ("fix"):
                    self.card[words[1].upper()] = int(words[2])
                    self.showcard()
                    break
                else:
                    for cmd in word:
                        n = self.GetCmdNumber(cmd)
                        a = self.GetCmdLetter(cmd)
                        if ( n != 0 ):
                            self.toggle(n-1)
                        elif ( a != 0 ):
                            self.score(a)
                            EndTurn = True
                        elif cmd == "q":
                            return True
                        elif cmd == "r":
                            self.roll()
                        elif cmd == "v":
                            self.showcard()
                        elif cmd == "p":
                            self.showcard()
                        elif cmd == " ":
                            pass
                        else:
                            print("### INSTRUCTIONS ###")
                            print("> q to quit")
                            print("> v or p to view or print the scorecard")
                            print("> r to roll free dice    | .#.")
                            print("> 1..5 to hold that die  | [#]")
                            print("> A..F score dice in the upper half")
                            print("> G..M score dice in lower half")
                            print("> fix A..M ## to correct an honest mistake")

    def GetCmdNumber(self,cmd):
        if cmd in "12345":
            return int(cmd)
        return 0

    def GetCmdLetter(self,cmd):
        cmd = cmd.upper()
        if cmd in "ABCDEFGHIJKLM":
            return cmd
        return 0


class yahtzee(object):
    def __init__(self, pnames):
        players = []
        completion = []
        for name in pnames:
            players.append(hand(name))
            completion.append( False )
        quit = False
        while False in completion:
            for i in range(len(players)):
                quit = players[i].doturn()
                if quit:
                    return
                completion[i] = players[i].complete()

if __name__ == "__main__":
    PRENAMES = [ "P1", "P2", "P3", "P4", "P5", "P6" ]
    np = 1
    if len(argv) > 1:
        np = int(argv[1])
    players = []
    for i in range(np):
        players.append(PRENAMES[i])
    yahtzee(players)