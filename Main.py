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

### Rota para atualização de autocomplete
@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('q')
    response = requests.get(f'https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={query}&language=pt-BR')
    results = response.json()['results']
    return jsonify([movie['title'] for movie in results[:5]])

if __name__ == '__main__':
    app.run(debug=True)
