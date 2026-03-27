Hier ist die komplette README.md. Der englische Teil ist der Standard-Text, den man sofort sieht, während die deutsche und französische Version jeweils in einem eigenen, ausklappbaren Bereich darunter liegen.

Markdown
# 📸 AI Photo Sorter

An intelligent Python script to analyze and sort your photos using local AI models via Ollama. It handles modern formats like HEIC and ensures Apple Live Photos stay intact.

---

## 🇬🇧 English (Main Guide)

### ✨ Features
* **AI Analysis:** Uses vision models to understand image content and categorize them.
* **HEIC Support:** Automatic conversion of Apple HEIC files to JPG for processing.
* **Live Photo Support:** Automatically detects and moves `.mov` files if they share the same name as an image.
* **Local & Private:** Everything runs on your machine; no photos are uploaded to the cloud.

### 📋 Prerequisites
1. **Python 3.10+**
2. **Ollama** installed and running (Download at [ollama.com](https://ollama.com))

### 🛠 Installation & Usage
1. **Install dependencies:**
   ```bash
   python install.py
Prepare photos: Place your images (JPG, HEIC) and Live Photo videos (MOV) in the /photos_input folder.

Run the script:

Bash
python run.py
The script will prompt you for:

Model Name: (e.g., llama3.2-vision)

Prompt: (e.g., "Sort these photos into folders based on their content.")

💡 Recommended Models
High Performance: llama3.2-vision (Highly recommended for accuracy)

Budget/Old PC: llava or moondream (Faster on less powerful hardware)

<details>
<summary>🇩🇪 <b>Deutsch (Übersetzung anzeigen)</b></summary>

✨ Funktionen
KI-Analyse: Nutzt Vision-Modelle, um Bildinhalte zu verstehen und zu kategorisieren.

HEIC-Unterstützung: Automatische Konvertierung von Apple HEIC-Dateien in JPG.

Live-Photo Support: Erkennt .mov-Dateien automatisch und verschiebt sie zusammen mit dem passenden Bild.

Lokal & Privat: Alles läuft auf deinem eigenen Rechner; keine Fotos verlassen dein System.

📋 Voraussetzungen
Python 3.10+

Ollama installiert (Download unter ollama.com)

🛠 Installation & Benutzung
Abhängigkeiten installieren:

Bash
python install.py
Fotos vorbereiten: Kopiere deine Bilder und Videos in den Ordner /photos_input.

Skript starten:

Bash
python run.py
Das Skript fragt dich nach dem Modell-Namen und dem Prompt für die Sortierung.

💡 Empfohlene Modelle
Beste Ergebnisse: llama3.2-vision

Schwächere PCs: llava oder moondream

</details>

<details>
<summary>🇫🇷 <b>Français (Afficher la traduction)</b></summary>

✨ Caractéristiques
Analyse IA : Utilise des modèles de vision pour comprendre et classer le contenu des images.

Support HEIC : Conversion automatique des fichiers Apple HEIC en JPG.

Support Live Photo : Détecte et déplace les fichiers .mov associés aux images portant le même nom.

Local & Privé : Tout s'exécute localement sur votre machine.

📋 Prérequis
Python 3.10+

Ollama (Télécharger sur ollama.com)

🛠 Installation et Utilisation
Installer les dépendances :

Bash
python install.py
Préparer les photos : Placez vos images dans le dossier /photos_input.

Lancer le script :

Bash
python run.py
Le script vous demandera le Nom du modèle et le Prompt.

💡 Modèles recommandés
Haute performance : llama3.2-vision

PC moins puissants : llava ou moondream

</details>