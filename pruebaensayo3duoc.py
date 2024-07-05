import json
import random
import statistics
from math import prod
import os

productos = [
    "Café Americano", "Té Chai", "Croissant", "Jugo Naranja", "Panini de Pavo y Queso",
    "Pastel de Zanahoria", "Espresso Doble", "Batido de Frutas", "Muffin", "Ensalada",
    "Chocolate Caliente", "Tarta de Frambuesa", "Sándwich de Huevo", "Galletas de Avena",
    "Frappé de Caramelo"
]


def asignar_valores_aleatorios():
    productos_con_valores = []
    for producto in productos:
        valor = random.randint(20, 100) * 100  
        iva = int(valor * 0.19)  
        productos_con_valores.append({"nombre": producto, "valor": valor, "iva": iva})
    
    with open("productos.json", "w") as file:
        json.dump(productos_con_valores, file)
    
    print("Valores aleatorios asignados y guardados en productos.json")
    

def cargar_productos():
    with open("productos.json", "r") as file:
        productos = json.load(file)
    return productos



def ver_estadisticas():
    os.system("cls")
    productos = cargar_productos()
    valores = [producto["valor"] for producto in productos]
    ivas = [producto["iva"] for producto in productos]
    
    producto_mas_alto = max(productos, key=lambda x: x["valor"])
    producto_menor_iva = min(productos, key=lambda x: x["iva"])
    promedio_valores = statistics.mean(valores)
    media_geometrica = prod(valores) ** (1/len(valores))
    
    print("\n--- Estadísticas de Productos ---")
    print(f"Producto con valor más alto: {producto_mas_alto['nombre']} - ${producto_mas_alto['valor']}")
    print(f"Producto con IVA más bajo: {producto_menor_iva['nombre']} - ${producto_menor_iva['iva']}")
    print(f"Promedio del valor de los productos: ${promedio_valores:.2f}")
    print(f"Media geométrica del valor de los productos: ${media_geometrica:.2f}")
    
    
def menu():
    os.system("cls")
    while True:
        print("=== MENÚ PRINCIPAL ===")
        print("1. Asignar montos aleatorios.")
        print("2. Ver estadísticas.")
        print("3. Salir del programa.")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '1':
            asignar_valores_aleatorios()
        elif opcion == '2':
            ver_estadisticas()
        elif opcion == '3':
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()

