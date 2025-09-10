import Emoji

cantidadFrase=int(input("Cuantas frases dese desea ingresar: "))
for i in range(cantidadFrase):
    frase= input("Ingrese la frase: ")
    Emoji.encontrarPalabra(frase)
    Emoji.agregarFrase(frase)