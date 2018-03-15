from flask import Flask
from crawl import get_jobs

app = Flask(__name__)
get_job = get_jobs


@app.route('/api/v1/job/<palavra_chave>')
def get_jobs(palavra_chave):
    palavra = palavra_chave.replace(' ', '+')
    palavra = palavra_chave.replace(',', '+')
    palavra.lower()
    print(palavra)
    return get_job(palavra)


if __name__ == '__main__':
    app.run(host='0.0.0.0')

