from transformers import MarianMTModel, MarianTokenizer
import pandas as pd # Added this line

# Install sacremoses if not already installed
try:
    import sacremoses
except ImportError:
    !pip install sacremoses
    import sacremoses

# Urdu to English
print("Model is loading....")
UR_EN_Model = "Helsinki-NLP/opus-mt-ur-en"

tokenizer1 = MarianTokenizer.from_pretrained(UR_EN_Model)
MTmodel1 = MarianMTModel.from_pretrained(UR_EN_Model)

print("Model (Urdu to English) is Loaded")

# English to Urdu
EN_UR_Model = "Helsinki-NLP/opus-mt-en-ur"

tokenizer2 = MarianTokenizer.from_pretrained(EN_UR_Model)
MTmodel2 = MarianMTModel.from_pretrained(EN_UR_Model)

print("Model (English to Urdu) is Loaded")


def translate(text, direction="ur_en"):

    if direction == "ur_en":
        model = MTmodel1
        tokenizer = tokenizer1

    elif direction == "en_ur":
        model = MTmodel2
        tokenizer = tokenizer2

    else:
        print("Invalid Direction")
        return

    
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)

    
    translated_tokens = model.generate(**inputs, num_beams=4, early_stopping=True)

    result = tokenizer.decode(translated_tokens[0], skip_special_tokens=True)

    print("𝓘𝓷𝓹𝓾𝓽:", text)
    print("𝓞𝓾𝓽𝓹𝓾𝓽:", result)
    print("-"*20)

    return result

translate("Consistency and practice are the keys to becoming a good programmer.", "en_ur")

translate("اگر ہم مسلسل محنت کریں تو کوئی بھی ہنر سیکھنا مشکل نہیں ہوتا۔", "ur_en")

