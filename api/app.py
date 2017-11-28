from flask import Flask, request, redirect, url_for
import tensorflow as tf
from flask import jsonify
import numpy as np
from PIL import Image

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Seja bem vindo a API do I See You!!!'

@app.route('/api/recognizer', methods=["POST"])
def recognizer():
    corte = 0.0
    result = []
    # Read in the image_data
    image_data = tf.gfile.FastGFile('image.jpg', 'rb').read()
    # Loads label file, strips off carriage return
    label_lines = [line.rstrip() for line
        in tf.gfile.GFile("./model/labels.txt")]
    # Unpersists graph from file
    with tf.gfile.FastGFile("./model/graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
    # Feed the image_data as input to the graph and get first prediction
    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': request.data})
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            if(score > corte):
                result.append({'%s ' % (human_string):'%.5f' % (score * 100)})
    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
