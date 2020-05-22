from flask import Flask, render_template, redirect, request
import spotipy_nowi
import services

app = Flask(__name__)

@app.route("/")
def index():
	musicas = spotipy_nowi.busca_musica("Liberdad")
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

if __name__ == "__main__":
	app.run(debug=True, port=5000)
