import sys

def procesar(dato):
    return dato.replace(" ", "")


for linea in sys.stdin:
    linea = linea.strip()
    if not linea:
        continue
    resultado = procesar(linea)
    print(resultado)
