import requests
import json

j = open("./config.json")
data = json.load(j)
huggingface_apikey = data["huggingface_apikey"]

API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
headers = {"Authorization": huggingface_apikey}

def qa(question, context):
    payload = {
	"inputs": {
		"question": question,
		"context": context
	},
}
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
