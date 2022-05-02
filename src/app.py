from flask import Flask, jsonify,request, json

app = Flask (__name__)

todos=[{"label":"Walk the dog","done":False},{"label":"Wake up","done":False}]
@app.route('/todos', methods=['GET'])
def handle_todo():
    json_todos= jsonify(todos)
    return json_todos

@app.route('/todos',methods=['POST'])
def add_new_todo():
    request_body=request.data
    print('Incoming request with the following body',request_body)
    decoded_object=json.loads(request_body)
    todos.append(decoded_object)
    return jsonify(todos)

@app.route('/todos/<int:position>',methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    todos.pop(position)
    return jsonify(todos)

if __name__=='__main__':
    app.run(host='127.0.0.1',port=8000,debug=True)