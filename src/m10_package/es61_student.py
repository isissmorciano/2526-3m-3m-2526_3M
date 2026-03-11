
from musica_student import playlist_student, canzoni_student
def main()->None:
    nome = input("Insersci il nome della tua nuova playlist: ")
    mia_playlist = playlist_student.crea_playlist(nome)
    for _ in range(3):
        titolo = input("Inserisci il titolo di una canzone: ")
        artista = input("Inserisci l'artista della canzone: ")
        durata = int(input("Quanto dura questa canzone: "))
        mia_canzone = canzoni_student.crea_canzone(titolo,artista,durata)
        mia_playlist["canzoni"].append(mia_canzone)
    for canzone in mia_playlist["canzoni"]:
        print(f"{canzoni_student.info_canzone(canzone)}")
    while True:
        print("Scegli cosa vuoi fare:")
        print("1 - Aggiungi una canzone alla playlist.")
        print("2 - Rimuovi una canzone dalla playlist.")
        print("3 - Visualizza la durata totale della playlist.")
        print("4 - Visualizza la playlist: ")
        print("5 - Esci")
        scelta = int(input("Inserisci una scelta 1-5: "))
        if scelta == 1:
            titolo = input("Inserisci il titolo di una canzone da aggiungere alla playlist: ")
            artista = input("Inserisci l'artista della canzone da aggiungere alla playlist: ")
            durata = int(input("Inserisci la durata della canzone da aggiungere alla playlist: "))
            canzone_da_aggiungere = canzoni_student.crea_canzone(titolo,artista,durata)
            playlist_student.aggiungi_canzone(mia_playlist,canzone_da_aggiungere)
        elif scelta == 2:
            titolo = input("Inserisci il titolo di una canzone da rimuovere dalla playlist: ")
            artista = input("Inserisci l'artista della canzone da rimuovere dalla playlist: ")
            durata = int(input("Inserisci la durata della canzone da rimuovere dalla playlist: "))
            canzone_da_rimuovere = canzoni_student.crea_canzone(titolo,artista,durata)
            playlist_student.rimuovi_canzone(mia_playlist,canzone_da_rimuovere)
        elif scelta == 3:
            durata_tot = playlist_student.durata_totale(mia_playlist)
            print(f"La playlist {mia_playlist['nome']} dura {durata_tot}")
        elif scelta == 4:
            print(f"{mia_playlist['nome']} : {playlist_student.mostra_playlist(mia_playlist)}")
        elif scelta == 5:
            print("Sei uscito con successo!")
            break
if __name__ == "__main__":
    main()
