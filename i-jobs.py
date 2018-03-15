from flask import Flask
from crawl import get_jobs
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)


@app.route('/api/v1/job/<palavra_chave>')
def jobs(palavra_chave):
    palavra = palavra_chave.replace(' ', '+')
    palavra = palavra_chave.replace(',', '+')
    palavra.lower()
    print(palavra)
    return get_jobs(palavra)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

