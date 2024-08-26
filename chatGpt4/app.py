from g4f.client import Client

client = Client()
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role":"user", "content":"Write me 15 types of Performance testing"}],
)
print(response.choices[0].message.content)

# python3 app.py