import os

# 📁 Dossier contenant les images
folder_path = "D:\\AnimalsCardImages\\animalsImageCard\\AnimalCards"

# 🔁 Parcourir tous les fichiers dans le dossier
for filename in os.listdir(folder_path):
    if filename.endswith(".png") and "#" in filename:
        new_filename = filename.replace("#", "")
        old_path = os.path.join(folder_path, filename)
        new_path = os.path.join(folder_path, new_filename)
        os.rename(old_path, new_path)
        print(f"✅ Renamed: {filename} → {new_filename}")
