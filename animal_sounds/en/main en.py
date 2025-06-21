from gtts import gTTS
import os

# Liste des noms en anglais
animal_names = [
    "Lion", "Elephant", "Bear", "Fox", "Deer", "Rabbit", "Horse", "Dog", "Cat", "Pig", "Goat",
    "Donkey", "Camel", "Crocodile", "Snake", "Shark", "Hippopotamus", "Buffalo", "Coyote",
    "Flamingo", "Gazelle", "Hamster", "Jaguar", "Leopard", "Lynx", "Monkey", "Ostrich", "Parrot",
    "Pigeon", "Rat", "Turtle", "Whale", "Boar", "Octopus", "Seal", "Dolphin", "Lizard", "Seagull",
    "Wolf", "Crow", "Doe", "Orca", "Buzzard", "Tiger", "Bull", "Iguana", "Frog", "Butterfly",
    "Spider", "Duck", "Penguin", "Giraffe", "Cow", "Sheep", "Rhinoceros", "Chicken", "Owl"
]

# Crée un dossier de sortie s'il n'existe pas
output_folder = "audio_en"
os.makedirs(output_folder, exist_ok=True)

# Génère les fichiers audio
for name in animal_names:
    name_lower = name.lower()
    filename = f"{name_lower} en.mp3"
    path = os.path.join(output_folder, filename)
    
    tts = gTTS(text=name, lang='en')
    tts.save(path)
    print(f"Généré : {filename}")
