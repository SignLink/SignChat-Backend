from flask import Flask, render_template
from flask import request, jsonify
from keras.models import load_model
import tensorflow as tf


app = Flask(__name__)

@app.route('/')

def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(debug=True)


#class ModelConfig(AppConfig):
   # default_auto_field = 'django.db.models.BigAutoField'
    #name = 'Model'


