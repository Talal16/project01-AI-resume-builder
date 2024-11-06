import openai 
import os
        


openai.api_key = os.getenv("OPENAI_API_KEY")

# openai.api_key  = "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"


completion = openai.ChatCompletion.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
    ]
)

print(completion.choices[0].message)