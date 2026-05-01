import subprocess
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent

MODULES = {
    "1": {
        "name": "Analisis",
        "script": PROJECT_ROOT / "analisis_punto_1" / "analisis.py",
        "output": PROJECT_ROOT / "analisis_punto_1" / "salida_analisis.txt",
    },
    "2": {
        "name": "Limpieza",
        "script": PROJECT_ROOT / "limpieza_punto_2" / "limpieza.py",
        "output": PROJECT_ROOT / "limpieza_punto_2" / "salida_limpieza.txt",
    },
    "3": {
        "name": "Transformacion",
        "script": PROJECT_ROOT / "transformacion_punto_3" / "transformacion.py",
        "output": PROJECT_ROOT / "transformacion_punto_3" / "salida_transformacion.txt",
    },
    "4": {
        "name": "Visualizacion",
        "script": PROJECT_ROOT / "visualizacion_punto_4" / "visualizacion.py",
        "output": PROJECT_ROOT / "visualizacion_punto_4" / "salida_visualizacion.txt",
    },
    "5": {
        "name": "Reto Punto 5",
        "script": PROJECT_ROOT / "reto_punto_5" / "reto_punto_5.py",
        "output": PROJECT_ROOT / "reto_punto_5" / "respuestas_reto.txt",
    },
}


def show_menu() -> None:
    print("\n" + "=" * 70)
    print("MENU PRINCIPAL - TALLER MOMENTO 2")
    print("=" * 70)
    print("1. Ejecutar modulo de Analisis")
    print("2. Ejecutar modulo de Limpieza")
    print("3. Ejecutar modulo de Transformacion")
    print("4. Ejecutar modulo de Visualizacion")
    print("5. Ejecutar modulo Reto Punto 5")
    print("6. Ejecutar todos los modulos")
    print("0. Salir")
    print("=" * 70)


def ensure_runtime_dirs() -> None:
    # Estos scripts guardan imagenes en esta ruta relativa.
    (PROJECT_ROOT / "visualizacion").mkdir(exist_ok=True)


def run_module(option: str) -> None:
    module = MODULES.get(option)
    if not module:
        print("Opcion invalida. Intenta nuevamente.")
        return

    script_path = module["script"]
    output_path = module["output"]

    if not script_path.exists():
        print(f"No se encontro el script: {script_path}")
        return

    print(f"\nEjecutando: {module['name']}")
    print("-" * 70)

    result = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT,
        capture_output=True,
        text=True,
    )

    if result.stdout:
        print(result.stdout)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(result.stdout or "", encoding="utf-8")
    print(f"Salida guardada en: {output_path}")

    if result.stderr:
        print("\nSe detectaron mensajes de error:")
        print(result.stderr)

    if result.returncode == 0:
        print(f"Modulo '{module['name']}' ejecutado correctamente.")
    else:
        print(f"Modulo '{module['name']}' termino con errores (codigo {result.returncode}).")


def run_all_modules() -> None:
    print("\nEjecutando todos los modulos...")
    for option in ["1", "2", "3", "4", "5"]:
        run_module(option)
        print("\n" + "#" * 70)


def main() -> None:
    ensure_runtime_dirs()

    while True:
        show_menu()
        choice = input("Selecciona una opcion: ").strip()

        if choice == "0":
            print("Saliendo del programa. Hasta luego.")
            break
        if choice == "6":
            run_all_modules()
            continue

        run_module(choice)


if __name__ == "__main__":
    main()
