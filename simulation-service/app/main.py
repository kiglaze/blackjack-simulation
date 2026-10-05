from fastapi import FastAPI, HTTPException
import httpx

app = FastAPI(title="Blackjack Simulation Service")


@app.get("/health")
async def health():
    return {"status": "ok"}


@app.get("/simulations/test/{ruleset_id}")
async def test_simulation(ruleset_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(
            f"http://rules-service:8000/rules/{ruleset_id}"
        )

    if response.status_code == 404:
        raise HTTPException(
            status_code=404,
            detail="Ruleset not found",
        )

    response.raise_for_status()

    rules = response.json()

    return {
        "message": "Simulation service successfully retrieved rules",
        "rules": rules,
    }
