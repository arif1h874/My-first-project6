from openai import OpenAI
 
# pip install openai 
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(
  api_key="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",
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud"},
    {"role": "user", "content": "what is coding"}
  ]
)

print(completion.choices[0].message.content)