# chatbot.py

import random

def get_bot_response(user_input):
    responses = {
        "oi": "Olá, como posso ajudar?",
        "como você está?": "Estou bem, obrigado por perguntar!",
        "tchau": "Até logo!",
    }

    return responses.get(user_input.lower(), "Desculpe, não entendi o que você quis dizer.")

def chatbot():
    print("Olá! Sou um chatbot simples. Digite 'tchau' para sair.")
    
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "tchau":
            print("Chatbot: Até logo!")
            break
        response = get_bot_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()

