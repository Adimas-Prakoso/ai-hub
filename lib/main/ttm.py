import requests
import json

j = open("./config.json")
data = json.load(j)
huggingface_apikey = data["huggingface_apikey"]

API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-stereo-small"
headers = {"Authorization": huggingface_apikey}

def generate_music(prompt):
    payload = {
	"inputs": prompt,
}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content