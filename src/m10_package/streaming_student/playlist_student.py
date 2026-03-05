# Parte 3: Modulo playlist.py
# Implementa funzioni per gestire collezioni di video.

# Funzioni di base:

# crea_playlist() - crea un dizionario con nome e lista vuota di video
# aggiungi_video() - aggiunge un video alla playlist
# rimuovi_video() - rimuove un video per indice
# durata_totale() - somma le durate di tutti i video
# dimensione_totale() - somma le dimensioni di tutti i video
# mostra_playlist() - formatta la playlist in una stringa leggibile
# Funzioni di ordinamento (con sorted):

# ordina_per_durata() - ordina i video dal più breve al più lungo
# Usa sorted() con key per specificare quale attributo usare per l'ordinamento
# Approfondimento: sorted() con key sorted() ordina una lista. Normalmente ordina numeri e stringhe per valore naturale. Ma con key, puoi dire esattamente come confrontare gli elementi:

# key=lambda v: v["durata"] ordina usando il valore della chiave "durata"

from streaming_student.video_student import dimensione_video

def crea_playlist(nome:str)->dict:
    return {"nome":nome, "video": []}


def aggiungi_video(playlist:dict, video:dict)->None:
    playlist["video"].append(video)


def rimuovi_video(playlist:dict, video_da_rimuovere:dict)->None:
    for video in playlist["video"]:
        if video == video_da_rimuovere:
            playlist["video"].remove(video)
            print("Video rimosso con successo!")
        else:
            print("Nella playlist non è presente un video con questo nome.")


def durata_totale(playlist:dict)->float:
    durata_tot = 0
    for video in playlist:
        durata = video["durata"]
        durata_tot = durata_tot + durata
    return durata_tot


def dimensione_totale(playlist:dict) -> float: 
    dimensione_tot = 0 
    for video in playlist:
        dimensione = dimensione_video(video)
        dimensione_tot = dimensione_tot + dimensione
    return dimensione_tot


def mostra_playlist(playlist:dict)-> float:
    return (f"La playlist {playlist['nome']} contiene i seguenti video: {playlist['video']}  ")


# ordina_per_durata() - ordina i video dal più breve al più lungo
# Usa sorted() con key per specificare quale attributo usare per l'ordinamento
# Approfondimento: sorted() con key sorted() ordina una lista. Normalmente ordina numeri e stringhe per valore naturale. Ma con key, puoi dire esattamente come confrontare gli elementi:




        
    
        