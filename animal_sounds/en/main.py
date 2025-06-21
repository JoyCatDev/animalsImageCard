from gtts import gTTS
import os

# Liste en Tifinagh (dans le même ordre que la traduction anglaise)
tifinagh_list = [
    "ⵉⵣⴻⵎ", "ⵉⵍⵓ", "ⴰⵊⴳⴻⵍⴰⵍ", "ⴰⴱⴰⵔⴻⵖ", "ⵉⵣⴻⵣⴻⵔ", "ⴰⵡⵜⵓⵍ", "ⴰⵄⵓⴷⵉⵡ", "ⴰⵇⵛⵓⵏ", "ⴰⵎⵛⵉⵛ",
    "ⴰⵃⴰⵍⵓⴼ", "ⵜⴰⵖⴰⵜⵜ", "ⴰⵖⵢⵓⵍ", "ⵉⵍⵖⴻⵎ", "ⴰⵖⵓⵛⴰⴼ", "ⴰⵣⵔⴻⵎ", "ⴰⵡⴻⵇⴳⴰⵙ", "ⴰⴱⴰⵏⵄⵓ", "ⵜⴰⵍⴻⵀⵎⵓⵙⵜ",
    "ⴰⴽⵓⵢⵓⵜ", "ⴰⴼⵍⴰⵎⵉⵏⴳⵓ", "ⵜⵉⵣⵔⵣⵔⵜ", "ⴰⵃⴰⵎⵙⵜⴻⵔ", "ⴰⴳⵉⵡ", "ⴰⵎⵢⴰⵙ", "ⴰⵎⵛⵉⵛ ⵍⴰⵅⵍⴰ", "ⵉⵯⴻⴽⴽⵉ", "ⴰⵏⵃⵉⵍ",
    "ⴱⴰⴱⴰⵖⴰⵢⵓ", "ⴰⵜⵓⵡⵉⵔ", "ⴰⵖⴻⵔⴷⴰ", "ⴰⴼⴻⴽⵔⵓⵏ", "ⵜⵉⵣⵎⴽⵜ", "ⵉⵍⴻⴼ", "ⵇⵉⵔⵏⵉⵜ", "ⴰⴷⴻⵎⵔⵉ", "ⴰⵣⵢⴰⵎ",
    "ⴰⵃⴻⵔⴱⴻⴱⴱⵓ", "ⴱⵓⴼⵇ", "ⵓⵛⴻⵏ", "ⴰⴱⴰⵖⵔⵉⵡ", "ⵜⴰⴳⵓⵡⵣⴰⵍⵜ", "ⵓⵔⴽⴰ", "ⵍⴻⵍⵍⴰⵥ", "ⴰⴽⵙⴻⵍ", "ⴰⵣⴳⴻⵔ", "ⵉⴳⵓⴰⵏ",
    "ⴰⵎⵇⴻⵕⵇⵓⵕ", "ⴰⴼⴻⵔⵜⴻⵟⵟⵓ", "ⵜⵉⵙⵙⵉⵙⵜ", "ⴰⴱⵔⵉⴽ", "ⴰⵡⴰⵙ", "ⴰⵎⴷⴻⵖ", "ⵜⴰⴼⵓⵏⴰⵙⵜ", "ⵉⵣⵉⵎⵎⴻⵔ",
    "ⴰⵖⵉⵍⴰⵙ ⵏ ⵓⴹⴰⵔ", "ⵜⵀⴰⵢⴰⵣⴻⵜ", "ⴰⵟⵟⴰⵙ"
]

# Traductions exactes en anglais (dans le même ordre)
english_names = [
    "Lion", "Elephant", "Bear", "Fox", "Deer", "Rabbit", "Horse", "Dog", "Cat", "Pig", "Goat", "Donkey",
    "Camel", "Crocodile", "Snake", "Shark", "Hippopotamus", "Buffalo", "Coyote", "Flamingo", "Gazelle",
    "Hamster", "Jaguar", "Leopard", "Lynx", "Monkey", "Ostrich", "Parrot", "Pigeon", "Rat", "Turtle",
    "Whale", "Boar", "Octopus", "Seal", "Dolphin", "Lizard", "Seagull", "Wolf", "Crow", "Doe", "Orca",
    "Buzzard", "Tiger", "Bull", "Iguana", "Frog", "Butterfly", "Spider", "Duck", "Penguin", "Giraffe",
    "Cow", "Sheep", "Rhinoceros", "Chicken", "Owl"
]

# Dossier de sortie
output_folder = "tifinagh_audio_tf"
os.makedirs(output_folder, exist_ok=True)

# Boucle de génération
for tif_word, eng_name in zip(tifinagh_list, english_names):
    filename = f"{eng_name.lower()} tf.mp3"
    filepath = os.path.join(output_folder, filename)
    try:
        print(f"🎙️ Génération de : {filename}")
        tts = gTTS(text=eng_name, lang='en')
        tts.save(filepath)
    except Exception as e:
        print(f"❌ Erreur pour {eng_name}: {e}")
