import random

Type = ['Heart', 'Diamond', 'Club', 'Spade']
Ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = [(Type, Rank) for Type in Type 
        for Rank in Ranks] #(Portfolio Courses, 2023)

assert len(deck) == 52 #Deck should have 52 cards.
assert len(set(deck)) == 52 #All cards should be unique.

random.seed(123)

for i in range(len(deck)):
    j = random.randint(0, len(deck) - 1)
    deck[i], deck[j] = deck[j], deck[i]

assert deck != [(Type, Rank) for Type in Type 
        for Rank in Ranks] #Deck should be shuffled.

first4_expected = [ ('Club', '5'),
                    ('Spade', '3'),
                    ('Spade', '10'),
                    ('Diamond', '2'),
                   ]

assert deck[:4] == first4_expected

#print("\nYour Deck is: ")
#for Type, Rank in deck:
#    print(f"{Rank} of {Type}")

#References

#Portfolio Courses (2023). Shuffle A Deck Of Cards | Python Example. [online] YouTube. Available at: https://www.youtube.com/watch?v=9Lh4PAN1HsA [Accessed 24 Jan. 2026].


