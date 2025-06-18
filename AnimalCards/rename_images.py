import os

# Dossier contenant les images
folder_path = "./"  # Change si nécessaire

# Étape 1 : Renommage temporaire pour éviter les conflits
for i in range(56, 0, -1):  # De 56 à 1
    old_name = f"ImageAnimal-{i}.png"
    temp_name = f"temp-{i + 1}.png"
    old_path = os.path.join(folder_path, old_name)
    temp_path = os.path.join(folder_path, temp_name)

    if os.path.exists(old_path):
        os.rename(old_path, temp_path)

# Étape 2 : Renommage définitif
for i in range(2, 58):  # De temp-2 à temp-57
    temp_name = f"temp-{i}.png"
    final_name = f"ImageAnimal-{i}.png"
    temp_path = os.path.join(folder_path, temp_name)
    final_path = os.path.join(folder_path, final_name)

    if os.path.exists(temp_path):
        os.rename(temp_path, final_path)

print("✅ Fichiers renommés de ImageAnimal-1 → ImageAnimal-2 jusqu'à ImageAnimal-56 → ImageAnimal-57.")
