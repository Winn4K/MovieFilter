import requests # type: ignore
from flask import Flask, request, jsonify, render_template # type: ignore
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

### Adicionando a chave da api e a url a duas variaveis, 
### para ficar mais facil a reutilização no restante .py
API_KEY = "a6858788eb7fd83a4eb89064e87c52da"
BASE_URL = "https://api.themoviedb.org/3"

### Rota para a página principal
@app.route("/")
def home():
    return render_template('home.html')

### Rota para envio de formulario
"""@app.route('/submit', methods=['GET', 'POST'])

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

        return render_template('home.html', filme_return=filme_return)"""


### Rota para atualização de autocomplete
@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('q')
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}&language=pt-BR')
    results = response.json()['results']
    return jsonify([movie['title'] for movie in results[:5]])

if __name__ == '__main__':
    app.run(debug=True)
