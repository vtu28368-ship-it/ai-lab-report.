# install openai first if not installed:
# pip install openai

import openai

openai.api_key = "sk-your_api_key_here"

completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user",
               "content": "Give me 3 ideas that I could build using OpenAI APIs"}]
)

print(completion.choices[0].message.content)


#b
import openai

openai.api_key = "sk-your_api_key_here"

messages = []
system_msg = input("What type of chatbot would you like to create?\n")
messages.append({"role": "system", "content": system_msg})

print("Your new assistant is ready! Type your query")
while input != "quit()":
    message = input()
    messages.append({"role": "user", "content": message})
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": reply})
    print("\n" + reply + "\n")


#c
    import openai
import gradio

openai.api_key = "sk-your_api_key_here"

messages = [{"role": "system", "content": "You are a financial expert that specializes in real estate investment and negotiation"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs="text", outputs="text", title="INTELLIGENT CHATBOT")
demo.launch(share=True)
