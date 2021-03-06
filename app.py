import os
from flask import Flask, jsonify, g
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


CORS(craftable_item, origins=['http://localhost:8080', 'https://sdv-resource-calculator.vercel.app/'], supports_credentials=True, resources={r"/api/*": {"origins": "*"}})
app.register_blueprint(craftable_item, url_prefix='/api/v1/craftable-items')


if 'ON_HEROKU' in os.environ: 
  models.initialize()
  models.create_craftable_items_row()


if __name__ == '__main__':
  models.initialize()
  models.create_craftable_items_row()
  app.run(debug=DEBUG, port=PORT)