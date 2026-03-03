# Parte 3: Implementazione di coordinate/linee.py
# Funzioni per gestire le linee (definite da due punti):

# crea_linea(p1: dict, p2: dict) -> dict:
# Restituisce un dizionario con chiavi: p1, p2
# lunghezza_linea(linea: dict) -> float:
# Calcola la lunghezza using distanza_tra_punti
# Importa from .punti import distanza_tra_punti
# punto_medio(linea: dict) -> dict:
# Restituisce il punto medio tra p1 e p2
# Coordinate: ((x1+x2)/2, (y1+y2)/2)
# info_linea(linea: dict) -> str:
# Restituisce formato: "Linea da (x1, y1) a (x2, y2)"

from punti_student import distanza_tra_punti
def crea_linea(p1: dict, p2: dict) -> dict:
    return{"P1" : p1,
           "P2": p2}


def lunghezza_linea(linea: dict) -> float:
    return distanza_tra_punti(linea)


def punto_medio(linea: dict) -> dict:
    x1 = linea["P1"]["X"]
    x2 = linea["P2"]["X"]
    y1 = linea["P1"]["Y"]
    y2 = linea["P2"]["Y"]
    
    
    

