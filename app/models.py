from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'Users'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(100))
    phone = db.Column(db.String(20))
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    is_active = db.Column(db.Boolean, default=True)

class AvailabilityStatus(db.Model):
    __tablename__ = 'AvailabilityStatus'
    availability_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.String(100), unique=True, nullable=False)

class Brand(db.Model):
    __tablename__ = 'Brands'
    brand_id = db.Column(db.Integer, primary_key=True)
    brand_name = db.Column(db.String(100), nullable=False)

class Product(db.Model):
    __tablename__ = 'Products'
    product_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    sku = db.Column(db.String(100), unique=True, nullable=False)
    types = db.Column(db.JSON, nullable=False)
    availability_id = db.Column(db.Integer, db.ForeignKey('AvailabilityStatus.availability_id'), nullable=False)
    description = db.Column(db.Text)
    image = db.Column(db.String(200))
    price = db.Column(db.Numeric(10,2), nullable=False)
    brand_id = db.Column(db.Integer, db.ForeignKey('Brands.brand_id'))
    stock = db.Column(db.Integer)

class OrderStatus(db.Model):
    __tablename__ = 'OrderStatus'
    order_status_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)

class ShippingType(db.Model):
    __tablename__ = 'ShippingTypes'
    shipping__type_id = db.Column(db.Integer, primary_key=True)
    shipping_cost = db.Column(db.Numeric(10,2), nullable=False)

class Order(db.Model):
    __tablename__ = 'Orders'
    order_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'), nullable=False)
    invoice_required = db.Column(db.Boolean, nullable=False)
    order_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    total_amount = db.Column(db.Numeric(10,2))
    order_status_id = db.Column(db.Integer, db.ForeignKey('OrderStatus.order_status_id'), nullable=False)
    shipping_type = db.Column(db.Integer, db.ForeignKey('ShippingTypes.shipping__type_id'))
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())

class OrderDetail(db.Model):
    __tablename__ = 'OrderDetails'
    order_id = db.Column(db.Integer, db.ForeignKey('Orders.order_id', ondelete='CASCADE'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('Products.product_id'), primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)

class InvoiceDetail(db.Model):
    __tablename__ = 'InvoiceDetails'
    invoice_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id', ondelete='CASCADE'), nullable=False)
    order_id = db.Column(db.Integer, db.ForeignKey('Orders.order_id', ondelete='CASCADE'), nullable=False)
    rfc = db.Column(db.String(13), nullable=False)
    address = db.Column(db.String(200))
    email = db.Column(db.String(100))
    razon_social = db.Column(db.String(200))
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    updated_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
