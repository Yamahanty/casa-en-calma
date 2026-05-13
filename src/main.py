# Casa en Calma - Primera versión en consola

tareas = [
    {"nombre": "Tender la cama", "estado": "pendiente"},
    {"nombre": "Lavar los platos", "estado": "pendiente"},
    {"nombre": "Recoger juguetes", "estado": "pendiente"},
    {"nombre": "Sacar la basura", "estado": "pendiente"},
    {"nombre": "Preparar ropa para mañana", "estado": "pendiente"},
]


def mostrar_tareas():
    print("\nTareas de hoy:")
    for numero, tarea in enumerate(tareas, start=1):
        simbolo = "✓" if tarea["estado"] == "realizada" else " "
        print(f"{numero}. [{simbolo}] {tarea['nombre']}")


def marcar_tarea_realizada():
    mostrar_tareas()

    try:
        opcion = int(input("\nEscribe el número de la tarea realizada: "))

        if 1 <= opcion <= len(tareas):
            tareas[opcion - 1]["estado"] = "realizada"
            print("Muy bien. Tarea marcada como realizada.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Debes escribir un número.")


def mostrar_frase_motivadora():
    print("\nFrase del día:")
    print("No tienes que hacerlo todo perfecto. Un paso pequeño también cuenta.")


def mostrar_menu():
    print("\n==============================")
    print("      CASA EN CALMA")
    print("==============================")
    print("1. Ver tareas de hoy")
    print("2. Marcar tarea como realizada")
    print("3. Ver frase motivadora")
    print("4. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("\nElige una opción: ")

        if opcion == "1":
            mostrar_tareas()
        elif opcion == "2":
            marcar_tarea_realizada()
        elif opcion == "3":
            mostrar_frase_motivadora()
        elif opcion == "4":
            print("\nHasta luego. Recuerda: poco a poco también se avanza.")
            break
        else:
            print("Opción inválida. Intenta otra vez.")


if __name__ == "__main__":
    main()
