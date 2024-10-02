from ollama import Client
client = Client(host="http://localhost:11434")

def pull_model():
  response = client.pull(model='llama3.2:1b', stream=True)
  return response

def get_ollama_chat_response(prompt):
  response = client.chat(model='llama3', messages=[
    {
      'role': 'user',
      'content': prompt,
    },
  ], stream=True)
  return response


if __name__ == "__main__":
  # response = pull_model() #might take few min
  # for item in response:
  #   print(item)

  response = get_ollama_chat_response('Why is the sky blue?')
  for chunk in response:
    print(chunk["message"]["content"], end='', flush=True)
