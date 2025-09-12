from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1> Olá meus Oompa Loompas </h1>"


@app.route('/perfil')
def perfil():
    return render_template("index.html")


app.run(debug=True)