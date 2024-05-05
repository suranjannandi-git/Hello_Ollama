import ollama 
prompt = "What is global warming";

output = ollama.generate(model="mistral", prompt=prompt, stream=False)
print(output)

