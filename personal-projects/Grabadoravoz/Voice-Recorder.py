import sounddevice as sd
from scipy.io.wavfile import write

# Configuración para grabación de audio
fs = 44100  # Frecuencia de muestreo estándar
seconds = 7  # Duración más corta para pruebas
output_file = "grabacion.wav"  # Nombre del archivo de salida

try:
    print(" Iniciando grabación mono (1 canal)...")
    
    # Ajustes clave para tu hardware:
    recording = sd.rec(
        int(seconds * fs),
        samplerate=fs,
        channels=1,  # Usamos 1 canal para mono
        device=0,    # Usamos explícitamente el micrófono interno (dispositivo 0)
        dtype='int16'
    )
    
    sd.wait()  # Espera hasta que termine
    write(output_file, fs, recording)
    print(f"Grabación guardada como '{output_file}'")
    print(f"Detalles: {seconds}s, {fs}Hz, mono")

except Exception as e:
    print(f"Error: {str(e)}")
    print("Solución: Verifica permisos de micrófono en Preferencias del Sistema > Seguridad")