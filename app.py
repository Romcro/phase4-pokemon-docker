import os
import pygame

# Vérifiez si l'environnement est Dockerisé
is_docker = os.path.exists('/.dockerenv')

if not is_docker:
    pygame.mixer.init()  # Initialisation du son uniquement en dehors de Docker

def play_music():
    if not is_docker:
        try:
            pygame.mixer.music.load('son/son.mp3')
            pygame.mixer.music.play(-1)
        except pygame.error as e:
            print(f"Erreur lors de la lecture de la musique : {e}")

def stop_music():
    if not is_docker and pygame.mixer.music.get_busy():
        pygame.mixer.music.stop()

print("Lancement de l'application Pokémon...")