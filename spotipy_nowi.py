import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

from services.musica import Musica

SPOTIPY_CLIENT_ID = 'e029f2a8b3df4947a5e19cec50d042f9'
SPOTIPY_CLIENT_SECRET = 'cda1c43214ad4e73914162e64aee2ba9'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))

def busca_musica(busca):

	musicas = []
	dados = spotify.search(q=busca, limit=10, type="track")
	#pprint.pprint(dados["tracks"]["items"])
	dados = dados["tracks"]["items"];

	for musica in dados:

		artistas = ""
		for artista in musica["artists"]:
			artistas += artista["name"]
			if(len(musica["artists"]) > 1):
				artistas += ", "

		musicas.append(Musica(musica["id"], musica["name"], musica["preview_url"], musica["external_urls"]["spotify"], artistas, musica["album"]["name"]))
	
	return musicas