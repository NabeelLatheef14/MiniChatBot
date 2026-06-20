# MiniChatBot
MiniChatBot is a chat bot application created using 'Llama' LLM model by Meta. This repo will be having the basic configurations and the instructions for the configurations.

## Requirements
1. Python
2. Ollama
3. Llama

## Python Installation

Download and install python from https://www.python.org/downloads.

Install Ollama Client Library
```bash
pip install ollama
```
Install Streamlit for UI design $\color{red}{\textsf{**Not Mandatory}}$
```bash
pip install streamlit
```

## Ollama Installation

Navigate to Ollama official website https://ollama.com/download and download OllamaSetup file according to your operating system

OR

For Windows Run the below command in powershell

```bash
irm https://ollama.com/install.ps1 | iex
```

For Linux/MacOs Run the below command in terminal

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Note:** _It is recommended to install it using terminal commands as sometimes system will not allow the users to insall the setup file._

Ensure Ollama is running sucessfully post the installation.
<br/><img width="335" height="172" alt="image" src="https://github.com/user-attachments/assets/0be0cef0-529e-4a72-9f2b-f239f93edd84" />

## Llama Installation

We will be using Llama 3.2 for this project, please feel free to use any other models available in the Ollama models. Visit: https://ollama.com/search
To install Llama 3.2 run the below command in terminal/powershell
```bash
ollama pull llama3.2
```
_If it is throwing error saying ollama is not idenfied, then try restarting the powershell or terminal._
<br/><img width="1895" height="101" alt="image" src="https://github.com/user-attachments/assets/63e16bb0-4e30-4ce8-b068-7fa9b0dc5ac6" />
<br/><img width="1698" height="256" alt="image" src="https://github.com/user-attachments/assets/1759c073-2242-4815-b25c-2421d2fd02e8" />

