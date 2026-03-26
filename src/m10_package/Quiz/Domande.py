def crea_domanda(testo: str, opzioni: list[str], risposta: int) -> dict:
    return {
        "Testo": testo,
        "Opzioni": opzioni,
        "Risposta": risposta
    }

def info_domanda(domanda:dict) -> str:
    linee = [domanda["Testo"]]
    for i, opzione in enumerate(domanda["Opzioni"], 1):
        linee.append(f"{i}. {opzione}")
    return "\n".join(linee)

def risposta_valida(domanda: dict, scelta: int) -> bool:
    return 1 <= scelta <= len(domanda["opzioni"])

def verifica_risposta(domanda: dict, scelta: int) -> bool:
    if not risposta_valida(domanda, scelta):
        return False
    return (scelta - 1) == domanda["risposta"]
