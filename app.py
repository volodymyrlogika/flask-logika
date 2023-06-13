from flask import Flask, render_template

app = Flask(__name__) #створюємо Flask-додаток

@app.route("/")
def hello_world():
    return render_template("index.html")

@app.route("/logika")
def logika():
    return render_template("logika.html")

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)

"""
venv\Scripts\activate
python app.py
"""