from typing import Union

from fastapi import FastAPI, HTTPException, Request

app = FastAPI()


@app.post("/sentiment")
async def submit_data(request: Request):
    data = await request.json()
    phrase = data['phrase']
    sentiment = await analyse(phrase)
    return sentiment


async def analyse(phrase):
    return "positif"
