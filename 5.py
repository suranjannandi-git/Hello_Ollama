import ollama 

with open('elephant.jpg', 'rb') as image_file:
    img = image_file.read()

prompt = "Describe the picture"
output3 = ollama.generate(model='llama3', prompt=prompt, images=[img])
print(output3["response"]);

