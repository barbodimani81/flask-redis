from flask import Flask
import redis

app = Flask(__name__)
cache = redis.Redis(host='redis', port=6379)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World and docker compose!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5555)
