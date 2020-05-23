import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pprint

from services.musica import Musica
from services.artista import Artista
from services.album import Album

SPOTIPY_CLIENT_ID = 'e029f2a8b3df4947a5e19cec50d042f9'
SPOTIPY_CLIENT_SECRET = 'cda1c43214ad4e73914162e64aee2ba9'

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET))

def busca_musica(busca):

	musicas = []
	dados = spotify.search(q=busca, limit=10, type="track")
	#pprint.pprint(dados["tracks"]["items"])
	dados = dados["tracks"]["items"];

	for musica in dados:

		artistas = []
		for artista in musica["artists"]:
			artistas.append(artista["name"])
		artistas = ", ".join(artistas)

		musicas.append(Musica(musica["id"], musica["name"], musica["preview_url"], musica["external_urls"]["spotify"], artistas, musica["album"]["name"]))
	
	return musicas



def busca_artista(busca):

	artistas = []
	dados = spotify.search(q=busca, limit=10, type="artist")
	#pprint.pprint(dados["artists"]["items"])
	dados = dados["artists"]["items"];


	for artista in dados:

		generos = ""
		if(len(artista["genres"]) > 1):
			generos = ", ".join(artista["genres"])

		imagem = "../static/img/sem-imagem.png"
		if len(artista["images"]) > 0:
			imagem = artista["images"][0]["url"]

		artistas.append(Artista(artista["id"], artista["name"], generos, artista["external_urls"]["spotify"], imagem))
	
	return artistas




def busca_album(busca):

	albuns = []
	dados = spotify.search(q=busca, limit=10, type="album")
	#pprint.pprint(dados["albums"]["items"])
	dados = dados["albums"]["items"];

	for album in dados:

		artistas = []
		for artista in album["artists"]:
			artistas.append(artista["name"])
		artistas = ", ".join(artistas)

		imagem = "../static/img/sem-imagem.png"
		if len(album["images"]) > 0:
			imagem = album["images"][0]["url"]

		albuns.append(Album(album["id"], album["name"], artistas, album["total_tracks"], album["external_urls"]["spotify"], imagem))

	return albuns