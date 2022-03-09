from flask import render_template
from app import app
from models.magic_trick_shop import orders

@app.route('/orders')
def index():
    return render_template('index.html', title = "Orders", orders=orders)

@app.route('/orders/<order_index>')
def order(order_index):
    return render_template('order.html', title = "Order Page", order=orders[int(order_index)])