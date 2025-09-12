from flask import Flask, jsonify, request

app = Flask(__name__)

# dados fictícios para nossa API
terceirao = [
    {"id": 1, "nome": "Paulo Silas", "Série": "3° Safira"},
    {"id": 2, "nome": "Mailon", "Série": "3° Rubi"}
]

# rota inicial
@app.route("/")
def home():
    return "🚀 API de Carros funcionando!"

# GET
@app.route("/terceirao", methods=["GET"])
def listar_terceirao():
    return jsonify(terceirao)

# POST
@app.route("/terceirao", methods=["POST"])
def adicionar_terceirao():
    novo_terceirao = request.get_json()
    terceirao.append(novo_terceirao)
    return jsonify({
        "Notificação": "Nome adicionado com sucesso!",
        "aluno": novo_terceirao
    })

# PUT
@app.route("/terceirao/<int:id>", methods=["PUT"])
def atualizar_terceirao(id):
    for aluno in terceirao:
        if aluno["id"] == id:
            dados = request.get_json()
            aluno.update(dados)
            return jsonify({
                "Notificação": "Dados atualizados!",
                "aluno": aluno
            })
    return jsonify({"Erro": "Dados não encontrados!"}), 404

# DELETE
@app.route("/terceirao/<int:id>", methods=["DELETE"])
def deletar_terceirao(id):
    for aluno in terceirao:
        if aluno["id"] == id:
            terceirao.remove(aluno)
            return jsonify({"Mensagem": "Aluno removido com sucesso!"})
    return jsonify({"Erro": "Dados não encontrados!"}), 404

# Roda o app
if __name__ == "__main__":
    app.run(debug=True)
