import ollama
from transformers import BartForConditionalGeneration, BartTokenizer

import textwrap

def bart(text: str) -> str:

    model_name = "facebook/bart-large-cnn"
    model = BartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BartTokenizer.from_pretrained(model_name)
    max_length = max(50, int(0.2 * len(text)))
    print(max_length)

    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, min_length=50, length_penalty=1, num_beams=4, early_stopping=True)

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    print("in bart module: ", summary)
    #formatted_summary = "\n".join(textwrap.wrap(summary, width=80))
    return summary


def llm_summarizer(text: str) -> str:
    # Mistral 7B
    model = 'llama3:instruct'

    # Load the system prompt
    with open('C:\\Users\\Chloe\\Documents\\MaastrichtLaw&Tech\\Thesis\\MscThesis\\summ_pipeline\\abstractive_methods\\summ_sys_prompt.txt', 'r', encoding='utf-8') as file:
        sys_prompt = file.read()

    # Load the summarization prompt
    with open('C:\\Users\\Chloe\\Documents\\MaastrichtLaw&Tech\\Thesis\\MscThesis\\summ_pipeline\\abstractive_methods\\summ_prompt.txt', 'r', encoding='utf-8') as file:
        prompt = file.read() 

    # Get response
    response = ollama.chat(model=model, keep_alive=0, options={'temperature': 0.0, 'seed': 42, "top_p": 0.0}, messages=[
            {
                'role': 'system',
                'content': sys_prompt
            },
            {
                'role': 'user',
                'content': prompt + text
            },
        ])
    
    return response['message']['content']

