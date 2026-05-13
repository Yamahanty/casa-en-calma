# Módulo de tareas para Casa en Calma

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


def marcar_tarea_realizada(numero_tarea):
    if 1 <= numero_tarea <= len(tareas):
        tareas[numero_tarea - 1]["estado"] = "realizada"
        print("Muy bien. Tarea marcada como realizada.")
    else:
        print("Número de tarea inválido.")
