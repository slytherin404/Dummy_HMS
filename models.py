from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contact = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default="admin", nullable=False)

    # One Admin can create many Sellers
    sellers = db.relationship('Seller', backref='created_by_admin', lazy=True)


class Seller(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # created by admin
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contact = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    storage_capacity = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(20), default="seller", nullable=False)
    # NEW: status field -> active / blocked / deleted
    status = db.Column(db.String(20), default="active", nullable=False)
    # Available days - JSON string storing list of dates when seller is available
    open_dates = db.Column(db.Text, nullable=True)

    # Link to Admin
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=True)

    # Seller has many storage items
    storages = db.relationship('Storage', backref='seller', lazy=True)

    # Orders received by Seller
    orders = db.relationship('Order', backref='seller', lazy=True)


class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    contact = db.Column(db.String(15), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(20), default="customer", nullable=False)
    # NEW: status field -> active / blocked / deleted
    status = db.Column(db.String(20), default="active", nullable=False)

    # Orders placed by Customer
    orders = db.relationship('Order', backref='customer', lazy=True)


class Storage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    product_quantity = db.Column(db.Integer, nullable=False)
    product_price = db.Column(db.Float, nullable=False)

    # Belongs to one seller
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'), nullable=False)


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.Float, nullable=False)
    # NEW: status field -> pending / accepted / delivered / out_of_stock
    status = db.Column(db.String(20), default="pending", nullable=False)

    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    seller_id = db.Column(db.Integer, db.ForeignKey('seller.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('storage.id'), nullable=False)

    # Order references a product
    product = db.relationship('Storage', backref='orders')
