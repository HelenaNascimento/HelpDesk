from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista para armazenar os tickets
tickets = []


@app.route('/')
def index():
    return render_template('index.html', tickets=tickets)


@app.route('/abrir_ticket', methods=['GET', 'POST'])
def abrir_ticket():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        tickets.append({'titulo': titulo, 'descricao': descricao, 'status': 'Aberto'})
        return redirect(url_for('index'))
    return render_template('abrir_ticket.html')


if __name__ == '__main__':
    app.run(debug=True)
