import random #Importing Random, because you cannot "Randomise" without it, it would be shuffling otherwise.

Type = ['Heart', 'Diamond', 'Club', 'Spade']
Ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

deck = [(Type, Rank) for Type in Type 
        for Rank in Ranks] #(Portfolio Courses, 2023)

seed = random.randint(1, 1000)
random.seed(seed)

for i in range(len(deck)):
    j = random.randint(0, len(deck) - 1)
    deck[i], deck[j] = deck[j], deck[i]

print(*deck, sep="\n")


#References

#Portfolio Courses (2023). Shuffle A Deck Of Cards | Python Example. [online] YouTube. Available at: https://www.youtube.com/watch?v=9Lh4PAN1HsA [Accessed 24 Jan. 2026].