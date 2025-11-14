from flask import Flask, request, jsonify

DB_USUARIOS = []
global NEXT_USER_ID
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

TIPOS_USUARIO_VALIDOS = ["Turista","Parceiro", "Administrador"]

app = Flask(__name__)

@app.route('/entrar', methods=['POST'])
def entrar():
    return jsonify({"mensagem": "Rota de Login: Implementação pendente no tópico 3."})

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    global NEXT_USER_ID
    dados = request.get_json()
    if not dados:
        return jsonify({"erro": "Dados ou formato incorreto (JSON)."}), 400

    campos_obrigatorios = ['nome', 'idade', 'telefone', 'email', 'senha', 'tipo_usuario']

    for campo in campos_obrigatorios:
        if campo not in dados:
            return jsonify({"erro": f"Campo obrigatório ausente: {campo}."}), 400
        
    if not isinstance(dados['idade'], int) or dados['idade'] <= 0:
        return jsonify({"erro": "Idade deve ser um número inteiro positivo."}), 400
    
    for usuario in DB_USUARIOS:
        if usuario['email'] == dados['email']:
            return jsonify({"erro": "E-mail já cadastrado. E-mail deve ser único (login)."}), 400
                            
    tipo_usuario = dados['tipo_usuario']
    if tipo_usuario not in TIPOS_USUARIO_VALIDOS:
        return jsonify({"erro": f"Tipo de usuário inválido. Escolha entre: {', '.join(TIPOS_USUARIO_VALIDOS)} "})
    
    novo_usuario = {
        'id': NEXT_USER_ID,
        'nome': dados['nome'],
        'idade': dados['idade'],
        'telefone': dados['telefone'],
        'email': dados ['email'],
        'senha': dados ['senha'],
        'tipo_usuario': tipo_usuario
    }

    DB_USUARIOS.append(novo_usuario)
    
    NEXT_USER_ID += 1

    usuario_resposta = novo_usuario.copy()
    del usuario_resposta['senha']
    return jsonify({
        "mensagem": "Usuário cadastrado com sucesso!", "usuario": usuario_resposta
    }), 201

@app.route('/', methods=['GET'])
def publicacao_home():
    return jsonify(DB_PUBLICACAO[0])

if __name__=='__main__':
    app.run(debug=True)