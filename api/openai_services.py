import openai



def optimize_seo_with_chatgpt(transcriptions):
    # Prepare the text for ChatGPT
    chatgpt_input = ' '.join(transcriptions)

    # Use ChatGPT to optimize SEO
    chatgpt_response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=chatgpt_input,
        max_tokens=200
    )

    optimized_text = chatgpt_response.choices[0].text.strip()
    return optimized_text
