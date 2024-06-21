from app import db

class Inventory(db.Model):
    __tablename__ = 'inventory'
    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(255), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)
    

class SalesOrder(db.Model):
    __tablename__ = 'sales_order'
    order_id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(255), nullable=False)
    order_date = db.Column(db.Date, nullable=False)
    total_amount = db.Column(db.Numeric(10, 2), nullable=False) 
    shipping_address = db.Column(db.String(255), nullable=False)
    payment_method = db.Column(db.String(20), nullable=False)
    
class OrderItem(db.Model):
    __tablename__ = 'order_items'
    order_item_id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('sales_order.order_id'))
    item_id = db.Column(db.Integer, db.ForeignKey('inventory.item_id'))
    quantity = db.Column(db.Integer, nullable=False)
    unit_price = db.Column(db.Numeric(10, 2), nullable=False)