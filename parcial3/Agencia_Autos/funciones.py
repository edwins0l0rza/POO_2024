import os
import sys

def borrarPantalla():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def esperarTecla():
    """Espera a que el usuario presione una tecla."""
    input("\n\nPresiona Enter para continuar...")
