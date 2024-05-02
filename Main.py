import requests # type: ignore
from flask import Flask, render_template # type: ignore
app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

app.run(debug=True)


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

# Exemplo de uso:
filme_id = 550  # ID do filme "Clube da Luta"
filme_info = buscar_filme_por_id(filme_id)
if filme_info:
    print("Título:", filme_info["title"])
    print("Sinopse:", filme_info["overview"])
