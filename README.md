# MvpBackEnd
📌 Projeto: Plataforma Web para Serviços Turísticos

MVP desenvolvido em Python + Flask (sem banco de dados), utilizando VS Code + REST Client e Figma (construção de protótipo).

👤 Equipe

| Nome                    | Função                                          |
| ------------------------| ------------------------------------------------|
| Sanderson Santos        | Desenvolvedor Back-End / Idealizador do Projeto |




## 🎯 **Situação-Problema** **Selecionada** **:** Circuito Saquarema Verde

Atualmente, profissionais do setor turístico como guias, historiadores, fotógrafos, educadores físicos e outros enfrentam dificuldade para divulgar atividades e passeios em um ambiente digital simples e acessível.

Da mesma forma, turistas buscam uma plataforma direta onde possam: 
- visualizar passeios disponíveis,
- comprar ingressos e
- acompanhar informações.




## 🚀 **Descrição** **do** **MVP**

Este MVP implementa uma API Flask sem banco de dados, utilizando apenas listas e dicionários em memória, com foco em demonstrar regras de negócio essenciais para uma plataforma turística.

O sistema possui três tipos de usuários, cada um com permissões específicas:

👤 Turista

Visualiza passeios

Realiza compras

Consulta histórico de compras

🧑‍💼 Parceiro

Cadastra passeios

Edita seus próprios passeios

Gerencia conteúdo relacionado às atividades oferecidas

👨‍💼 Administrador

Edita a Publicação principal da página inicial

Exclui/Reseta a Publicação


### ✔ **Funcionalidades** **incluídas** **no** **MVP:**

🔐 Autenticação

- Cadastro de usuários (Turista, Parceiro, Administrador)

- Login com validação de e-mail + senha

- Identificação automática do tipo de usuário após login

📰 Publicação Principal (Admin)

- Editar título, descrição e imagem

- Excluir/resetar a publicação

- Conteúdo exibido a qualquer visitante

🧭 Gestão de Passeios (Parceiro)

- Cadastro de passeios com:

  - título

  - descrição

  - valor

  - imagem

  - data do passeio

  - horário de partida/retorno

- Edição de passeios existentes

- Validação para impedir que turistas criem ou editem passeios

- Apenas o dono do passeio pode editá-lo

🎟️ Compra de Passeios (Turista)

- Turista realiza compra informando seu e-mail e ID do passeio

- Registro da compra associando Turista ↔ Passeio

- Parceiros e Administradores são impedidos de comprar

- Turista acessa seu histórico com todos os passeios adquiridos

🧪 Validações

- Campos obrigatórios

- Tipos de usuário em cada rota

- Impedir cadastro duplicado

- Impedir operações não permitidas

- Retorno de mensagens claras + HTTP status apropriado

💾 Armazenamento

- Feito totalmente em memória (listas, dicionários)

- Reiniciado sempre que o servidor Flask é reiniciado

## 🖥️ Como Executar o Projeto Localmente
🔧 Pré-requisitos

- Python 3.10+

- Flask instalado

- VS Code (opcional, porém recomendado)

- Extensão REST Client para rodar o arquivo teste.http

### 📥 1. Clonar o repositório

git clone https://github.com/SandersonTI/MvpBackEnd.git  


### 📦 2. Instalar dependências

pip install flask  


### ▶ 3. Executar o servidor

python app.py  

O servidor iniciará em:  
http://127.0.0.1:5000  

### 🧪 4. Executar os testes com REST Client (teste.http)  
No VS Code, abra o arquivo:  

teste.http  

E clique no botão Send Request em cada bloco de requisição para testar todas as rotas implementadas.  

  
### 🧩 Informações Adicionais
___
O MVP foi desenvolvido com foco em clareza, validações sólidas, segurança de permissões e simplicidade arquitetural, garantindo uma base consistente para futuras evoluções.

🔧 **Arquitetura e Expansão Futura**

- Estrutura preparada para migração rápida para banco de dados reais (PostgreSQL, MySQL, MongoDB).

- Código organizado por rotas, com validações específicas para cada tipo de usuário (Turista, Parceiro e Administrador).

- Lógica totalmente compatível para expansão futura como:

  - Interface visual completa (Frontend)

  - Autenticação com tokens JWT

  - Painéis de controle para Parceiros e Administradores

  - Relatórios e dashboards

  - Persistência completa em banco de dados

⚙️ **Pilares do MVP**

- Este MVP demonstra de forma integrada:

- Fluxo completo de autenticação (login + identificação de perfil)

- Operações CRUD com permissões (passeios, publicação, compras)

- Regras de negócio aplicadas de forma explícita e validada

Manipulação de dados em memória com respostas JSON padronizadas

Estrutura simples, porém preparada para ganhar robustez conforme o projeto evoluir
