from transformers import pipeline  # Import the pipeline function from the transformers library

# Load pre-trained translation pipelines from Hugging Face
# These pipelines use models for translating text between English and German.
# The 'translation_en_to_de' pipeline translates from English to German.
translator_en_de = pipeline("translation_en_to_de", model="Helsinki-NLP/opus-mt-en-de")
# The 'translation_de_to_en' pipeline translates from German to English.
translator_de_en = pipeline("translation_de_to_en", model="Helsinki-NLP/opus-mt-de-en")

def translate_prompt_based(text: str, src_lang: str, tgt_lang: str) -> str:
    """
    Translate text from source language (src_lang) to target language (tgt_lang) using a prompt-based model.
    Supported language pairs: 'en' <-> 'de'
    
    :param text: The text that needs to be translated.
    :param src_lang: The source language code ('en' for English, 'de' for German).
    :param tgt_lang: The target language code ('en' for English, 'de' for German).
    :return: The translated text as a string.
    :raises ValueError: If the specified language pair is unsupported.
    """
    # Check if source and target languages are the same
    if src_lang == tgt_lang:
        # If both languages are the same, return the original text
        return text
    
    # Check the source and target languages to determine which translation pipeline to use
    if src_lang == 'en' and tgt_lang == 'de':
        # If translating from English to German, use the English-to-German pipeline
        translated_text = translator_en_de(text)[0]['translation_text']
    elif src_lang == 'de' and tgt_lang == 'en':
        # If translating from German to English, use the German-to-English pipeline
        translated_text = translator_de_en(text)[0]['translation_text']
    else:
        # Raise an error if the specified language pair is not supported
        raise ValueError("Unsupported language pair")

    # Return the translated text
    return translated_text
