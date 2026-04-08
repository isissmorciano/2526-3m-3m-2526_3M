# fai un gioco super complicato con almeno 200 righe di codice senza suoni e senza grafica, solo testo. Deve essere un gioco di avventura testuale con scelte multiple e finali multipli.Ecco un gioco di avventura testuale con scelte multiple e finali multipli. Ilgioco si chiama "La Foresta Incantata".

import time
def print_slow(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.05)
    print()

def main():
    print_slow("Benvenuto a 'La Foresta Incantata'!")
    print_slow("Sei un giovane avventuriero alla ricerca di tesori nascosti.")
    print_slow("Ti trovi all'ingresso di una foresta misteriosa. Cosa fai?")
    
    scelta1 = input("1. Entra nella foresta\n2. Esplora i dintorni\n3. Torna indietro\n> ")
    
    if scelta1 == "1":
        print_slow("Entri nella foresta e ti ritrovi in un sentiero oscuro.")
        print_slow("Dopo qualche passo, incontri un vecchio saggio che ti offre due strade.")
        scelta2 = input("1. Prendi la strada a sinistra\n2. Prendi la strada a destra\n> ")
        
        if scelta2 == "1":
            print_slow("Prendi la strada a sinistra e trovi un lago incantato.")
            print_slow("Nel lago c'è una creatura magica che ti offre un dono.")
            scelta3 = input("1. Accetta il dono\n2. Rifiuta il dono\n> ")
            
            if scelta3 == "1":
                print_slow("Accetti il dono e ottieni una spada magica!")
                print_slow("Con la spada, sconfiggi un drago e trovi un tesoro nascosto!")
                print_slow("Hai vinto! Fine del gioco.")
            else:
                print_slow("Rifiuti il dono e continui a esplorare la foresta.")
                print_slow("Purtroppo, incontri un gruppo di banditi che ti derubano.")
                print_slow("Hai perso! Fine del gioco.")
        
        else:
            print_slow("Prendi la strada a destra e trovi una grotta misteriosa.")
            print_slow("Dentro la grotta, incontri un guardiano che ti sfida a risolvere un enigma.")
            scelta3 = input("1. Accetti la sfida\n2. Rifiuti la sfida\n> ")
            
            if scelta3 == "1":
                print_slow("Accetti la sfida e risolvi l'enigma con successo!")
                print_slow("Il guardiano ti concede l'accesso a una stanza segreta piena di tesori!")
                print_slow("Hai vinto! Fine del gioco.")
            else:
                print_slow("Rifiuti la sfida e decidi di tornare indietro.")
                print_slow("Mentre torni, incontri un lupo affamato che ti attacca.")
                print_slow("Hai perso! Fine del gioco.")    

    elif scelta1 == "2":
        print_slow("Esplori i dintorni e trovi un villaggio nascosto.")
        print_slow("Gli abitanti del villaggio ti offrono ospitalità e informazioni sulla foresta.")
        scelta2 = input("1. Accetta l'ospitalità\n2. Rifiuta l'ospitalità\n> ")
        
        if scelta2 == "1":
            print_slow("Accetti l'ospitalità e trascorri la notte nel villaggio.")
            print_slow("Il giorno dopo, gli abitanti ti guidano verso un tesoro nascosto nella foresta!")
            print_slow("Hai vinto! Fine del gioco.")
        else:
            print_slow("Rifiuti l'ospitalità e decidi di esplorare da solo.")
            print_slow("Purtroppo, ti perdi nella foresta e non riesci a trovare la strada per uscire.")
            print_slow("Hai perso! Fine del gioco.")

    else:
        print_slow("Decidi di tornare indietro e abbandonare l'avventura.")
        print_slow("Forse un giorno tornerai a esplorare la foresta incantata.")
        print_slow("Fine del gioco.")
        
if __name__ == "__main__":
    main()

    
