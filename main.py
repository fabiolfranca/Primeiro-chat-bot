from chatbot import conversar
from tkinter import *
import threading

janela = Tk()
janela.geometry("600x600")
janela.title("Chatbot do Fabio")
janela.configure(bg="#2c2c2c")


label = Label(janela, text="Bem vindo ao Chatbot do Fabio!", font=("Arial", 12), bg="#2c2c2c", fg="white")
label.pack()



janela_resposta = Text(janela, height=30, width=70)
janela_resposta.tag_config("Usuario", foreground="blue", font=("Arial", 10, "bold"))
janela_resposta.tag_config("bot", foreground="#833F00", font=("Arial", 10, "bold"))
janela_resposta.tag_config("Usuario", justify=RIGHT)
janela_resposta.tag_config("bot", justify=LEFT)
janela_resposta.configure(bg="#c7c7c7")
janela_resposta.pack()





frame_input = Frame(janela, bg="#2c2c2c")
frame_input.pack(fill="x", padx=10, pady=10)


titulo_prompt = Label(frame_input, text="Digite sua pergunta abaixo:", font=("Arial", 10), bg="#2c2c2c", fg="white")
titulo_prompt.pack(anchor="w", padx=5)

frame_linha = Frame(frame_input, bg="#2c2c2c")
frame_linha.pack(fill="x", pady=5)

prompt = Entry(frame_input, width=65, bg="#e9e8e8")
prompt.pack(side=LEFT, fill=X, expand=True, padx=5)



def enviar_mensagem():
   pergunta = prompt.get()
   janela_resposta.insert(END, "Você: " , "Usuario")
   janela_resposta.insert(END, pergunta + "\n")
   janela_resposta.insert(END, "Chatbot: " + "Pensando..." + "\n", "bot")
   thread = threading.Thread(target=responder, args=(pergunta,))
   thread.start()
   prompt.delete(0, END)


def responder(pergunta):
    resposta = conversar(pergunta)
    janela_resposta.insert(END, "Chatbot: ", "bot")
    janela_resposta.insert(END, resposta + "\n")   


botao_enviar = Button(frame_input, text="Enviar", command=enviar_mensagem)
botao_enviar.pack(side=LEFT, padx=5)




botao_fechar = Button(frame_input, text="Fechar", command=janela.destroy)
botao_fechar.pack(side=LEFT, padx=5)



janela.mainloop()