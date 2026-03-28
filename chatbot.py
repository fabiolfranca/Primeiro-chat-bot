from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate


model = OllamaLLM(model="mistral")
prompt = PromptTemplate.from_template("Usuario: {pergunta} \nIA: ")
chain = prompt | model


def conversar(pergunta):
    resposta = chain.invoke({"pergunta": pergunta})
    return resposta


