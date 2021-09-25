save_frequent = {}

def predict_bangla_text_to_english_text(bangla_text):
    if bangla_text not in save_frequent:
        english_text = translator.predict(bangla_text)
        save_frequent[bangla_text] = english_text # saving for later use
    else:
        return save_frequent[bangla_text]
    return english_text