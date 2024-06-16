# Recursive GPT Code Generator
## Generate code snippets recursively using OpenAI GPT API
## Optimize existing scripts
* Python + OpenAI API (include .env file with key)
* Run in Python virtual environment
* main.py is advanced script generation
* pip install -r requirements.txt
* Scripts saved in /gen_code

# Useage
* Options:
* Generate from scratch / load an existing script / continue from previous iteration

## Generate from scratch
* Example Use - create a script to generate a custom Linux desktop file manager:
![Update code idea and language](https://github.com/PointlessAI/recursive-gpt/blob/master/img/linux_gui.png)
* After 5 iterations:
![Desktop File Manager](https://github.com/PointlessAI/recursive-gpt/blob/master/img/desktop-file-manager.png)

## Load from existing
* Example Use - Read and recursively enhance an existing script:
![Set file load path](https://github.com/PointlessAI/recursive-gpt/blob/master/img/existing_0.jpg)
* After 5 iterations:
![Happy AI](https://github.com/PointlessAI/recursive-gpt/blob/master/img/existing_1.jpg)

## Testing Options
* Generated scripts are tested on the fly. If a script produces a GUI or runs a long time then it is best to test through compiling only.
* Select static (compile only) or dynamic (exec ful script) testing depending on requirements:
![Select testing method](https://github.com/PointlessAI/recursive-gpt/blob/master/img/testing.jpg)
* After 5 iterations:
![Pong](https://github.com/PointlessAI/recursive-gpt/blob/master/img/testing2.jpg)