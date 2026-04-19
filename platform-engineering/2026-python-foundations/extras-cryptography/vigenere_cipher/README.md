Cifrado polialfabético que usa una clave para desplazar letras de manera variable. Proyecto #80 del libro "The Big Book of Small Python Projects".

## 🔧 Cómo funciona

A diferencia del Cifrado César (desplazamiento fijo), Vigenère usa una **clave**:
- Cada letra del mensaje se desplaza según la letra correspondiente de la clave
- La clave se repite cíclicamente hasta cubrir el mensaje

## 🚀 Cómo usar

```bash
python vigenere_book.py