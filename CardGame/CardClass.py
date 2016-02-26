class Card_Class(object):
    suit = ["Heart", "Spade","Club","Diamond"]
    prøve = [["hej",2],["hej",3]]
    cardtype = [["1",1],["2",2],["3",3],["4",4],["5",5],["6",6],["7",7],["8",8],["9",9],["10",10],["J",10],["Q",10],["K",10],["A",(11,1)]]
    
    def __init__(self):
        
        self.allCards = []
        for name,value in self.cardtype:
            for Suit in self.suit:
                self.allCards.append(tuple([Suit + " " + name,value]))
                
                
        print(self.allCards)
        print("Henriks computer hacked = comlete")
    def GetCard(self):
        return(self.allCards.pop(0))

    def PrintAll(self):
        space = 0
        add = 1
        while True: 
            if space >= 50:
                add = -1
            elif space <=0:
                add = 1
            space += add
            yield (" "*space +"Hacking your mom")
            yield ((50-space)*" "+"You screwed")
            

            
        
    pass




