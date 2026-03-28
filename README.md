# 🤖 Chatbot com IA Local (Mistral + Ollama)

Este projeto é um chatbot com interface gráfica desenvolvido em Python, utilizando um modelo de linguagem local.

## 🚀 Tecnologias utilizadas

- Python
- Tkinter (interface gráfica)
- LangChain
- Ollama
- Mistral (modelo de linguagem)

## 🧠 Sobre o projeto

O chatbot funciona de forma 100% local, utilizando o modelo Mistral através do Ollama, sem necessidade de API externa.

A interface foi construída com Tkinter, permitindo interação simples e direta com o modelo.

## 💻 Funcionalidades

- Envio de mensagens via interface gráfica
- Respostas geradas por IA local
- Execução em thread (não trava a interface)
- Diferenciação visual entre usuário e chatbot

## ⚙️ Como executar

1. Instale o Ollama:
https://ollama.com

2. Baixe o modelo Mistral:
  bash
  ollama pull mistral

3. Clone o repositório:
   git clone <seu-repo>
   cd <seu-repo>

4. Crie um ambiente virtual (opcional):
   python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows

5. Instale as dependências:
   pip install langchain langchain-ollama

6. Execute o projeto:
   python main.py

## Observações
- O modelo roda localmente, podendo consumir bastante memória dependendo da máquina.
- O tempo de resposta pode variar conforme o hardware.

<img width="597" height="630" alt="image" src="https://github.com/user-attachments/assets/6e1b4b0b-ee2f-45a7-bfde-51c4a72bc116" />


## Aprendizados

 Este projeto foi desenvolvido com foco em aprendizado de:

- Integração com modelos de linguagem
- Interfaces gráficas em Python
- Execução assíncrona com threads
