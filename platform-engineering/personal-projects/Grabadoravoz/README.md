# Mi project Voice-Recorder.

# Grabadora de Voz en Python 🎤

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)

Grabadora de audio simple que guarda archivos WAV, compatible con macOS (especialmente optimizada para MacBook Air).

## 🚀 Características
- Graba audio en formato WAV (mono, 44.1kHz por defecto).
- Configurable: duración, nombre de archivo y dispositivo de entrada.
- Detección automática de micrófonos disponibles.
- Manejo de errores para interrupciones o permisos.

## 📦 Requisitos
```bash
pip install sounddevice scipy numpy

🖥️ Compatibilidad
✅ macOS (probado en MacBook Air)
✅ Linux
⚠️ Windows (requiere configuración adicional de PortAudio)
