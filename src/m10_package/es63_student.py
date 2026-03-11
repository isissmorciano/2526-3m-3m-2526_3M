

# ## Obiettivo



# - Organizzare funzioni correlate in moduli
# - Usare dizionari per rappresentare dati
# - Ordinare dati con criteri personalizzati usando `sorted()` e `key`










































#Parte 3: Modulo `playlist.py`
    # Implementa funzioni per gestire collezioni di video.

    # **Funzioni di base:**
    # - `crea_playlist()` - crea un dizionario con nome e lista vuota di video
    # - `aggiungi_video()` - aggiunge un video alla playlist
    # - `rimuovi_video()` - rimuove un video per indice
    # - `durata_totale()` - somma le durate di tutti i video
    # - `dimensione_totale()` - somma le dimensioni di tutti i video
    # - `mostra_playlist()` - formatta la playlist in una stringa leggibile

    # **Funzioni di ordinamento (con sorted):**
    # - `ordina_per_durata()` - ordina i video dal più breve al più lungo
    #   - Usa `sorted()` con `key` per specificare quale attributo usare per l'ordinamento

    # **Approfondimento: sorted() con key**
    # `sorted()` ordina una lista. Normalmente ordina numeri e stringhe per valore naturale. Ma con `key`, puoi dire esattamente come confrontare gli elementi:
    # - `key=lambda v: v["durata"]` ordina usando il valore della chiave "durata"

    # ### Parte 4: Dati da usare

    # **Nome playlist:** `"Corso Python Base"`

    # **Video da aggiungere (nell'ordine):**

    # | Titolo | Durata (s) | Risoluzione | Bitrate (kbps) |
    # |--------|-----------|-------------|---|
    # | Introduzione a Python | 930 | 1080p | 5000 |
    # | Variabili e Tipi | 1335 | 720p | 3000 |
    # | Funzioni e Moduli | 1080 | 1080p | 5000 |
    # | Liste e Dizionari | 1560 | 480p | 2000 |

    # ### Parte 5: Utilizzo del Package
    # Scrivi uno script che:

    # 1. Importa il package
    # 2. Crea una playlist con il nome specificato
    # 3. Aggiunge i 4 video con i dati della tabella sopra
    # 4. Stampa la playlist originale
    # 5. Stampa la playlist ordinata per durata
    # 6. Stampa statistiche totali (durata e dimensione)


# from streaming import video ,playlist 

from streaming.playlist import *
from streaming.video import *



def main():
    nome="Corso Python Base"

    # **Video da aggiungere (nell'ordine):**

    lista_v=[]

    # | Titolo | Durata (s) | Risoluzione | Bitrate (kbps) |
    # |--------|-----------|-------------|---|
    # | Introduzione a Python | 930 | 1080p | 5000 |
    # | Variabili e Tipi | 1335 | 720p | 3000 |
    # | Funzioni e Moduli | 1080 | 1080p | 5000 |
    # | Liste e Dizionari | 1560 | 480p | 2000 |

   
    playlist=crea_playlist(nome)

    lista_v.append(crea_video('intap',930,1080,5000))
    lista_v.append(crea_video('vet',1335,720,3000))
    lista_v.append(crea_video('fem',1080,1080,5000))
    lista_v.append(crea_video('led',1560,480,2000))

    for v in lista_v :

        aggiungi_video(playlist,v)

    print (playlist)

    for video in playlist:
         



