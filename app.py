# importe os módulos necessários
from flask import Flask , render_template , request , jsonify

# importando arquivo sentiment_analysis como sa
import sentiment_analysis as sa

app = Flask(__name__)

# rota do aplicativo para a página index
@app.route('/')
def home():
    return render_template('index.html')

# escreva uma rota para requisição post
@app.route('/predict' , methods = ['POST'])
def review():
    response = ""
    # extraia a avaliação do cliente escrevendo a "chave" apropriada dos dados JSON
    review = request.json.get('customer_review')

    # verifique se a avaliação do cliente está vazia, então retorne o erro
    if not review:

        return jsonify({'status' : 'error' , 
                        'message' : 'Avaliação em branco'})

    # se a avaliação não estiver vazia, passe-a pela função 'predict'.
    # a função predict retorna 2 coisas: o sentimento e o caminho da imagem na pasta static
    # exemplo : Positivo , ./static/assets/emoticons/positive.png

    else:

        sentiment , emoji_url = sa.predict(review)

        response =jsonify({'status' : 'Success',
                            'prediction' : sentiment,
                            'url' : emoji_url})

        return response
if __name__  ==  "__main__":
    app.run(debug = True)