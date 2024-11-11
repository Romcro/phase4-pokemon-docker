# Utilise une image de base Python légère
FROM python:3.12-slim

# Installer les dépendances système pour tkinter, pygame, et Pillow
RUN apt-get update && apt-get install -y \
    python3-tk \
    libgl1-mesa-glx \
    libjpeg-dev \
    libtiff-dev \
    libsdl2-dev \
    libsdl2-image-dev \
    libsdl2-mixer-dev \
    libsdl2-ttf-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Créer un environnement virtuel et l'activer
RUN python -m venv /app/venv

# Activer l'environnement virtuel et installer les dépendances Python
COPY requirements.txt .
RUN . /app/venv/bin/activate && pip install --no-cache-dir -r requirements.txt

# Copier le reste du code source
COPY . .

# Définir le chemin de l’environnement virtuel dans la variable PATH
ENV PATH="/app/venv/bin:$PATH"

# Exécuter le script Python
CMD ["python", "app.py"]
