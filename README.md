# Hello_Ollama
Learn how to deploy LLM models in local computer 

##### Steps to play with Ollama and Models onPrem:

###### Download & Install Ollama
    https://ollama.com/download

###### Install Ollama CLI

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
