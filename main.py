from fastapi import FastAPI, Request

import controller

app = FastAPI()


@app.post("/sentiment")
async def submit_data(request: Request):
    data = await request.json()
    phrase = data['phrase']
    sentiment = await controller.analyse(phrase)
    return sentiment
