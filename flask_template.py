from flask import Flask, request, redirect, jsonify, make_response, current_app

app = Flask(__name__)

# example with post-data
@app.route('/echo', methods=['POST'])
def echo():
    text = request.json['input']
    return jsonify({'output':text})

# example with post-parameters
@app.route('/repeat', methods=['POST'])
def repeat():
    input = request.args['input']
    return jsonify({'output':input})

# example with post-url
@app.route('/pprint/<input>', methods=['POST'])
def pprint(input):
    return jsonify({'output':input})

if __name__ == '__main__':
    app.run()
