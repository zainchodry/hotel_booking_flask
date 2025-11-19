from flask import request, render_template, redirect, url_for, flash, Blueprint
from app.models import *
from app.extenshions import *
from flask_login import login_required, current_user

main = Blueprint("main", __name__)




@main.route("/")
def index():
    return render_template("index.html")

@main.route("/rooms")
def rooms():
    all_rooms = Room.query.all()
    return render_template("rooms.html", rooms=all_rooms)

@main.route("/room/<int:room_id>", methods=["GET", "POST"])
def room_detail(room_id):
    room = Room.query.get_or_404(room_id)

    if request.method == "POST":
        if not current_user.is_authenticated:
            flash("You must be logged in to book a room", "danger")
            return redirect(url_for("main.login"))

        check_in = request.form.get("check_in")
        check_out = request.form.get("check_out")

        booking = Booking(
            user_id=current_user.id,
            room_id=room.id,
            check_in=datetime.strptime(check_in, "%Y-%m-%d"),
            check_out=datetime.strptime(check_out, "%Y-%m-%d")
        )

        room.is_available = False
        db.session.add(booking)
        db.session.commit()

        flash("Room booked successfully!", "success")
        return redirect(url_for("main.bookings"))

    return render_template("room_detail.html", room=room)

@main.route("/bookings")
@login_required
def bookings():
    user_bookings = Booking.query.filter_by(user_id=current_user.id).all()
    return render_template("bookings.html", bookings=user_bookings)

@main.route("/manage-rooms", methods=["GET", "POST"])
def manage_rooms():
    if request.method == "POST":
        room_number = request.form.get("room_number")
        room_type = request.form.get("room_type")
        price = request.form.get("price")

        new_room = Room(room_number=room_number, room_type=room_type, price=price)
        db.session.add(new_room)
        db.session.commit()

        flash("Room added successfully!", "success")
        return redirect(url_for("main.manage_rooms"))

    rooms = Room.query.all()
    return render_template("manage_rooms.html", rooms=rooms)
