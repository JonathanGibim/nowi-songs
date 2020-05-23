from flask import Flask, render_template, redirect, request
import spotipy_nowi
import services

app = Flask(__name__)



@app.route("/")
def index():
	musicas = spotipy_nowi.busca_musica("Gusttavo Lima")
	return render_template('index.html', **locals())




@app.route('/musicas/', methods=['GET', 'POST'])
def musicas():

	if request.method == 'GET':
		busca = ""
		musicas = spotipy_nowi.busca_musica("Liberdade Provisória")

	if request.method == 'POST':
		dados_form = request.form.to_dict()
		busca = dados_form['musica']
		musicas = spotipy_nowi.busca_musica(busca)

	
	return render_template('musicas.html', **locals())




@app.route('/artistas/', methods=['GET', 'POST'])
def artistas():

	if request.method == 'GET':
		busca = ""
		artistas = spotipy_nowi.busca_artista("João")

	if request.method == 'POST':
		dados_form = request.form.to_dict()
		busca = dados_form['artista']
		artistas = spotipy_nowi.busca_artista(busca)

	
	return render_template('artistas.html', **locals())




@app.route('/albuns/', methods=['GET', 'POST'])
def albuns():

	if request.method == 'GET':
		busca = ""
		albuns = spotipy_nowi.busca_album("Elvis")
		
	if request.method == 'POST':
		dados_form = request.form.to_dict()
		busca = dados_form['album']
		albuns = spotipy_nowi.busca_album(busca)

	
	return render_template('albuns.html', **locals())


if __name__ == "__main__":
	app.run(debug=True, port=5000)
