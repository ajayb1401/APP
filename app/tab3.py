from transformers import pipeline
pipe = pipeline(task='text2text-generation', model='facebook/m2m100_418M')
def text_translate(text, target_lang):
    translated_text =pipe(text, forced_bos_token_id=pipe.tokenizer.get_lang_id(lang=target_lang))
    generated_text = translated_text[0]['generated_text']
    return generated_text