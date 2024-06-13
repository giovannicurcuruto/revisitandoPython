from flask import Flask, make_response, jsonify, request
from bd import Carros

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros', methods=['GET'])
def get_carros():
    return make_response(
        jsonify(
            message='Lista de Carros.',
            data = Carros)
    )

@app.route('/carros/<int:id>', methods=['GET'])
def get_carros_by_id(id):
    return make_response(
        jsonify(
            message = f'Carro do id {id}',
            data = Carros[id-1]
        )
    )

@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    Carros.append(carro)
    return make_response(
        jsonify(
            meessage = 'Carro criado com sucesso!',
            data = carro
            )
        )

@app.route('/carros/<int:id>',methods=['DELETE'])
def delete_carro(id):
    global Carros
    Carros = [carro for carro in Carros if carro['id'] != id]
    return make_response(
        jsonify(
            message = f'Carro do id {id}, foi removido com sucesso. '
        ),200
    )

@app.route('/carros/<int:id>', methods=['PUT'])
def update_carro(id):
    carro_new = request.json
    for carro in Carros:
        print(carro['id'])
        if carro['id'] == id:
            carro.update(carro_new)
            carro['id'] = id
            return make_response(
                jsonify({
                    "message": f"Carro com id {id} atualizado",
                    "data": carro
                }),200)
        
    return make_response(
        jsonify({
            "message": "Carro não encontrado"
        }), 404)

app.run()

