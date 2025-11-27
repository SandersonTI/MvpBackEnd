from flask import Flask, request, jsonify

DB_USUARIOS = []
global NEXT_USER_ID
NEXT_USER_ID = 1

DB_PASSEIOS = []
NEXT_PASSEIOS_ID = 1

DB_COMPRAS = []
NEXT_COMPRAS_ID = 1

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

def checar_admin(email):
    for usuario in DB_USUARIOS:
        if usuario['email'] == email and usuario['tipo_usuario'].lower() == "administrador":
            return True
    return False    

def checar_parceiro(email):
    for usuario in DB_USUARIOS:
        if usuario['email'] == email and usuario['tipo_usuario'].lower() == "parceiro":
            return True
    return False    

def checar_turista(email):
    for usuario in DB_USUARIOS:
        if usuario['email'] == email and usuario['tipo_usuario'].lower() == "turista":
            return usuario
    return None

app = Flask(__name__)

@app.route('/entrar', methods=['POST'])
def entrar():

    dados = request.get_json()

    if not dados or 'email' not in dados or 'senha' not in dados:
        return jsonify({"erro": "E-mail e senha são obrigatórios."}), 400

    email = dados['email']
    senha_digitada = dados['senha']
    
    usuario_encontrado = None

    for usuario in DB_USUARIOS:
        if usuario['email'] == email:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        return jsonify({"erro": "E-mail ou senha inválidos."}), 401

    if usuario_encontrado['senha'] != senha_digitada:
        return jsonify({"erro": "E-mail ou senha inválidos."}), 401

    usuario_resposta = usuario_encontrado.copy()

    del usuario_resposta ['senha']
    return jsonify({
    "mensagem": "Login realizado com sucesso!",
    "user_id": usuario_resposta['id'],
    "nome": usuario_resposta['nome'],
    "email": usuario_resposta['email'],
    "tipo_usuario": usuario_resposta['tipo_usuario']
}), 200

    
@app.route('/publicacao/editar', methods=['POST'])
def editar_publicacao():

    dados = request.get_json()

    if not dados or 'admin_email' not in dados:
        return jsonify({"erro": "Email do Administrador e dados são obrigatórios."}), 400
    
    admin_email = dados.get('admin_email')

    if not checar_admin(admin_email):
        return jsonify({"erro": "Acesso negado, Apenas Administradores podem editar a Publicação."}), 403

    campos_permitidos = ['lugar', 'titulo', 'descricao', 'imagem']

    dados_para_atualizar = {k: v for k, v in dados.items() if k in campos_permitidos}

    if not dados_para_atualizar:
        return jsonify({"erro": "Nenhum campo válido para atualização da Publicação foi fornecido."}), 400
    
    publicacao_atual = DB_PUBLICACAO[0]

    for chave, valor in dados_para_atualizar.items():
        publicacao_atual[chave] = valor

    return jsonify({
        "mensagem": "Publicação atualizada com sucesso por " + publicacao_atual['titulo'],
        "publicacao": publicacao_atual
    }), 200

@app.route('/publicacao/excluir', methods=['POST'])
def excluir_publicacao():

    dados = request.get_json()

    if not dados or 'admin_email' not in dados:
        return jsonify({"erro": "Email do administrador é obrigatório."}), 400
    
    admin_email = dados.get('admin_email')

    if not checar_admin(admin_email):
        return jsonify({"erro": "Acesso negado. Apenas Administradores podem excluir a Publicação."}), 403
    
    DB_PUBLICACAO.clear()

    publicacao_resetada = {
        'id': 1,
        'lugar': 'Bem-vindo ao Turismo MVP',
        'titulo': 'Padrão Restaurado',
        'descricao': 'Conteúdo padrão de Publicação foi restaurado.',
        'imagem': 'link_para_imagem_padrao.jpg'
    }

    DB_PUBLICACAO.append(publicacao_resetada)

    return jsonify({"mensagem": "Publicação excluida e restaurada para o padrão (simulação de exclusão)."}),200

@app.route('/passeio/cadastrar', methods=['POST'])
def cadastrar_passeio():

    global NEXT_PASSEIOS_ID

    dados = request.get_json()

    if not dados or 'parceiro_email' not in dados:
        return jsonify({"erro": " Email do Parceiro e dados do passeio são obrigatórios."}), 400
    
    parceiro_email = dados.get('parceiro_email')

    if not checar_parceiro(parceiro_email):
        return jsonify({"erro": "Acesso negado. Apenas Parceiros podem cadastrar passeios. "}), 403
    
    campos_obrigatorios = ['titulo', 'descricao', 'valor', 'imagem_url']

    for campo in  campos_obrigatorios:
        if campo not in dados or not dados[campo]:
            return jsonify({"erro": f"campo obrigatório do passeio ausente: {campo}."}), 400
        
    novo_passeio = {
        'id': NEXT_PASSEIOS_ID,
        'parceiro_email': parceiro_email,
        'titulo': dados['titulo'],
        'descricao': dados['descricao'],
        'valor': dados['valor'],
        'imagem_url': dados['imagem_url']
    }

    DB_PASSEIOS.append(novo_passeio)
    NEXT_PASSEIOS_ID += 1

    return jsonify({
        "mensagem": "Passeio cadastrado com sucesso!",
        "passeio": novo_passeio
    }), 201

@app.route('/passeio/comprar', methods=['POST'])
def comprar_passeio():
    
    global NEXT_COMPRA_ID

    dados = request.get_json()

    if not dados or 'turista_email' not in dados or 'passeio_id' not in dados:
        return jsonify({"erro": "Email do turista e ID do Passeio são obrigatórios"}), 400
            
    turista_email = dados.get('turista_email')
    passeio_id = dados.get('passeio_id')

    turista = checar_turista(turista_email)
    
    if not turista:
        return jsonify({"erro": "Acesso negado. Apenas Turistas podem realizar compras."}), 403
    
    passeio_encontrado = None

    for passeio in DB_PASSEIOS:
        if passeio['id'] == passeio_id:
            passeio_encontrado = passeio
            break

    if not passeio_encontrado:
        return jsonify({"erro": f"Passeio com ID {passeio_id} não encontrado."}), 404
    
    registro_compra = {
        'id': NEXT_COMPRA_ID,
        'turista_id': turista['id'],
        'turista_email': turista_email,
        'passeio_id': passeio_id,
        'passeio_titulo': passeio_encontrado['titulo'],
        'valor_pago': passeio_encontrado['valor']
    }

    DB_COMPRAS.append(registro_compra)
    NEXT_COMPRA_ID += 1

    return jsonify({
    "mensagem": "Compra registrada com sucesso!",
    "detalhes": registro_compra
}), 201

@app.route('/passeios', methods=['GET'])
def exibir_passeio():
    if not DB_PASSEIOS:
        return jsonify({"mensagem": "Nenhum passeio cadastrado no momento."}), 200
    return jsonify({
        "quanidade": len(DB_PASSEIOS),
        "passeios": DB_PASSEIOS
    }), 200

@app.route('/turista/minhas-compras', methods=['GET'])
def minhas_compras():

    dados = request.get_json()

    if not dados or 'turista_email' not in dados:
        return jsonify({"erro": "Email do Turista é obrigatório para visualização."}), 400
    
    turista_email = dados.get('turista_email')

    turista = checar_turista(turista_email)
    if not turista:
        return jsonify({"erro": "Acesso negado. Apenas Turistas podem ver este histórico."}), 403
    
    turista_id = turista['id']

    minhas_compras = [
        compra for compra in DB_COMPRASif compra['turista_id'] == turista_id
    ]

    if not minhas_compras:
        return jsonify({"mensagem": "Você ainda não possui compras registradas."}), 200
    
    return jsonify({
        "turista_nome": turista['nome'],
        "total_compras": len(minhas_compras),
        "compras": minhas_compras
    }), 200

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

@app.route('/debug/usuarios', methods=['GET'])
def debug_usuarios():
    return jsonify(DB_USUARIOS)

if __name__=='__main__':
    app.run(debug=True)