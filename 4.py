import ollama 
prompt = "What is global warming";

output = ollama.generate(model="phi3", prompt=prompt, stream=True)
for chunk in output:
    print(chunk["response"], end='', flush=True)
    if chunk["done"] == True:
        print("First generation complete")
        context = chunk["context"]

prompt = "Who is responsible?"
output2 = ollama.generate(model="phi3", prompt=prompt, context=context, stream=True);
for chunk in output2:
    print(chunk["response"], end='', flush=True)



