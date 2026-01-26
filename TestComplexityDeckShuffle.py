import random
import time
import tracemalloc

Type = ['Heart', 'Diamond', 'Club', 'Spade']
Ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

tracemalloc.start()
time.start_time = time.time()
deck = [(Type, Rank) for Type in Type 
        for Rank in Ranks] #(Portfolio Courses, 2023)

assert len(deck) == 52 #Deck should have 52 cards.
assert len(set(deck)) == 52 #All cards should be unique.

random.seed(123)

for i in range(len(deck)):
    j = random.randint(0, len(deck) - 1)
    deck[i], deck[j] = deck[j], deck[i]

print("\nYour Deck is: ")
for Type, Rank in deck:
    print(f"{Rank} of {Type}")

current, peak = tracemalloc.get_traced_memory()

print(f"\n--- Execution Time: {(time.time() - time.start_time) * 1000:.3f} miliseconds ---")
print(f"--- Memory Usage: {peak:.2f} bytes ---")

#References

#Portfolio Courses (2023). Shuffle A Deck Of Cards | Python Example. [online] YouTube. Available at: https://www.youtube.com/watch?v=9Lh4PAN1HsA [Accessed 24 Jan. 2026].


