from flask import Flask, make_response, jsonify, request
from bd import Carros
import psycopg2

#Neste exercicio, o 'from bd import Carros' está em desuso.

hostname = 'localhost'
database = 'flaskdb'
username = 'postgres'
password = 'passpost'
port_id = 5432


conn = psycopg2.connect(
    host = hostname,
    dbname = database,
    user = username,
     password = password,
    port = port_id
)
cur = conn.cursor()


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/carros', methods=['GET'])
def get_carros():
    cur.execute('SELECT * from carros')
    result_db = cur.fetchall()

    return make_response(
        jsonify(
            message='Lista de Carros.',
            data = result_db)
    )

@app.route('/carros/<int:id>', methods=['GET'])
def get_carros_by_id(id):
    cur.execute(f'SELECT * FROM carros where id = {id}')
    result_db = cur.fetchall()
    return make_response(
        jsonify(
            message = f'Carro do id {id}',
            data = result_db
        )
    )

@app.route('/carros', methods=['POST'])
def create_carro():
    carro = request.json
    cur.execute('INSERT INTO carros(marca, modelo, ano) VALUES (%s, %s, %s)', 
                (carro["marca"], carro["modelo"], carro["ano"]))
    conn.commit()
    return make_response(
        jsonify(
            meessage = 'Carro criado com sucesso!',
            data = carro
            )
        )

@app.route('/carros/<int:id>',methods=['DELETE'])
def delete_carro(id):
    cur.execute(f'DELETE FROM carros WHERE ID = {id}')
    return make_response(
        jsonify(
            message = f'Carro do id {id}, foi removido com sucesso. '
        ),200
    )

@app.route('/carros/<int:id>', methods=['PUT'])
def update_carro(id):
    carro_new = request.json
    print(carro_new)
    cur.execute(
        'UPDATE carros set marca=%s, modelo=%s, ano=%s where id=%s',
        (carro_new['marca'], carro_new['modelo'], carro_new['ano'], id)
    )
    conn.commit()
    return make_response(
        jsonify({
            "message": f"Carro com id {id} atualizado",
            "data": carro_new
        }),200)
        


app.run()

