import requests # type: ignore
from flask import Flask, request, render_template # type: ignore
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route('/submit', methods=['GET', 'POST'])
def submit():

    API_KEY = "a6858788eb7fd83a4eb89064e87c52da"
    BASE_URL = "https://api.themoviedb.org/3"

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
    filme_id = movieId() # ID do filme "Clube da Luta"
    filme_info = buscar_filme_por_id(filme_id)
    if filme_info:
        filme_return = filme_info["title"]

        return render_template('home.html', filme_return=filme_return)

app.run(debug=True)
