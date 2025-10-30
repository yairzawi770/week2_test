from random import random


def create_card(rank: str, suite: str) -> dict:
    cards = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    return {"rank": rank, "suite": suite}

def build_standard_deck() -> list[dict]:
    temp_cards = ["A","2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    temp_suites = ["H", "C", "D", "S"]
    cards = []
    for tc in temp_cards:
        for ts in temp_suites:
            card = create_card(tc, ts)
            cards.append(card)
    return cards


print(build_standard_deck())


def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    random.shuffle(deck)
    return deck
