import ollama 
prompt = "What is global warming";

output = ollama.generate(model="mistral", prompt=prompt, stream=True)
for chunk in output:
    print(chunk["response"], end='', flush=True)

