from .database import db

# a product can be in multiple orders and an order can contain multiple
#products - MANY TO MANY relationship - Association Model
# Reference - https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html#association-object 
class OrderProduct(db.Model):
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'), primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), primary_key=True)
    product = db.relationship("Product", back_populates="orders")
    order = db.relationship("Order", back_populates="products")
    # quantity = db.Column(db.Integer, nullable = False)