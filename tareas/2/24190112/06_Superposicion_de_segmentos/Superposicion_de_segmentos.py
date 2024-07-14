import re

def Leer(archivo_entrada):
    with open(archivo_entrada, encoding="utf-8") as entrada:
        texto = entrada.read()
    return texto

def Extraer(texto):
    numeros = re.findall(r'-?\d+', texto)
    numeros = [int(num) for num in numeros]
    return numeros

def Escribir(archivo_salida, x1, y1, x2, y2):
    with open(archivo_salida, "w", encoding="utf-8") as salida:
        if not superponen_segmentos(x1, y1, x2, y2):
            salida.write("No, los segmentos no se superponen.")
        else:
            salida.write("Sí, los segmentos se superponen.")

def superponen_segmentos(x1, y1, x2, y2):
    return not (y1 < x2 or x1 > y2)

def main():
    archivo_entrada = "entrada_ejercicio6.txt"
    archivo_salida = "salida_ejercicio6.txt"
    
    texto = Leer(archivo_entrada)
    num = Extraer(texto)
    
    x1, y1, x2, y2 = num
    Escribir(archivo_salida, x1, y1, x2, y2)

if __name__ == "__main__":
    main()
