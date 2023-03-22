import openai
openai.api_key = "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"
openai.organization = "org-FPcSNLlNyG3rezPYeHPLT3BlbkFJpmCjcd4hZhyrTeNFtoGr"
def generate_response(prompt):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )
    message = completion.choices[0].message.content.strip()
    return message
