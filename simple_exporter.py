from flask import Flask, Response

app = Flask(__name__)

@app.route('/metrics')
def metrics():
    return Response('my_custom_metric 1\n', mimetype='text/plain')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
