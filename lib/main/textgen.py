import requests
import json

j = open("./config.json")
data = json.load(j)
huggingface_apikey = data["huggingface_apikey"]

API_URL = "https://api-inference.huggingface.co/models/HuggingFaceH4/zephyr-7b-beta"
headers = {"Authorization": huggingface_apikey}

def textgen(prompt):
    payload = {
	"inputs": prompt,
}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()