import random
import os
import requests
from flask import Flask, render_template, request
from MemeEngine import MemeEngine
from QuoteEngine import Ingestor

app = Flask(__name__)

meme = MemeEngine.MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    quotes = []

    for file in quote_files:
            quotes.extend(Ingestor.parse(file))

    for file in quote_files:
        print(file)
        quotes += Ingestor.parse(file)
        print(Ingestor.parse(file))


    images_path = "./_data/photos/dog/"

    imgs = None
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """

    img = None
    quote = None

    img = random.choice(imgs)
    quote = random.choice(quotes)

    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    try:
        image_url = request.form['image_url']
        r = requests.get(image_url, allow_redirects=True)
        f_name = f'./static/{random.randint(0, 100000000)}.jpg'
        img = open(f_name, 'wb')
        img.write(r.content)
        img.close()
        meme = MemeEngine.MemeEngine('./static')
        body = request.form['body']
        author = request.form['author']
        path = meme.make_meme(f_name, body, author)
    except Exception:
        print("Invalid URL")
        return render_template('meme_error.html')

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
