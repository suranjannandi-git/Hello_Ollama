# Hello_Ollama
Learn how to deploy LLM models in local computer 

##### Steps to play with Ollama and Models onPrem:

###### Download & Install Ollama
    https://ollama.com/download

###### Install Ollama CLI
    # double click to install

###### Check list of available models
    https://ollama.com/library

###### Few necessary CLI command 
    > ollama pull <model name e.g. mistral>
    > ollama run mistral
    >> /set system <instruction for new model>      # creating a new model
    >> /save <new model name>                       # save the new model 
    >> /bye                                         # close the current model
    > ollama run <newly created model>
    > ollama rm <model name>

###### Try the #.py files, make model/code change and observe 

###### Connecting using api
    local ollama runs on http://localhost:11434
    same example is in 8.py 


Thanks for the teaching, reaceived from Matt Williams
https://www.youtube.com/watch?v=_4K20tOsXK8
https://github.com/technovangelist/videoprojects/tree/main/2024-04-01-intro-dev-python

# https://hub.docker.com/r/ollama/ollama
docker pull ollama/ollama
docker run --rm -d --name ollama-container -p 11434:11434/tcp ollama/ollama:latest 
docker logs -f --tail 100 ollama-container
http://localhost:11434/
docker exec -it ollama-container /bin/bash
docker exec -it ollama-container printenv
docker inspect ollama-container

curl -X POST http://localhost:11434/api/pull -d '{"name": "llama2"}' -H "Content-Type: application/json"
curl -X POST http://localhost:11434/api/generate -d '{"model": "llama2", "prompt": "What is AI?"}' -H "Content-Type: application/json"

# Host gguf model through ollama
create a file Modelfile
Add a line into Medelfile as
    FROM path/merlinite-7b-lab-Q4_K_M.gguf
Execute command
    ollama create <mygguf> -f Modelfile
    ollama list 
Use the <mygguf> model for inferencing

