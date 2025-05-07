from flask import Flask

app= Flask(__name__)
@app.route('/')
def home():
    return"<h1> !Hola, esta es mi pagina web en producciòn con Python</h1>¡"
if __name__=='__main__':
    app.run()   