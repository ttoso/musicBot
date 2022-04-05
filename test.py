import spotipy
from spotipy.oauth2 import SpotifyClientCredentials



def getGenres(artistName):
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    genres = []

    results = sp.search(artistName, type='artist')
    generos = results['artists']['items'][0]['genres']
    for genero in generos:
        genres.append(genero)
    return genres


result = getGenres('rammstein')
for genero in result:
    print(genero)


