import yt_dlp
import os
import inquirer

# Fonction pour télécharger l'audio d'une vidéo
def download_audio(url, download_path, format, quality):
    # Configuration des options de téléchargement

    postprocessor = {
        'key': 'FFmpegExtractAudio',  # Nom du post-processeur correct
        'preferredcodec': format,  # Le format désiré
    }

    if quality:
        postprocessor['preferredquality'] = quality

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [postprocessor],
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),  # Nom du fichier de sortie (titre de la vidéo)
        'quiet': False,  # Affiche les logs (si True, tout sera silencieux)
    }

    # Télécharger la vidéo (ou la playlist) avec les options spécifiées
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # Tenter d'extraire les informations de la vidéo avant de la télécharger
        info_dict = ydl.extract_info(url, download=False)
        title = info_dict.get('title', None)
        filename = os.path.join(download_path, f"{title}.mp3")

        # Vérifier si le fichier existe déjà
        if os.path.exists(filename):
            print(f"Le fichier {filename} existe déjà, vidéo ignorée.")
            return  # Passer à la vidéo suivante si le fichier existe

        try:
            ydl.download([url])
        except yt_dlp.utils.DownloadError as e:
            print(f"Erreur pour la vidéo {url}: {e}, vidéo ignorée.")

# Fonction pour télécharger une playlist YouTube
def download_playlist(playlist_url, download_path, format, quality):
    # Vérifie si le dossier de destination existe, sinon le crée
    if not os.path.exists(download_path):
        os.makedirs(download_path)  # Créer le dossier si nécessaire

    # Lance le téléchargement de la playlist
    download_audio(playlist_url, download_path, format, quality)

# Point d'entrée du script
if __name__ == "__main__":
    # Demander à l'utilisateur l'URL de la playlist YouTube
    playlist_url = input("Enter YouTube playlist URL: ")
    
    # Demander à l'utilisateur le chemin où sauvegarder les fichiers audio
    download_path = input("Enter the folder to save the audio files: ")

    formatList = [
        inquirer.List('format',
            message="Quel format audio voulez-vous?",
            choices=[
                'mp3',
                'wav',
            ],
        ),
    ]

    format = inquirer.prompt(formatList)['format']

    qualityList = [
        inquirer.List('quality',
            message="Quelle qualité audio voulez-vous?",
            choices=[
                '128k',
                '192k',
                '256k',
                '320k',
            ],
        ),
    ]

    if format == 'mp3':
        quality = inquirer.prompt(qualityList)['quality']
    else:
        quality = None
    
    # Télécharger la playlist
    download_playlist(playlist_url, download_path, format, quality)