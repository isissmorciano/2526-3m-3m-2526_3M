

def crea_domanda(testo: str, opzioni: list[str], risposta: int) -> dict:
    """Crea una domanda con opzioni e indice della risposta corretta.

    La risposta corretta è un indice 0-based nella lista delle opzioni.
    """
    return {"testo": testo, "opzioni": opzioni, "risposta": risposta}


def info_domanda(domanda: dict) -> str:

    linee = [domanda["testo"]]
    for i, opzione in enumerate(domanda["opzioni"], 1):
        linee.append(f"{i}. {opzione}")
    return "\n".join(linee)


def risposta_valida(domanda: dict, scelta: int) -> bool:
   
    return 1 <= scelta <= len(domanda["opzioni"])


def verifica_risposta(domanda: dict, scelta: int) -> bool:
   
    if not risposta_valida(domanda, scelta):
        return False
    return (scelta - 1) == domanda["risposta"]