# openai the company created a package to use everything which we want to use to use the automated stuff.
import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Give me 3 ideas for apps I could build with openai apis "}])
print(completion.choices[0].message.content)