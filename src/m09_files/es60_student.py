import json

# Funzioni - Validazione

# ```python
# def valida_voto(voto_str) -> tuple[bool, float | str]
#     """Validate vote. Returns (is_valid, value_or_error)."""
# ```

def valida_voto(voto_str) -> tuple[bool, float | str]:
    try:
        voto = float(voto_str)
        if 0 <= voto <= 10:
            return True, voto
        else:
            return False, "Voto deve essere tra 0 e 10."
    except ValueError:
        return False, "Voto deve essere un numero."


def main():
    studenti = [
     {"nome": "Alice", "voto": 8.5},
     {"nome": "Bob", "voto": 7.0},
     {"nome": "Carlo", "voto": 9.0}
     ]
    



if __name__ == "__main__":
    main()