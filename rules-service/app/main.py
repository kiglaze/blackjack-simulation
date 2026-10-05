from fastapi import FastAPI, HTTPException

from app.models import Ruleset


app = FastAPI(title="Blackjack Rules Service")


RULESETS = {
    "vegas-6-deck": Ruleset(
        name="Vegas 6 Deck",
        decks=6,
        dealer_hits_soft_17=True,
        blackjack_payout=1.5,
        double_after_split=True,
        surrender_allowed=True,
    ),
    "atlantic-city": Ruleset(
        name="Atlantic City",
        decks=8,
        dealer_hits_soft_17=False,
        blackjack_payout=1.5,
        double_after_split=True,
        surrender_allowed=True,
    ),
}


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/rules")
async def get_rulesets():
    return RULESETS


@app.get("/rules/{ruleset_id}", response_model=Ruleset)
async def get_ruleset(ruleset_id: str):
    ruleset = RULESETS.get(ruleset_id)

    if ruleset is None:
        raise HTTPException(
            status_code=404,
            detail="Ruleset not found",
        )

    return ruleset
