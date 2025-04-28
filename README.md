# YT-DL

## Description

**YT-DL** est un projet personnel utilisant Python qui permet de télécharger des fichiers audio (MP3) à partir de playlists YouTube.

**Avertissement :**  
Ce script est destiné à un usage personnel uniquement, conformément aux [Conditions d'utilisation de YouTube](https://www.youtube.com/t/terms). Veuillez vous assurer de respecter les lois sur le droit d'auteur et de ne télécharger que du contenu pour lequel vous avez les droits.

## Prérequis

Avant de commencer, vous devez installer les outils suivants :

1. **Python 3** :  
   Télécharge Python [ici](https://www.python.org/downloads/).

2. **yt-dlp** :  
   Un outil pour télécharger des vidéos et des playlists depuis YouTube et d'autres plateformes.
   - Installe-le via `pip` :
     ```bash
     pip install yt-dlp
     ```

3. **ffmpeg** :  
   Un outil multimédia nécessaire pour la conversion audio.
   - Installe-le via Homebrew (sur macOS) :
     ```bash
     brew install ffmpeg
     ```

## Installation

Clonez ce dépôt ou téléchargez les fichiers du projet.

```bash
git clone https://github.com/veverre/YT-DL.git
```

## Usage

Lancez le script avec la commande suivante :

```bash
python3 download_playlist.py
```

Ensuite, entrez l'URL de la playlist YouTube et le dossier où vous souhaitez enregistrer les fichiers audio.

## Fonctionnalités

- Télécharge les fichiers audio de playlists YouTube.
- Convertit les fichiers audio au format MP3 après le téléchargement.
- Vérifie si le fichier existe déjà dans le dossier de téléchargement avant de lancer le téléchargement.
- Ignore les vidéos privées et passe à la suivante sans interrompre le processus.