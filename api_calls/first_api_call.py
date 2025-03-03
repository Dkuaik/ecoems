import json 
from openai import OpenAI
import os

with open('prompt/question_generator.json', 'r') as f:
    prompt = json.load(f)

model_ai = 'text-embedding-ada-002'

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# print(OPENAI_API_KEY)

client = OpenAI()

response = client.embeddings.create(
    model=model_ai,
    input=prompt
)

with open ('api_ans/question_generator.json', 'w') as f:
    json.dump(response, f)

