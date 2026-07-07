import os
import json
from openai import OpenAI  # Import the OpenAI library

from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))  # Initialize the OpenAI client   

response = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": "What is the capital of France?"}])
print(response.choices[0].message.content)   # Print the response from the model in JSON format with the key "capital"
print(json.loads(response.choices[0].message.content)["capital"])   # Print the capital from the response   


# Create a function to get the capital of a country
def get_capital(country):
   response = client.chat.completions.create(model="gpt-4o", messages=[{"role": "user", "content": f"What is the capital of {country}?"}])
   return json.loads(response.choices[0].message.content)["capital"]

print(get_capital("France"))   # Print the capital of France