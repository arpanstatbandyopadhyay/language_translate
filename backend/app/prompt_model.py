from transformers import pipeline

# Load pre-trained translation pipelines from Hugging Face
translator_en_de = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")
translator_de_en = pipeline("translation_de_to_en", model="Helsinki-NLP/opus-mt-de-en")

def translate_prompt_based(text: str, src_lang: str, tgt_lang: str) -> str:
    """
    Translate text from source language (src_lang) to target language (tgt_lang) using prompt-based model.
    Supported language pairs: 'en' <-> 'de'
    """
    if src_lang == 'en' and tgt_lang == 'de':
        translated_text = translator_en_de(text)[0]['translation_text']
    elif src_lang == 'de' and tgt_lang == 'en':
        translated_text = translator_de_en(text)[0]['translation_text']
    else:
        raise ValueError("Unsupported language pair")

    return translated_text
