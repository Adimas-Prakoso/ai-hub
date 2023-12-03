import requests
import json

j = open("./config.json")
data = json.load(j)
huggingface_apikey = data["huggingface_apikey"]
API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"

def imagetotext(image_path):
    headers = {"Authorization": huggingface_apikey}
    with open(image_path, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()