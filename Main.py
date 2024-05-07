import requests # type: ignore
from flask import Flask, request, jsonify, render_template # type: ignore
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

API_KEY = "a6858788eb7fd83a4eb89064e87c52da"
BASE_URL = "https://api.themoviedb.org/3"

@app.route("/")
def home():
    return render_template('home.html')

'''
@app.route('/submit', methods=['GET', 'POST'])

def submit():

    def buscar_filme_por_id(filme_id):
        endpoint = f"{BASE_URL}/movie/{filme_id}"
        params = {"api_key": API_KEY}
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            filme = response.json()
            return filme
        else:
            print("Erro ao buscar filme:", response.status_code)
            return None

    def movieId():
        # Aqui você pega o valor do input pelo nome do campo
        if request.method == 'POST':
            firstMovie = request.form.get('firstMovie')
            return f'{firstMovie}'


    # Exemplo de uso:
    filme_id = movieId() 
    filme_info = buscar_filme_por_id(filme_id)
    if filme_info:
        filme_return = filme_info["title"]

        return render_template('home.html', filme_return=filme_return)
'''

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('q')
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}&language=pt-BR')
    results = response.json()['results']
    return jsonify([movie['title'] for movie in results[:5]])

@app.route('/meu_form/<inputId>', methods=['POST', 'GET'])
def meu_form(inputId):
    movie_id = None  # Inicialize movie_id com None

    if request.method == 'POST':
        movieName = request.form[inputId]
        urlNome = f'https://api.themoviedb.org/3/search/movie?query={movieName}&api_key={API_KEY}&language=pt-BR'

        response = requests.get(urlNome)
        data = response.json()

        if 'results' in data and data['results']:
            movie_id = data['results'][0]['id']

    if movie_id:  # Verifique se movie_id existe antes de usá-lo
        urlId = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}'

        response = requests.get(urlId)
        data = response.json()

        full_poster_url = 'Pôster não encontrado.'  # valor padrão
        poster_path = data.get('poster_path')
        if poster_path:
            # URL completa do pôster
            full_poster_url = f'https://image.tmdb.org/t/p/w500{poster_path}'

        return jsonify({'poster_url': full_poster_url})

    # Se o método não for POST ou se não houver resultados para o filme pesquisado,
    # retorne uma resposta padrão.
    return "Nenhum filme foi pesquisado ou o filme pesquisado não foi encontrado."
    


if __name__ == '__main__':
    app.run(debug=True)
