from pydantic import BaseModel

class Ruleset(BaseModel):
    name: str
    decks: int
    dealer_hits_soft_17: bool
    blackjack_payout: float
    double_after_split: bool
    surrender_allowed: bool
