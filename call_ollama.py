from ollama import Client

client = Client(host="http://localhost:11434")
MODEL = 'deepseek-r1:8b'  # 'llama3.2:1b'

def pull_model():
  response = client.pull(model=MODEL, stream=True)
  return response

def get_ollama_chat_response(prompt):
  response = client.chat(model=MODEL, messages=[
    {
      'role': 'user',
      'content': prompt,
    },
  ], stream=True)
  return response

if __name__ == "__main__":
  response = get_ollama_chat_response('white a simple python program that prints "Hello, Ollama!"')
  for chunk in response:
    print(chunk["message"]["content"], end='', flush=True)
  print()  # Newline after the response
