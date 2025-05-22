import random
from .card import Suit, Rank, Card

from abc import ABC, abstractmethod


class BaseDeck(ABC):
    def __init__(self):
        self.cards = []
        self._initialize_cards()

    def __len__(self):
        return len(self.cards)
    
    def reset(self):
        self._initialize_cards()

    @abstractmethod
    def shuffle(self):
        pass

    @abstractmethod
    def deal(self, n=1):
        pass
    
    @abstractmethod
    def _initialize_cards(self):
        pass


class StandardDeck(BaseDeck):
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, n: int = 1):
        if n > len(self):
            raise ValueError("Deck does not have enough cards to deal")
        if n <= 0:
            raise ValueError("Must deal one or more cards")
        
        cards_to_deal = [self.cards.pop() for _ in range(n)]
        return cards_to_deal
    
    def _initialize_cards(self):
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(suit, rank))
