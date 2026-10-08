"""Генератор случайных предложений на испанском языке."""

import itertools
import random


SUJETOS = (
    "El músico",
    "La profesora",
    "Un viajero",
    "Mi vecina",
    "El gato",
    "La niña",
    "Un científico",
    "La escritora",
)

ACCIONES = (
    "observa",
    "descubre",
    "recuerda",
    "visita",
    "fotografía",
    "explora",
    "admira",
    "busca",
)

COMPLEMENTOS = (
    "un jardín lleno de flores",
    "las montañas cubiertas de nieve",
    "una calle tranquila",
    "el antiguo mercado del pueblo",
    "un libro muy interesante",
    "las estrellas desde la ventana",
    "una playa de arena dorada",
    "el castillo junto al río",
)

CIRCUNSTANCIAS = (
    "cada mañana",
    "durante sus vacaciones",
    "cuando termina la lluvia",
    "antes de la cena",
    "con mucha curiosidad",
    "en una tarde de verano",
    "mientras escucha música",
    "al caer la noche",
)


def generar_frases(cantidad: int = 10) -> list[str]:
    """Возвращает заданное количество неповторяющихся испанских предложений."""
    combinaciones = itertools.product(
        SUJETOS, ACCIONES, COMPLEMENTOS, CIRCUNSTANCIAS
    )
    frases = [
        f"{sujeto} {accion} {complemento} {circunstancia}."
        for sujeto, accion, complemento, circunstancia in combinaciones
    ]

    if not 0 <= cantidad <= len(frases):
        raise ValueError(f"Количество должно быть от 0 до {len(frases)}")

    return random.sample(frases, cantidad)


if __name__ == "__main__":
    for numero, frase in enumerate(generar_frases(), start=1):
        print(f"{numero}. {frase}")
