
from flask import Flask, render_template, request, redirect


class Jogo:
    def __init__(self, nome, categoria, console):
        self.nome = nome
        self.categoria = categoria
        self.console = console


jogo1 = Jogo('Tetris', 'Puzzle', 'Atari')
jogo2 = Jogo('God of War', 'Hack n Slash', 'PS2')
jogo3 = Jogo('Mortal Kombat', 'Luta', 'PS2')
jogo4 = Jogo('FIFA22', 'Esporte', 'PS5')
lista = [jogo1, jogo2, jogo3, jogo4]

# Inserindo aplicação
app = Flask(__name__)

# Cria-se uma rota para acessar a página
@app.route('/')
def index():
    return render_template('lista.html', titulo='jogos', jogos=lista)

@app.route('/novo',)
def novo():
    return render_template('novo.html', titulo='jogos')

@app.route('/criar', methods=['POST',])
def criar():
    nome = request.form['nome']
    categoria = request.form['categoria']
    console = request.form['console']
    jogo = Jogo(nome, categoria, console)
    lista.append(jogo)
    return redirect('/')

# Fazer a aplicação rodar
app.run(debug=True)