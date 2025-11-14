from flask import Flask, request, jsonify

DB_USUARIOS = []
NEXT_USER_ID = 1

DB_PUBLICACAO = []
publicacao_inicial = {
    'id' : 1,
    'lugar' : 'Bem vindo ao Turismo MVP',
    'titulo' : 'Sua Plataforma de Aventura!',
    'descricao' : 'Explore os melhores passeios e cadastre-se hoje.',
    'imagem' : 'link_para_imagem_padrao.jpg'
}
DB_PUBLICACAO.append(publicacao_inicial)

app = Flask(__name__)

@app.route('/entrar', methods=['POST'])
def entrar():
    return jsonify({"mensagem": "Rota de Login: Implementação pendente no tópico 3."})

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    return jsonify({"mensagem": "Rota de Cadastro: Implementação pendente no Tópico 2."})

@app.route('/', methods=['GET'])
def publicacao_home():
    return jsonify(DB_PUBLICACAO[0])

if __name__=='__main__':

    app.run(debug=True)
