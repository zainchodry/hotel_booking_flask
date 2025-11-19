from app.extenshions import db
from flask_login import UserMixin
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    bookings = db.relationship("Booking", backref="user", lazy=True)

    def __repr__(self):
        return f"<User {self.username}>"

class Room(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    room_number = db.Column(db.String(20), unique=True, nullable=False)
    room_type = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    is_available = db.Column(db.Boolean, default=True)

    bookings = db.relationship("Booking", backref="room", lazy=True)

    def __repr__(self):
        return f"<Room {self.room_number}>"

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    room_id = db.Column(db.Integer, db.ForeignKey("room.id"), nullable=False)
    check_in = db.Column(db.Date, nullable=False)
    check_out = db.Column(db.Date, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Booking {self.id}>"