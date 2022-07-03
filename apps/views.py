from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


@app.route('/')
def indexView():
    return "Hello World !"


if __name__ == "__main__":
    app.run()
