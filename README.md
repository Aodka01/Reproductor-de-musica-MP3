🎧 Reproductor de Música por Consola (Python)

Este proyecto es un reproductor de música por consola escrito en Python, capaz de reproducir archivos .mp3 desde una ruta indicada por el usuario. Permite pausar, continuar, avanzar, retroceder, cambiar de canción, activar modo repetición y visualizar una barra de progreso en tiempo real.

--------------------------------------------------
🚀 Características

✔️ Reproducción de archivos .mp3
✔️ Control mediante teclado en tiempo real
✔️ Pausa y reanudación sin reiniciar la canción
✔️ Barra de progreso dinámica
✔️ Avance y retroceso de 10 segundos
✔️ Modo repetición ON/OFF
✔️ Lista automática desde una carpeta
✔️ Colores en consola (terminal más visual)

--------------------------------------------------
🧰 Requisitos

Debes tener instalado:

- Python 3.8+
- pygame
- keyboard
- colorama
- mutagen (opcional)

Comando de instalación:
pip install pygame keyboard colorama mutagen

--------------------------------------------------
📂 ¿Cómo usarlo?

1. Ejecuta el script:
python reproductor.py

2. Ingresa la ruta donde guardas tus canciones .mp3

Ejemplo:
C:\Users\Usuario\Music

3. Usa los controles del teclado.

--------------------------------------------------
🎮 Controles disponibles

p = Pausar
c = Continuar
a = Avanzar +10s
r = Retroceder -10s
n = Siguiente canción
b = Canción anterior
x = Activar/Desactivar repetición
ESC = Salir del reproductor

--------------------------------------------------
📌 Notas importantes

- Solo reproduce archivos .mp3
- Algunas versiones de pygame no soportan saltos exactos
- mutagen mejora duración real de la pista

--------------------------------------------------
🧠 Tecnologías utilizadas

- Pygame → Motor de audio
- Keyboard → Captura de teclas en tiempo real
- Colorama → Colores en consola
- Mutagen → Duración real del audio

--------------------------------------------------
🖥️ Compatibilidad

✅ Windows
⚠️ Linux requiere permisos especiales
⚠️ macOS puede tener restricciones con keyboard

--------------------------------------------------
📜 Créditos

Todos los derechos reservados a Aodka.

--------------------------------------------------
🐞 Problemas conocidos

- get_pos() puede devolver valores erróneos al estar pausado
- Algunas terminales no muestran bien caracteres Unicode

--------------------------------------------------
¡Disfruta tu reproductor! 🎶
