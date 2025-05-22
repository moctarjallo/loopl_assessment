from openai import OpenAI
client = OpenAI()

import asyncio


async def analyse(phrase):

    response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
        "role": "system",
        "content": "You will be provided with a tweet, and your task is to classify its sentiment as positive, neutral, or negative."
        },
        {
        "role": "user",
        "content": f"{phrase}"
        }
    ],
    temperature=0.7,
    max_tokens=64,
    top_p=1
    )
    return response.choices[0].message.content

if __name__ == '__main__':
    phrases = [
        "Ce produit est fantastique, je le recommande vivement !",
        "Service client décevant, j'ai attendu 2 heures au téléphone.",
        "Qualité correcte pour le prix, rien d'exceptionnel.",
        "Livraison rapide et emballage soigné, très satisfait."
    ]
    for phrase in phrases:
        response = asyncio.run(analyse(phrase))
        print(response)