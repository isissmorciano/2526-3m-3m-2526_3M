# Parte 4: Dati da usare
# Nome playlist: "Corso Python Base"

# Video da aggiungere (nell'ordine):

# Titolo	Durata (s)	Risoluzione	Bitrate (kbps)
# Introduzione a Python	930	1080p	5000
# Variabili e Tipi	1335	720p	3000
# Funzioni e Moduli	1080	1080p	5000
# Liste e Dizionari	1560	480p	2000
# Parte 5: Utilizzo del Package
# Scrivi uno script che:

# Importa il package
# Crea una playlist con il nome specificato
# Aggiunge i 4 video con i dati della tabella sopra
# Stampa la playlist originale
# Stampa la playlist ordinata per durata
# Stampa statistiche totali (durata e dimensione)



from streaming_student import playlist_student,video_student

def main()->None:
    nome = "Corso Python Base"
    mia_playlist = playlist_student.crea_playlist(nome)
    video1 = video_student.crea_video("Introduzione a Python",930,"1080p",5000)
    video2 = video_student.crea_video("Variabili e Tipi",1335,"720p",3000)
    video3 = video_student.crea_video("Funzioni e Moduli",1080,"1080p",5000)
    video4 = video_student.crea_video("Liste e Dizionari",1560,"480p",2000)
    playlist_student.aggiungi_video(mia_playlist,video1)
    playlist_student.aggiungi_video(mia_playlist,video2)
    playlist_student.aggiungi_video(mia_playlist,video3)
    playlist_student.aggiungi_video(mia_playlist,video4)
    print(playlist_student.mostra_playlist(mia_playlist))
    print(f"Durata totale: {playlist_student.durata_totale(mia_playlist)} secondi")
    print(f"Dimensione totale: {playlist_student.dimensione_totale(mia_playlist)} MB")


if __name__ == "__main__":
    main()