import requests
import json

j = open("./config.json")
data = json.load(j)
xcode_apikey = data["xcode_apikey"]

def ChatModels(models, text):
    if 'GPT-3.5' in models:
        get = requests.get(f"https://api.akuari.my.id/ai/gpt?chat={text}")
        res = get.json()
        mess = res["respon"]
    elif 'BARD-AI' in models:
        get = requests.get(f"https://api.xcodeteam.xyz/api/artificial-intelligence/bard?api_key={xcode_apikey}&question={text}")
        res = get.json()
        mess = res["data"]["answer"]
    elif 'SIM-SIMI' in models:
        get = requests.get(f"https://api.akuari.my.id/simi/simi2?query={text}")
        res = get.json()
        mess = res["respon"]
    elif 'CHATTY-AI' in models:
        get = requests.get(f"https://api.xcodeteam.xyz/api/artificial-intelligence/chatty-ai?api_key={xcode_apikey}&question={text}")
        res = get.json()
        mess = res["data"]["answer"]
    return mess

def insert_newline(text):
  return text.replace(" " * 100, '\n')
