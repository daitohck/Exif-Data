import sys
from PIL import Image, ExifTags
from moviepy.editor import VideoFileClip

def afficher_metadonnees_fichier(fichier_path):
    try:
        if fichier_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
            img = Image.open(fichier_path)
            exif_data = img._getexif()

            if exif_data is not None:
                print("Métadonnées de l'image:")
                for tag, value in exif_data.items():
                    tag_name = ExifTags.TAGS.get(tag, tag)
                    print(f"{tag_name}: {value}")
            else:
                print("Aucune métadonnée EXIF trouvée dans l'image.")
            
            img.close()
        elif fichier_path.lower().endswith(('.mp4', '.avi', '.mov')):
            clip = VideoFileClip(fichier_path)
            print("Métadonnées de la vidéo:")
            print(f"Durée: {clip.duration} secondes")
            print(f"Largeur: {clip.size[0]} pixels")
            print(f"Hauteur: {clip.size[1]} pixels")
            print(f"FPS (images par seconde): {clip.fps}")
            clip.close()
        else:
            print("Format de fichier non pris en charge.")

    except Exception as e:
        print(f"Erreur: {e}")

if len(sys.argv) != 2:
    print("Veuillez fournir le chemin d'un fichier (image ou vidéo) en tant qu'argument.")
    sys.exit(1)
fichier_path = sys.argv[1]

afficher_metadonnees_fichier(fichier_path)