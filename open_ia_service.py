from openai import OpenAI

client = OpenAI(api_key="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", base_url="https://openrouter.ai/api/v1")

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Tu es un traducteur."},
        {"role": "user", "content": "Traduire 'Hello' en français."}
    ]
)

translated_text = response.choices[0].message.content
print(translated_text)
