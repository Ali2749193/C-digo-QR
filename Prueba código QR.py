import numpy as np 
from PIL import Image

# Función para convertir texto a binario
def texto_a_binario(texto):
    # Convierte un texto en una cadena binaria (ASCII)
    return ''.join(f'{ord(c):08b}' for c in texto)

# Función para crear una matriz cuadrada vacía
def crear_matriz(tamaño):
    # Crea una matriz llena de ceros
    return np.zeros((tamaño, tamaño), dtype=int)

# Función para añadir patrones de posición en las esquinas
def añadir_patrones_de_posicion(matriz):
    def añadir_patron(x, y):
        # Agrega un patrón de posición (cuadrado grande con un núcleo en el centro)
        for i in range(-1, 7):
            for j in range(-1, 7):
                if 0 <= x + i < len(matriz) and 0 <= y + j < len(matriz):
                    # Bordes externos del patrón y núcleo central
                    if (0 <= i <= 6 and (j in [0, 6] or i in [0, 6])) or (2 <= i <= 4 and 2 <= j <= 4):
                        matriz[x + i, y + j] = 1

    # Añadir los patrones en las esquinas (superior izquierda, superior derecha, inferior izquierda)
    añadir_patron(0,0)
    añadir_patron(0, len(matriz) - 8)
    añadir_patron(len(matriz) - 7, 0)
 
# Función para añadir los datos binarios a la matriz
def añadir_datos(matriz, datos):
    filas, columnas = matriz.shape
    indice_datos = 0

    # Rellenar las celdas libres con los datos binarios
    for columna in range(columnas  -1, -1, -1):  # Recorremos de derecha a izquierda
        for fila in range(filas):
            if matriz[fila, columna] == 0 and indice_datos < len(datos):
                matriz[fila, columna] = int(datos[indice_datos])
                indice_datos += 1
    return matriz

# Función para guardar la matriz como imagen
def guardar_matriz_como_imagen(matriz, nombre_archivo):
    # Convertir la matriz en una imagen (blanco y negro)
    imagen = Image.fromarray((matriz * 255).astype(np.uint8), mode='L')
    # Redimensionar la imagen para que sea más visible
    imagen = imagen.resize((matriz.shape[0] * 10, matriz.shape[1] * 10), resample=Image.NEAREST)
    imagen.save(nombre_archivo)

# Datos de entrada
datos = "Hola"  # Texto que queremos codificar
datos_binarios = texto_a_binario(datos)

# Crear el código QR básico
tamaño = 25  # Tamaño para la versión 2 QR
matriz = crear_matriz(tamaño)
añadir_patrones_de_posicion(matriz)
matriz = añadir_datos(matriz, datos_binarios)

# Guardar el código QR como imagen
guardar_matriz_como_imagen(matriz, "codigo_qr.png")
print("Código QR generado como 'codigo_qr.png'")
