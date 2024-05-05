import ollama

msgs = [
    {
        "role": "system",
        "content": "The user will give you a concept. Explain it to a 5 years old, using descriptive imagery and interesting and fun."
    },
    {
        "role": "user",
        "content": "Global Warming"
    }
]

output = ollama.chat(model="phi3", messages=msgs)
print(output["message"]["content"])
