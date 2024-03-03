from langfuse import Langfuse
from langfuse.openai import openai

# BUG? Why aren't these values picked up from here? (I had to manually set the env variables)
langfuse = Langfuse(
  secret_key="sk-lf-cfdd7e7c-213f-49e4-9862-11a57294b0d5",
  public_key="pk-lf-7a50182c-9626-4af6-96c8-f011e76fdb36",
  host="http://localhost:3000"
)

completion = openai.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": "You are a very accurate calculator."},
      {"role": "user", "content": "1 + 1 = "}],
)

print(completion)