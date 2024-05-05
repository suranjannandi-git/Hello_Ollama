import ollama 
prompt = "What is global warming";
output = ollama.generate(model="mistral")

print (prompt)
