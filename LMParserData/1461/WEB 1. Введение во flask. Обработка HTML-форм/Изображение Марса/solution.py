from flask import Flask

app = Flask(__name__)


@app.route('/')
def osn():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return "</br>".join(["Человечество вырастает из детства.", 
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!", "Присоединяйся!"])


@app.route('/image_mars')
def image_mars():
    return """<title>Привет Марс!</title><h1>Жди нас, Марс!</h1>
<img src="https://img.freepik.com/premium-photo/png-outdoors-planet-space-moon_53876-920835.jpg?semt=ais_hybrid&w=740">
</br>Вот она какая, красная планета."""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')