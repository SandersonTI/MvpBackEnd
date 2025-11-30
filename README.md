# MvpBackEnd
📌 Projeto: Plataforma Web para Serviços Turísticos

MVP desenvolvido em Python + Flask (sem banco de dados), utilizando VS Code + REST Client.

| Nome                 | Funcao                                          |
| -------------------- | ----------------------------------------------- |
| **Sanderson Santos** | Desenvolvedor Back-End / Idealizador do Projeto |




## 🎯 **Situação-Problema** **Selecionada** **:** Circuito Saquarema Verde

Atualmente, profissionais do setor turístico como guias, historiadores, fotógrafos, educadores físicos e outros enfrentam dificuldade para divulgar atividades e passeios em um ambiente digital simples e acessível.

Da mesma forma, turistas buscam uma plataforma direta onde possam visualizar passeios disponíveis, comprar ingressos e acompanhar informações.




## 🚀 **Descrição** **do** **MVP**

O MVP consiste em uma plataforma web sem banco de dados, focada em demonstrar o funcionamento básico de um sistema de serviços turísticos.

Ele possui três tipos de usuários:

Turista → visualiza passeios e realiza compras

Parceiro → cadastra e gerencia passeios

Administrador → edita a publicação principal da página inicial


### ✔ **Funcionalidades** **incluídas** **no** **MVP:**

- Cadastro de usuários (Turista, Parceiro, Administrador)

- Login e identificação do tipo de usuário

- Edição e exclusão da Publicação principal (Administrador)

- Cadastro de passeios (Parceiro)

- Listagem pública de passeios

- Compra de passeios (Turista)

- Histórico de compras (Turista)

- Validações completas baseadas em regras de negócio

- Armazenamento temporário em memória (listas/dicionários)


## 🖥️ Como Executar o Projeto Localmente
🔧 Pré-requisitos

- Python 3.10+

- Flask instalado

- VS Code (opcional, porém recomendado)

- Extensão REST Client (para rodar o teste.http)

### 📥 1. Clonar o repositório

git clone https://github.com/SandersonTI/MvpBackEnd.git  


### 📦 2. Instalar dependências

pip install flask  


### ▶ 3. Executar o servidor

python app.py  

O servidor iniciará em:  
http://127.0.0.1:5000  

### 🧪 4. Executar os testes (teste.http)  
No VS Code, abra o arquivo:  

teste.http  

E clique no botão Send Request em cada bloco de requisição.


