from ollama import Client

client = Client(host="http://localhost:11434")
prompt = "What is global warming"

output = client.generate(model="llama3", prompt=prompt, stream=True)
# print(output["response"])

for chunk in output:
    print(chunk["response"], end='', flush=True)
