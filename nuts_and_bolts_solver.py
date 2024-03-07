"""
Este script ha sido desarrollado como parte de una entrega para la asignatura de Diseño de Algoritmos,
especialidad en Computación, en la Facultad de Informática de Donostia-San Sebastián (UPV/EHU).
El objetivo de este script es complementar la práctica mediante la resolución del problema de las tuercas y
los tornillos (Nuts and Bolts Problem), con una variante del algoritmo Quick Sort.

La base del algoritmo implementado en este script se ha tomado y adaptado de una solución propuesta
en GeeksforGeeks, disponible en: https://www.geeksforgeeks.org/nuts-bolts-problem-lock-key-problem-using-quick-sort/.
Se ha extendido la funcionalidad original para incluir medición de tiempos de ejecución y
un método de fuerza bruta.
"""

import random
import time
from typing import List


# Función para imprimir el array
def printArray(arr: List[int]) -> None:
    for i in range(len(arr)):
        print(f" {arr[i]}", end=" ")
    print()


# Similar al método de partición estándar.
def partition(arr: List[int], low: int, high: int, pivot: int) -> int:
    i = low
    j = low
    while j < high:
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
        elif arr[j] == pivot:
            arr[j], arr[high] = arr[high], arr[j]
            j -= 1
        j += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i


# Basada en quicksort
def matchPairs(nuts: List[int], bolts: List[int], low: int, high: int) -> None:
    if low < high:
        pivot = partition(nuts, low, high, bolts[high])
        partition(bolts, low, high, nuts[pivot])  # Esta es la clave, particionar nuts en base a este pivote
        matchPairs(nuts, bolts, low, pivot - 1)
        matchPairs(nuts, bolts, pivot + 1, high)


# Brute force, para compara tiempos
def matchPairsBruteForce(nuts: List[int], bolts: List[int]) -> None:
    for i in range(len(nuts)):
        for j in range(len(bolts)):
            if nuts[i] == bolts[j]:
                bolts[i], bolts[j] = bolts[j], bolts[i]
                break


# Función para generar listas de números aleatorios
def generateRandomLists(size: int) -> (List[int], List[int]):
    nuts = random.sample(range(1, size + 1), size)
    bolts = nuts.copy()
    random.shuffle(bolts)
    return nuts, bolts


if __name__ == "__main__":
    size = 12000
    nuts, bolts = generateRandomLists(size)

    # D&D
    start_time = time.time()
    matchPairs(nuts, bolts, 0, size - 1)
    dnd_time = time.time() - start_time
    print("[D&D] Tuercas y tornillos emparejados son: ")
    printArray(nuts)
    printArray(bolts)
    print(f"Tiempo D&D: {dnd_time:.6f} segundos")

    # Fuerza Bruta
    nuts, bolts = generateRandomLists(size)
    start_time = time.time()
    matchPairsBruteForce(nuts, bolts)
    brute_force_time = time.time() - start_time
    print("[BRUTE FORCE] Tuercas y tornillos emparejados son: ")
    printArray(nuts)
    printArray(bolts)
    print(f"Tiempo Brute force: {brute_force_time:.6f} segundos")
