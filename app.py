from flask import Flask, g
from flask_cors import CORS
import models
from resources.craftable_items import craftable_item

DEBUG = True
PORT = 5000


app = Flask(__name__)


'''
DB CONNECTION
'''

@app.before_request
def before_request():
  g.db = models.DATABASE
  g.db.connect()


@app.after_request
def after_request(response):
  g.db.close()
  return response


CORS(craftable_item, origins=['http://localhost:8080'], supports_credentials=True)
app.register_blueprint(craftable_item, url_prefix='/api/v1/craftable-items')


@app.route('/')
def index():
  return 'Hello World!'


if __name__ == '__main__':
  models.initialize()
  # models.createdb()
  app.run(debug=DEBUG, port=PORT)