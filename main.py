import os
import requests

animals = [
    "lion", "elephant", "bear", "fox", "deer", "rabbit", "horse", "dog", "cat", "pig", "goat", "chicken",
    "donkey", "camel", "crocodile", "snake", "shark", "hippopotamus", "buffalo", "coyote", "flamingo", "gazelle",
    "hamster", "jaguar", "leopard", "lynx", "monkey", "ostrich", "parrot", "pigeon", "rat", "turtle", "whale",
    "boar", "octopus", "seal", "dolphin", "lizard", "seagull", "wolf", "crow", "doe", "orca", "buzzard", "tiger",
    "bull", "iguana", "frog", "butterfly", "spider", "duck", "penguin", "giraffe", "cow", "sheep", "rhinoceros"
]

os.makedirs("animal_sounds", exist_ok=True)

for animal in animals:
    url = f"https://www.google.com/logos/fnbx/animal_sounds/{animal}.mp3"
    try:
        print(f"Downloading: {animal}")
        r = requests.get(url)
        if r.status_code == 200:
            with open(f"animal_sounds/{animal}.mp3", "wb") as f:
                f.write(r.content)
        else:
            print(f"Failed to download: {animal}")
    except Exception as e:
        print(f"Error with {animal}: {e}")
