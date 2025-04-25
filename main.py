from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")
@app.route("/calculo", methods=['POST'])
def calculadora():
    resultado = ""
    numero1 = int(request.form['numero1'])
    numero2 = int(request.form['numero2'])
    operacao = str(request.form['operacao'])

    if operacao == '+':
        resultado = numero1 +  numero2
    elif operacao == '-':
        resultado = numero1 - numero2
    elif operacao == '*':
        resultado = numero1 * numero2
    elif operacao == '/':
        resultado = numero1/numero2

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)


