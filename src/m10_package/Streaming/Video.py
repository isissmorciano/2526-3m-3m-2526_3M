""" Modulo video per gestire video singoli in uno streaming package"""

def crea_video(titolo: str, durata: int, risoluzione: str, bitrate: int) -> dict:

    """"Crea un video
    
    Args:
        Titolo: Titolo del Video
        Durata: Durata in Secondi
        Risoluzione: Risoluzione (es. "1080p", "720p", "480p", "360p")
        Bitrate: Bitrate in Kbps"""