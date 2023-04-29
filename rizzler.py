import openai
import gradio

openai.api_key = "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"

messages = [{"role": "system", "content": "You are a love experts that specializes in talking to women and flirting"}]

def CustomChatGPT(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    ChatGPT_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": ChatGPT_reply})
    return ChatGPT_reply

demo = gradio.Interface(fn=CustomChatGPT, inputs = "text", outputs = "text", title = "RizzGPT")

demo.launch(share=True)
