import colorama
from colorama import Fore, Style
import pygame
import keyboard
import time
import os

colorama.init()

# --- Firma ---
print(Fore.LIGHTRED_EX + " ▄▄▄      ▒█████   ██████   ██  ██ ▄▄▄▄      ")
print(                   "▒████▄   ▒██▒  ██▒██    ▒█▒ ██  ██ █████▄    ")
print(                   "▒██  ▀█▄ ▒██░  ██░██     ██ ████   █▌  ▀█▄  ")
print(                   "░██▄▄▄▄██▒██   ██░██     █░ ██ ██ ░██▄▄▄▄██ ")
print(                   " ▓█    ██░ ████▓▒▒███████▒░▒██  ██ ██    ██▒")
print(                   " ▒▒   ▓▒ ░ ▒░▒░▒░▒ ▒▓▒ ▒ ░ ▒▒▓  ▒  ▒▒   ▓▒ ░")
print(                   "  ▒   ▒▒ ░ ░ ▒ ▒░░ ░▒  ░ ░ ░ ▒  ▒   ▒   ▒▒ ░")
print(                   "  ░   ▒  ░ ░ ░ ▒ ░  ░  ░   ░ ░  ░   ░   ▒   ")
print(                   "      ░  ░   ░ ░       ░     ░          ░  ░")
print(Fore.RESET)
print(f"{Fore.RED}todos los derechos reservados a mi puñeta.")
print(Fore.RESET)

# --- CONFIGURACIÓN ---
Ruta = input(Fore.LIGHTBLUE_EX + "Introduce la ruta de la carpeta donde tienes tus canciones:")
print(Fore.RESET)
music_folder = Ruta
avance = 10  # segundos de salto

pygame.init()
pygame.mixer.init()

# Volumen inicual

volume = 0.5
pygame.mixer.music.set_volume(volume)

# Cargar lista de canciones .mp3
playlist = [f for f in os.listdir(music_folder) if f.lower().endswith(".mp3")]
if not playlist:
    print(Fore.RED + "No se encontraron .mp3 en la carpeta." + Fore.RESET)
    raise SystemExit

current_index = 0
repeat_mode = False
is_paused = False



def wait_key_release(key, timeout=1.0):
    """Evita repetidos triggers mientras el usuario mantiene la tecla presionada."""
    t0 = time.time()
    while keyboard.is_pressed(key) and (time.time() - t0) < timeout:
        time.sleep(0.02)

def play_song(index, start=0.0):
    ruta = os.path.join(music_folder, playlist[index])
    try:
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play(start=start)
    except TypeError:
        # Algunas versiones de pygame no soportan start en MP3; en ese caso, reinicia desde 0
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play()
    
    print(Fore.YELLOW + f"\n▶️ Reproduciendo: {playlist[index]}" + Fore.RESET)

def next_song():
    global current_index
    current_index = (current_index + 1) % len(playlist)
    play_song(current_index)

def prev_song():
    global current_index
    current_index = (current_index - 1) % len(playlist)
    play_song(current_index)

# Función barra de progreso
def progress_bar():
    pos = pygame.mixer.music.get_pos() / 1000.0
    length = get_length()
    if length <= 0:
        # si no hay duración disponible, muestra solo el tiempo transcurrido
        return f"{int(pos)}s"
    bar_len = 30
    filled = int(min(max((pos / length), 0.0), 1.0) * bar_len)
    bar = "[" + "█" * filled + "-" * (bar_len - filled) + "]"
    return f"{bar} {int(pos)}/{int(length)}s"

# Duración real del archivo usando mutagen (opcional)
def get_length():
    try:
        from mutagen.mp3 import MP3
        ruta = os.path.join(music_folder, playlist[current_index])
        audio = MP3(ruta)
        return audio.info.length
    except Exception:
        return 0

# Iniciar primera canción
play_song(current_index)


print(Fore.LIGHTGREEN_EX,
      "Controles:\n"
      "[p] Pausar | [c] Continuar | [a] Avanzar 10s | [r] Retroceder 10s\n"
      "[n] Siguiente | [b] Anterior | [x] Repetición On/Off | [+] Subir Volumen | [-] Bajar Volume | [ESC] Salir"
      + Fore.RESET)

while True:

    # PAUSA
    if keyboard.is_pressed('p'):
        if not is_paused:
            pygame.mixer.music.pause()
            is_paused = True
            print(Fore.LIGHTBLUE_EX + "⏸ Pausado" + Fore.RESET)
        wait_key_release('p')

    # CONTINUAR
    elif keyboard.is_pressed('c'):
        if is_paused:
            pygame.mixer.music.unpause()
            is_paused = False
            print("▶️ Continuando")
        wait_key_release('c')

    # AVANZAR 10s
    elif keyboard.is_pressed('a'):
        pos = pygame.mixer.music.get_pos() / 1000.0
        # Si está pausado no usamos get_pos() que puede ser -1 o inválido; simplemente unpause luego play desde pos:
        if is_paused:
            pygame.mixer.music.unpause()
            is_paused = False
        try:
            pygame.mixer.music.play(start=max(0, pos + avance))
        except TypeError:
            # fallback: reiniciar (si la versión no soporta start)
            pygame.mixer.music.play()
        print(f"⏩ {int(pos + avance)}s")
        wait_key_release('a')

    # RETROCEDER 10s
    elif keyboard.is_pressed('r'):
        pos = pygame.mixer.music.get_pos() / 1000.0
        if is_paused:
            pygame.mixer.music.unpause()
            is_paused = False
        nueva_pos = max(0, pos - avance)
        try:
            pygame.mixer.music.play(start=nueva_pos)
        except TypeError:
            pygame.mixer.music.play()
        print(f"⏪ {int(nueva_pos)}s")
        wait_key_release('r')

    # SIGUIENTE
    elif keyboard.is_pressed('n'):
        print("⏭ Siguiente")
        next_song()
        is_paused = False
        wait_key_release('n')

    # ANTERIOR
    elif keyboard.is_pressed('b'):
        print("⏮ Anterior")
        prev_song()
        is_paused = False
        wait_key_release('b')

    # REPETICIÓN ON/OFF
    elif keyboard.is_pressed('x'):
        repeat_mode = not repeat_mode
        print(Fore.CYAN + f"🔁 Repetición: {'ON' if repeat_mode else 'OFF'}" + Fore.RESET)
        wait_key_release('x')

    # SALIR
    elif keyboard.is_pressed('esc'):
        print(Fore.RED + "👋 Cerrando reproductor..." + Fore.RESET)
        break

    # Subir volumen 
    elif keyboard.is_pressed('+'):
        volume = min(1.0, volume + 0.05)
        pygame.mixer.music.set_volume(volume)
        print(Fore.GREEN + F"🔊 Volumen: {int(volume*100)}%" + Fore.RESET)
        wait_key_release('+')

    #  Bajar Volumen 

    elif keyboard.is_pressed('-'):
        volume = max(0.0, volume - 0.05)
        pygame.mixer.music.set_volume(volume)
        print(Fore.GREEN + f"🔊 Volumen: {int(volume*100)}%" + Fore.RESET)
        wait_key_release('-')

    # Si la canción NO está ocupada (no reproduciendo) y NO estamos en pausa -> pasó a final
    if not pygame.mixer.music.get_busy() and not is_paused:
        # Pequeña espera extra para evitar false positives momentáneos
        time.sleep(0.05)
        if not pygame.mixer.music.get_busy() and not is_paused:
            if repeat_mode:
                play_song(current_index)
            else:
                next_song()

    # Mostrar barra de progreso (sin spam)
    print(Fore.LIGHTRED_EX,  "\r" + progress_bar(), end="")

    
    

    time.sleep(0.18)
