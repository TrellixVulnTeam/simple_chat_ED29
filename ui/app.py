from flask import Flask, render_template, request
from flask import jsonify, url_for

app = Flask(__name__,static_url_path="/static")

#############
# Routing
#
@app.route('/message', methods=['POST'])
def reply():
    return jsonify( { 'text': execute.decode_line(sess, model, enc_vocab, rev_dec_vocab, request.form['msg'] ) } )


@app.route('/respond/', methods=['POST'])
def repl():
    return jsonify({'text': execute.decode_line(sess, model, enc_vocab, rev_dec_vocab, request.get_json()['msg'])})


@app.route("/")
def index():
    return render_template("index.html")
#############

@app.route("/onboarding")
def onboarding():
    return render_template("index.html")

'''
Init seq2seq model

    1. Call main from execute.py
    2. Create decode_line function that takes message as input
'''
# _____________________________________________________________

import sys
import os.path

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))
import tensorflow as tf
import execute

sess = tf.Session()
sess, model, enc_vocab, rev_dec_vocab = execute.init_session(sess, conf='seq2seq_serve.ini')
# _________________________________________________________________

# start app
if (__name__ == "__main__"):
    app.run(port=5000)
