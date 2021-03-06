from typing import List

MARK = -1
card = []
original_cards = []

with open("input.txt", "r") as f:
    contents = f.readlines()

called_numbers = [int(i) for i in contents[0].strip("\n").split(",")]

contents.pop(0)
contents.pop(0)

for line in contents:
    line = [int(i) for i in line.strip("\n").split()]
    if line:
        card.append(line)
        print(card)
    else:
        original_cards.append(card)
        card = []
original_cards.append(card)


def has_row_winner(card: List[List[int]]) -> bool:
    for row in card:
        if sum(row) == -5:
            return True
    return False


def has_col_winner(card: List[List[int]]) -> bool:
    for i in range(0, 5):
        if sum([row[i] for row in card]) == -5:
            return True
    return False


def mark_card(card: List[List[int]], called_number) -> List[List[int]]:
    for row in card:
        for i in range(0, 5):
            if row[i] == called_number:
                row[i] = MARK

    return card


# part 1
cards = original_cards.copy()


def bingo(cards: List[List[List[int]]], called_numbers: List[int]) -> List[List[int]]:
    for called_number in called_numbers:
        print(called_number)
        for card in cards:
            card = mark_card(card, called_number)
            if has_row_winner(card) or has_col_winner(card):
                print("winner")
                return called_number, card


winning_number, winning_card = bingo(cards, called_numbers)

sum_of_card = 0
for row in winning_card:
    for i in row:
        if i >= 0:
            sum_of_card += i

print(sum_of_card * winning_number)

# part 2
cards = original_cards.copy()


def anti_bingo(
    cards: List[List[List[int]]], called_numbers: List[int]
) -> List[List[int]]:
    winning_cards = []
    for called_number in called_numbers:
        print(called_number)
        for card in cards:
            card = mark_card(card, called_number)
            if has_row_winner(card) or has_col_winner(card):
                # print("winner")
                if card not in winning_cards:
                    print("winner")
                    winning_cards.append(card)
                if len(winning_cards) == len(cards):
                    return called_number, card


winning_number, winning_card = anti_bingo(cards, called_numbers)

sum_of_card = 0
for row in winning_card:
    for i in row:
        if i >= 0:
            sum_of_card += i

print(sum_of_card)
print(sum_of_card * winning_number)

"""
Since my motivation for completing these puzzles daily was to have an excuse to write a little bit of code and knock some rust off, 
it's probably worth looking at my completed solutions and at least bullet out what i'd do differently if this was "real" code.

- bingo cards should probably be wrapped in a class, instead of a list of lists of ints (5x5 was specified in the problem itself)
- there's a lot of repeated code, could take the time to clean up and refactor/extend part 1 to write part 2
- loops over ranges still feel pretty clunky in python, prob should enumerate() but it's 5x5 by spec
- mark_card() and the winner functions should clearly be methods of a card class
- i spent more time dealing with the inputs than i did writing part 1, so i prob need to remember how file inputs work
- python sets can't contain lists, only hashable types
- in hindsight, using 0 to mark called numbers would've saved some effort. im guilty of not reading the problem statement through
    and seeing that i'd need to sum the open numbers at the end and that 0 wasn't used in the game
"""
