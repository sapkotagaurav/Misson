import random
class Card:
    def __init__(self,suit="CLUBS",rank="TWO") :
        self.suit = suit
        self.rank = rank
        
    def __str__(self) -> str:
        return "{self.rank} of {self.suit}".format(self=self)
   
class Deck:
    def __init__(self) -> None:
        self.ranks =["TWO", "THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE","TEN","JACK","QUEEN","KING","ACE"]
        self.suits=["CLUBS","SPADES","DIAMONDS","HEARTS"]
        deck =[]
        #creating 13X4 cards and saving the deck
        for rank in self.ranks:
            for suit in self.suits:
                card = Card(suit=suit,rank=rank)
                deck.append(card)
        self.deck = deck
          
def main():
    shuffled_deck= Deck().deck
    #shuffling the deck
    random.shuffle(shuffled_deck)
    print("_________Shuffled Deck________")
    for card in shuffled_deck:
        print(card)
    print("_______Ordered by ranks______")
    #saving the ordered by ranks deck to use this in later problem
    orderedbyrank=[]
    for rank in Deck().ranks:
        for card in shuffled_deck:
            if str(card).__contains__(rank):
                print(card)
                orderedbyrank.append(card)
    print("____________FINAL_______ Ordered by rank and suit_______")
    for suit in Deck().suits:
        for card in orderedbyrank:
            if(str(card).__contains__(suit)):
                print(card)    



    
main()
