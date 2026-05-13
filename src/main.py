# Casa en Calma - Versión organizada en módulos

from tareas import mostrar_tareas, marcar_tarea_realizada
from motivacion import mostrar_frase_motivadora


def main():
    print("==============================")
    print("      CASA EN CALMA")
    print("==============================")

    mostrar_tareas()

    print("\nMarcando una tarea de ejemplo como realizada...")
    marcar_tarea_realizada(1)

    mostrar_tareas()
    mostrar_frase_motivadora()

    print("\nPrueba finalizada correctamente.")


if __name__ == "__main__":
    main()ain__":
    main()
