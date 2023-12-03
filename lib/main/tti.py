import requests
import json

j = open("./config.json")
data = json.load(j)
huggingface_apikey = data["huggingface_apikey"]

def query(prompt, api_url):
    payload = {
        "inputs": prompt,
    }
    headers = {"Authorization": huggingface_apikey}
    response = requests.post(api_url, headers=headers, json=payload)
    return response.content
    