from PIL import Image
import os
import requests
from io import BytesIO


def download_image(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Lève une exception si la requête échoue

        # Ouvrir l'image à partir du contenu de la réponse
        img = Image.open(BytesIO(response.content))
        return img
    except Exception as e:
        print(f"Une erreur s'est produite lors du téléchargement de l'image : {e}")
        return None


def resize_image(image, output_folder):
    if image is None:
        return

    # Tailles et noms spécifiés
    sizes = [
        ((32, 32), "32x32.png"),
        ((128, 128), "128x128.png"),
        ((256, 256), "128x128@2x.png"),
        ((512, 512), "icon.png"),
        ((30, 30), "Square30x30Logo.png"),
        ((44, 44), "Square44x44Logo.png"),
        ((71, 71), "Square71x71Logo.png"),
        ((89, 89), "Square89x89Logo.png"),
        ((107, 107), "Square107x107Logo.png"),
        ((142, 142), "Square142x142Logo.png"),
        ((150, 150), "Square150x150Logo.png"),
        ((284, 284), "Square284x284Logo.png"),
        ((310, 310), "Square310x310Logo.png"),
        ((50, 50), "StoreLogo.png"),
    ]

    # Redimensionner et enregistrer les images
    for size, name in sizes:
        # Redimensionner l'image
        resized_img = image.resize(size)
        resized_img.save(os.path.join(output_folder, name), format="PNG")

    # Créer le fichier ICO
    ico_sizes = [(32, 32)]
    image.save(os.path.join(output_folder, "icon.ico"), format="ICO", sizes=ico_sizes)

    # Créer le fichier ICNS
    icns_sizes = [(32, 32), (16, 16), (1024, 1024), (512, 512), (256, 256)]
    image.save(
        os.path.join(output_folder, "icon.icns"), format="ICNS", sizes=icns_sizes
    )


# Demander à l'utilisateur de saisir le chemin de l'image ou le lien Internet
image_input = input("Veuillez entrer le chemin de l'image ou le lien Internet : ")

# Vérifier si l'entrée est un lien Internet ou un chemin local
if image_input.startswith("http://") or image_input.startswith("https://"):
    image = download_image(image_input)
else:
    # Vérifier si le chemin de l'image est valide
    if not os.path.exists(image_input):
        print("Le chemin de l'image spécifié est invalide.")
        exit()

    # Ouvrir l'image depuis le chemin local
    image = Image.open(image_input)

# Dossier de sortie
output_folder = "icon_folder"

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Appel de la fonction pour redimensionner l'image
resize_image(image, output_folder)
