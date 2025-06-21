from gtts import gTTS
import os

# Mots en arabe et leurs traductions en anglais pour les noms de fichiers
arabic_names = [
    "أسد", "فيل", "دب", "ثعلب", "غزال", "أرنب", "حصان", "كلب", "قطة", "خنزير",
    "ماعز", "حمار", "جمل", "تمساح", "ثعبان", "قرش", "فرس النهر", "جاموس", "كايوتي",
    "فلامنغو", "غزال", "هامستر", "اليغور", "فهد", "الوشق", "قرد", "نعامة", "ببغاء",
    "حمامة", "فأر", "سلحفاة", "حوت", "خنزير بري", "أخطبوط", "فقمة", "دلفين", "سحلية",
    "نورس", "ذئب", "غراب", "غزال", "حوت أوركا", "باز", "نمر", "ثور", "إغوانا", "ضفدع",
    "فراشة", "عنكبوت", "بطة", "بطريق", "زرافة", "بقرة", "خروف", "وحيد القرن", "دجاجة", "بومة"
]

english_names = [
    "lion", "elephant", "bear", "fox", "deer", "rabbit", "horse", "dog", "cat", "pig",
    "goat", "donkey", "camel", "crocodile", "snake", "shark", "hippopotamus", "buffalo", "coyote",
    "flamingo", "gazelle", "hamster", "jaguar", "leopard", "lynx", "monkey", "ostrich", "parrot",
    "pigeon", "rat", "turtle", "whale", "boar", "octopus", "seal", "dolphin", "lizard",
    "seagull", "wolf", "crow", "doe", "orca", "buzzard", "tiger", "bull", "iguana", "frog",
    "butterfly", "spider", "duck", "penguin", "giraffe", "cow", "sheep", "rhinoceros", "chicken", "owl"
]

# Dossier de sortie
output_folder = "audio_ar"
os.makedirs(output_folder, exist_ok=True)

# Générer les fichiers audio
for arabic, english in zip(arabic_names, english_names):
    file_name = f"{english.lower()} ar.mp3"
    file_path = os.path.join(output_folder, file_name)

    tts = gTTS(text=arabic, lang='ar')
    tts.save(file_path)
    print(f"Généré : {file_name}")
