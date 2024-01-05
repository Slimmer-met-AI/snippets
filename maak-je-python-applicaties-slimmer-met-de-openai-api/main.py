# 1. Importeer de openai module
from openai import OpenAI

# 2. Maar een OpenAI client aan
client = OpenAI()

# 3. Kies een model
model = 'gpt-3.5-turbo'

# 4. Maak een initialisatiestring aan, dit is de instructie aan het model
initialization = "You are now louis C.K. Every prompt that you receive, you answer with blunt, self-deprecating humor." 

# 5. Vraag de gebruiker om een prompt
user_prompt = input('Prompt: ')

# 6. Stel de temperatuur - oftewel de randomness - van het model in
temperature = 0.1

# 7. Roep de API aan en haal het antwoord op
answer = client.chat.completions.create(
    model = model,
    messages=[
        {'role': 'system', 'content': initialization},
        {'role': 'user', 'content': user_prompt}
    ],
    temperature = temperature,
).choices[0].message.content

# 8. Print het antwoord
print(answer)