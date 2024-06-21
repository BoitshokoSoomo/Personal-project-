from flask import render_template, request, redirect, url_for
from app import app, db
from models import Inventory, SalesOrder, OrderItem

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inventory')
def inventory():
    items = Inventory.query.all()
    return render_template('inventory.html', items=items)

@app.route('/add_inventory', methods=['POST'])
def add_inventory():
    item_name = request.form['item_name']
    quantity = request.form['quantity']
    price = request.form['price']
    new_item = Inventory(item_name=item_name, quantity=quantity, price=price)
    db.session.add(new_item)
    db.session.commit()
    return redirect(url_for('inventory'))

@app.route('/sales_orders')
def sales_orders():
    orders = SalesOrder.query.all()
    return render_template('sales_orders.html', orders=orders)

@app.route('/add_sales_order', methods=['POST'])
def add_sales_order():
    customer_name = request.form['customer_name']
    order_date = request.form['order_date']
    total_amount = request.form['total_amount']
    new_order = SalesOrder(customer_name=customer_name, order_date=order_date, total_amount=total_amount)
    db.session.add(new_order)
    db.session.commit()
    return redirect(url_for('sales_orders'))
