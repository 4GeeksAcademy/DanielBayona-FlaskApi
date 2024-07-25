from flask import Flask, jsonify, request
app =  Flask(__name__)

todos = [
{
    "label": "My first task",
    "done": False
},
{
    "label": "My second task",
    "done": False
}
]

@app.route('/todos', methods=['GET'])
def hello_world():
    response = jsonify(todos)
    response.status_code = 200
    return response

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    todos.append(request_body)
    print('Incoming request with the following body', request_body)
    return jsonify(todos) , 200

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position is not None:
        for item in range(len(todos)):
            if position == item:
                todos.remove(todos[item])

    return jsonify(todos)
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)