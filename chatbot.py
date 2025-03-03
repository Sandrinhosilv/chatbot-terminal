# chatbot.py

import random

def greet():
    greetings = ["Olá!", "Oi!", "Como vai?", "Oi, tudo bem?"]
    return random.choice(greetings)

def respond_to_query(query):
    responses = {
        "como você está?": "Estou bem, obrigado por perguntar!",
        "qual o seu nome?": "Eu sou um chatbot criado no terminal.",
        "adeus": "Até logo! Foi bom conversar com você!",
    }

    # Se a pergunta for conhecida, retorna a resposta, caso contrário, uma resposta padrão
    return responses.get(query.lower(), "Desculpe, não entendi sua pergunta.")

def chatbot():
    print("Olá! Sou um chatbot. Digite 'adeus' para sair.")
    while True:
        query = input("Você: ")
        if query.lower() == "adeus":
            print("Chatbot: Até logo!")
            break
        elif query.lower() in ["olá", "oi", "como vai"]:
            print("Chatbot:", greet())
        else:
            print("Chatbot:", respond_to_query(query))

if __name__ == "__main__":
    chatbot()
