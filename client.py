import requests


url = "http://127.0.0.1:8000/sentiment"

data = {
    "phrase": "Ce produit est fantastique, je le recommande vivement !",
}

response = requests.post(url, json=data)

print(response.json())