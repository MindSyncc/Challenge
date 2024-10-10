import openai
import os

openai_api_key = os.getenv("OPENAI_API_KEY")
'''sk-proj-9TAXK90muk0S86yCN41w4Su4qBAhNNxPcgVcIMWEWf_lGnvTUKBSH3egZ4__
-GBTQrQ0K4loaMT3BlbkFJ3TW0EP7grEUKeuqg5BVmjRE2h7SEw8koTBXjy0Es9veSIeV_
iXtoc6g2H-r5EUKjiw995jrJEA'''


def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Escolhe o modelo GPT-3
        prompt=prompt,
        max_tokens=150,  # Ajuste o limite de tokens conforme necessário
        n=1,  # Número de respostas
        stop=None,  # Onde a resposta deve parar
        temperature=0.7  # Criatividade da resposta
    )
    return response.choices[0].text.strip()


def formulae_chatbot():
    print("Olá! Eu sou o FormulaE Bot. Pergunte-me algo sobre a Fórmula E ou digite 'Sair' para encerrar.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == "sair":
            print("Bot: Até logo!")
            break
        # Envia a entrada do usuário para a API do ChatGPT
        response = chat_with_gpt(user_input)
        print(f"Bot: {response}")


formulae_chatbot()
