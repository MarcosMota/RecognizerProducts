#!-*- conding: utf8 -*-
from flask import Flask, request, redirect, url_for,jsonify
import tensorflow as tf
import numpy as np
from PIL import Image

FILE_LABEL = './models/brand/labels.txt'
FILE_GRAPH = './models/brand/graph.pb'

def getTags(image):
    limit = 0.0
    result = list()
    # Carrega o arquivo de etiqueta
    label_lines = [line.rstrip() for line
        in tf.gfile.GFile(FILE_LABEL)]
    # Carrega o arquivo do graph do tensor
    with tf.gfile.FastGFile(FILE_GRAPH, 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')
    # Com a imagem como entrada para que o tensor obtenha a primeira previsao
    with tf.Session() as sess:
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor, {'DecodeJpeg/contents:0': image})
        # Ordenar para mostrar os rotulos da primeira previsao em ordem de confianca
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
        for node_id in top_k:
            human_string = label_lines[node_id]
            score = predictions[0][node_id]
            # Adicionar somente as etiquetas que forem maior que o valor de corte
            if(score > limit):
                result.append(human_string)
    # Retorna as etiquetas
    return result
