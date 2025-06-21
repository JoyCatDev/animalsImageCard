from gtts import gTTS
import os

# Dictionnaire: Français -> Anglais
animal_names = {
    "Lion": "lion",
    "Éléphant": "elephant",
    "Ours": "bear",
    "Renard": "fox",
    "Cerf": "deer",
    "Lapin": "rabbit",
    "Cheval": "horse",
    "Chien": "dog",
    "Chat": "cat",
    "Cochon": "pig",
    "Chèvre": "goat",
    "Âne": "donkey",
    "Chameau": "camel",
    "Crocodile": "crocodile",
    "Serpent": "snake",
    "Requin": "shark",
    "Hippopotame": "hippopotamus",
    "Buffle": "buffalo",
    "Coyote": "coyote",
    "Flamant rose": "flamingo",
    "Gazelle": "gazelle",
    "Hamster": "hamster",
    "Jaguar": "jaguar",
    "Léopard": "leopard",
    "Lynx": "lynx",
    "Singe": "monkey",
    "Autruche": "ostrich",
    "Perroquet": "parrot",
    "Pigeon": "pigeon",
    "Rat": "rat",
    "Tortue": "turtle",
    "Baleine": "whale",
    "Sanglier": "boar",
    "Poulpe": "octopus",
    "Phoque": "seal",
    "Dauphin": "dolphin",
    "Lézard": "lizard",
    "Mouette": "seagull",
    "Loup": "wolf",
    "Corbeau": "crow",
    "Cerf (ou Biche)": "doe",
    "Orque": "orca",
    "Buse": "buzzard",
    "Tigre": "tiger",
    "Taureau": "bull",
    "Iguane": "iguana",
    "Grenouille": "frog",
    "Papillon": "butterfly",
    "Araignée": "spider",
    "Canard": "duck",
    "Pingouin": "penguin",
    "Girafe": "giraffe",
    "Vache": "cow",
    "Mouton": "sheep",
    "Rhinocéros": "rhinoceros",
    "Poule": "chicken",
    "Hibou": "owl"
}

# Créer le dossier de sortie
output_folder = "audio_fr"
os.makedirs(output_folder, exist_ok=True)

# Génération des voix
for fr_name, en_name in animal_names.items():
    filename = f"{en_name.lower()} fr.mp3"
    filepath = os.path.join(output_folder, filename)

    tts = gTTS(text=fr_name, lang='fr')
    tts.save(filepath)
    print(f"Généré : {filename}")
