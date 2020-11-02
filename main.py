import random

n1 = input("Whats your name? ")

n2 = input("Whats your partners name? ")

p1 = []

p2 = []

p1score = 0

p2score = 0

#makes a deck and adds values 2-14 for the cards 4 time into 52 cards

def deck():
  deck = []
  for i in range(2,15):
    deck.append(i)
  
  deck *= 4
  return deck

bDeck = deck()

#shuffles the deck randomly

random.shuffle(bDeck)

#takes 26 of the cards from the end to the first player and second player keeps the deck of 26 cards

for f in range(26):
  p1.append(bDeck.pop())

p2 = []
p2 = bDeck

#compares the card values

for i in range(len(bDeck)):
  a = p1.pop()
  b = p2.pop()
  #checks each card value and sees who wins
  if a > b:
    print( str(a) + ' ' + str(b) + ' ' + n1 + " has won ")
    p1score += 1
  elif b > a:
    print(str(a) + ' ' + str(b) + ' ' + n2 + " has won  ")
    p2score += 1
  elif a == b:
    print("War!")

#compares the score of the player and says who won

def finalV():
  if p1score > p2score:
    print(n1 + " is a winner with a score of " + str(p1score))
    print(n2 + " is a loser with a score of " + str(p2score))
  elif p2score > p1score:
    print(n2 + " is a winner with a score of " + str(p2score))
    print(n1 + " is a loser with a score of " + str(p1score))
  elif p1score == p2score:
    print("You guys tied!")

#prints final score of the person who won

finalV()
