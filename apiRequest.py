from flask import Flask, jsonify
from flask import make_response
from flask import request
from ProductRecommendation import recom
import json

app = Flask(__name__)
f = open('meta.json', )
products = json.load(f)
f.close()

@app.route('/api/products', methods=['GET'])
def get_products():
    return jsonify({'products': products})

@app.route('/api/products/<string:product_id>', methods=['GET'])
def get_product(product_id):
    #product =[product for product in products['meta'][]  == product_id]
    for each in products['meta']:
        if each['productid']==product_id:
            product=product_id
    if len(product) == 0:
        return jsonify({'product': 'Not found'}),404

    post=recom(product)
    post=post.to_json(orient="table")
    return jsonify({'products': post})

if __name__ == '__main__':
    app.run()
