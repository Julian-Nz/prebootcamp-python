# 1. Actualizar valores en diccionarios y listas

matriz = [ [10, 15, 20], [3, 7, 14] ]
cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"}
]
ciudades = {
    "México": ["Ciudad de México", "Guadalajara", "Cancún"],
    "Chile": ["Santiago", "Concepción", "Viña del Mar"]
}
coordenadas = [
    {"latitud": 8.2588997, "longitud": -84.9399704}
]

# Actualizaciones
matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = 9.9355431

# 2. Iterar a través de una lista de diccionarios
def iterarDiccionario(lista):
    for dic in lista:
        salida = ", ".join([f"{k} - {v}" for k, v in dic.items()])
        print(salida)

# 3. Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    for dic in lista:
        if llave in dic:
            print(dic[llave])

# 4. Iterar a través de un diccionario con valores de lista
def imprimirInformacion(diccionario):
    for clave, lista in diccionario.items():
        print(f"{len(lista)} {clave.upper()}")
        for item in lista:
            print(item)
