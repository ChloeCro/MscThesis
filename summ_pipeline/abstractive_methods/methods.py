from transformers import BartForConditionalGeneration, BartTokenizer
import textwrap

def bart(text: str) -> str:

    model_name = "facebook/bart-large-cnn"
    model = BartForConditionalGeneration.from_pretrained(model_name)
    tokenizer = BartTokenizer.from_pretrained(model_name)

    inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
    summary_ids = model.generate(inputs, max_length=500, min_length=300, length_penalty=1, num_beams=4, early_stopping=True)

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    print("in bart module: ", summary)
    #formatted_summary = "\n".join(textwrap.wrap(summary, width=80))
    return summary