from CardClass import Card_Class
class Player_Class(object):

    cardStack = Card_Class()
    def __init__(self, name):
        self.Name = name
        self.Cards = []
    
    def GiveCard (self):
        self.Cards.append(self.cardStack.GetCard())
        #self.Cards.append(cardStack.GetCard())

    def ClearCards (self):
        self.Cards=[]
    
    




