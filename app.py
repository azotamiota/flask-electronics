from crypt import methods
from flask import Flask, render_template, url_for

app = Flask(__name__)

electronics = [
    {'id': 1, 'type': 'phone', 'brand-model': 'IPhone 11', 'colour' : 'white', 'image': 'https://www.backmarket.co.uk/cdn-cgi/image/format=auto,quality=75,width=640/https://d1eh9yux7w8iql.cloudfront.net/product_images/290036_5a2ddcac-5a87-4462-9e9f-30a304b5e215.jpg'},
    {'id': 2, 'type': 'laptop', 'brand-model': 'Dell 2314H', 'colour' : 'black', 'image': 'https://i.dell.com/is/image/DellContent/content/dam/ss2/product-images/dell-client-products/notebooks/inspiron-notebooks/15-3520/media-gallery/in3520-cnb-05000ff090-sl.psd?fmt=png-alpha&pscan=auto&scl=1&hei=402&wid=402&qlt=100,0&resMode=sharp2&size=402,402'},
    {'id': 3, 'type': 'PC', 'brand-model': 'Asus 12-KH', 'colour' : 'grey', 'image': 'https://www.scan.co.uk/images/products/3074140-a.jpg'},
    {'id': 4, 'type': 'camera', 'brand-model': 'Canon 1150D', 'colour' : 'red', 'image': 'https://www.backmarket.co.uk/cdn-cgi/image/format=auto,quality=75,width=640/https://d1eh9yux7w8iql.cloudfront.net/product_images/35738_94f1041f-82c0-4cde-8c20-fe2072495873.jpg'}
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    return render_template('products.html', electronics=electronics, title='Products')

@app.route('/products/<int:id>/', methods=['GET', 'DELETE', 'PATCH'])
def one_product(id):
    matching_product = [product for product in electronics if product['id'] == id ]
    return render_template('one_product.html', product=matching_product[0], title=matching_product[0]['brand-model'], image=matching_product[0]['image'])

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)

