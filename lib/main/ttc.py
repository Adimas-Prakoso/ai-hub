import openai
import json

j = open("./config.json")
data = json.load(j)
openai_apikey = data["openai_apikey"]

def generate_code(prompt):
    # Set up OpenAI API credentials
    openai.api_key = openai_apikey

    # Generate code using GPT-3 model
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n = 1,
        stop=None,
    )

    # Extract the generated code from the response
    generated_code = response.choices[0].text.strip()

    return generated_code

