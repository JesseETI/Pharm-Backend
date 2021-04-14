from .database import db
from datetime import datetime

#Order model
class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="orders")
    item_count = db.Column(db.Integer, nullable=False)
    order_total = db.Column(db.Float(decimal_return_scale=2), nullable=False)
    date_placed = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    pickup_status = db.Column(db.String(50), nullable=False)
    products = db.relationship("OrderProduct", back_populates="order",  cascade="all,delete")

    def toDict(self):
        return{
            "id" : self.id,
            "user" : self.user.toDict(),
            "item_count": self.item_count,
            "order_total": round(self.order_total,2),
            "date_placed": self.date_placed.strftime("%a, %d %b, %Y"),
            "status": self.pickup_status,
            "products": [OrderProduct.product.toDict() for OrderProduct in self.products]
        }